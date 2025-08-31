from manim import *
import pygraphviz

import sys

LINK_COLOR = DARK_BROWN
LINK_WIDTH = 7
IMG_FOLDER = "img_low_q"

FILE_KEYS = {}
with open("slide_keys.txt", "r") as f:
    for i, line in enumerate(f.read().splitlines()):
        split = line.split(" ")
        name = split[0]
        val = split[1]
        if name not in FILE_KEYS:
            FILE_KEYS[name] = {}
        FILE_KEYS[name][val] = f"Slide{i + 1}"


class CardContents(Group):

    def __init__(self, name, start_zoomed=False, *args, **kwargs):
        super().__init__(*args, **kwargs, z_index=-1)

        self.rect = PlaceHolderRectangle(z_index=-1)
        self.imgs_enabled = True
        self.imgs = {}
        self.name = name
        if self.imgs_enabled:
            self.current_icon = "1.0"
            icon = self.get_image(self.current_icon)

            self.current_slide = "1.1"
            slide = self.get_image(self.current_slide)

            if start_zoomed:
                self.currently_showing = self.get_current_slide()
                slide.set_opacity(1)
            else:
                self.currently_showing = self.get_current_icon()
                icon.set_opacity(1)

            self.add(self.rect)
            self.add(icon)
            self.add(slide)
        else:
            self.text = Text(name, color=BLACK)
            if self.text.width >= self.rect.width * 0.8:
                self.text.scale_to_fit_width(self.rect.width * 0.8)

            self.add(self.rect)
            self.add(self.text)

    def get_image(self, key):
        if key in self.imgs:
            return self.imgs[key]

        img = ImageMobject(
            f"./{IMG_FOLDER}/{FILE_KEYS[self.name][key]}.png",
            z_index=0,
        ).set_opacity(0)
        img.scale_to_fit_width(self.rect.width * 0.9)

        img.move_to(self.rect.get_center())
        self.imgs[key] = img
        self.add(img)
        return img

    def show_img(self, key):
        if self.imgs_enabled and key != self.currently_showing:
            current = self.get_image(self.currently_showing)
            img = self.get_image(key)
            current.set_opacity(0)
            img.set_opacity(1)
            self.currently_showing = key

    def set_opacity(self, value):
        self.rect.set_opacity(value)
        if self.imgs_enabled:
            self.imgs[self.currently_showing].set_opacity(value)
        else:
            self.text.set(opacity=value)

    @override_animate(set_opacity)
    def _animate_set_opacity(self, value, anim_args=None):
        if anim_args is None:
            anim_args = {}

        anims = []

        anims.append(self.rect.animate.set_opacity(value))
        # print(self.name, " setting opacity to ", value)
        if self.imgs_enabled:
            anims.append(self.imgs[self.currently_showing].animate.set_opacity(value))
        else:
            anims.append(self.text.animate.set(opacity=value))
        return AnimationGroup(*anims)

    @override_animate(show_img)
    def _animate_show_img(self, key, lag_ratio=None, anim_args=None):
        if anim_args is None:
            anim_args = {}

        if self.imgs_enabled and key != self.currently_showing:
            current_img = self.get_visible()
            new_img = self.get_image(key)
            self.add(new_img)
            if lag_ratio is not None:
                anim = AnimationGroup(
                    new_img.animate.set_opacity(1),
                    current_img.animate.set_opacity(0),
                    lag_ratio=0.3,
                )
            else:
                anim = AnimationGroup(
                    new_img.animate.set_opacity(1),
                    current_img.animate.set_opacity(0),
                )

            self.currently_showing = key
            return anim
        else:
            return None

    def get_visible(self):
        if self.imgs_enabled:
            return self.get_image(self.currently_showing)
        else:
            return None

    def get_current_icon(self):
        if self.imgs_enabled:
            return self.current_icon
        else:
            return None

    def get_current_slide(self):
        if self.imgs_enabled:
            return self.current_slide
        else:
            return None


class PlaceHolderRectangle(Rectangle):
    def __init__(self, *args, **kwargs):
        super().__init__(
            fill_color=WHITE,
            stroke_width=LINK_WIDTH / 2,
            stroke_color=LINK_COLOR,
            fill_opacity=1,
            width=1.6,
            height=0.9,
            *args,
            **kwargs,
        )


class SplineEdge(VMobject):
    def __init__(
        self,
        control_points,
        stroke_color=LINK_COLOR,
        stroke_width=7,
        z_index=-2,
        cap_style=CapStyleType.ROUND,
        **kwargs,
    ):

        super().__init__(
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            cap_style=cap_style,
            z_index=z_index,
            **kwargs,
        )

        self.add_cubic_bezier_curve(*control_points[:4])
        for i in range(4, len(control_points), 3):
            self.add_cubic_bezier_curve_to(
                control_points[i], control_points[i + 1], control_points[i + 2]
            )


class CardGraph(Group):
    def __init__(self):
        super().__init__()
        self.cards = {}
        self.links = {}
        self.card_positions = {}
        self.spline_data = {}

    def add_link(
        self,
        name1,
        name2,
        spline_data=None,
        start_zoomed=False,
    ):
        self.add_card(name1, start_zoomed=start_zoomed)
        self.add_card(name2, start_zoomed=start_zoomed)

        if (name1, name2) not in self.links:
            try:
                self.links[(name1, name2)] = SplineEdge(
                    self.spline_data[(name1, name2)]
                )
            except KeyError:
                if (name2, name1) in self.spline_data:
                    self.links[(name1, name2)] = SplineEdge(
                        self.spline_data[(name2, name1)]
                    )
                elif spline_data is not None:
                    self.links[(name1, name2)] = SplineEdge(spline_data)
                else:
                    raise Exception(
                        f"Spline data for edge ({name1}, {name2}) not found in self.spline_data"
                    )
            # self.add(self.links[(name1, name2)])
        return self.links[(name1, name2)]

    def add_card(self, name, pos=None, start_zoomed=False):
        if name not in self.cards:
            try:
                self.cards[name] = CardContents(
                    name, start_zoomed=start_zoomed
                ).move_to(self.card_positions[name])
            except KeyError:
                if pos is not None:
                    self.cards[name] = CardContents(
                        name, start_zoomed=start_zoomed
                    ).move_to(pos)
                else:
                    raise Exception(
                        f"Position data for card {name}, not found in self.card_positions"
                    )
            # self.add(self.cards[name])
        return self.cards[name]

    @override_animate(add_link)
    def _add_link_animate(
        self,
        name1,
        name2,
        spline_data=None,
        other_end=False,
        from_point=None,
        anim_args=None,
    ):
        if anim_args is None:
            anim_args = {}

        edge = self.add_link(name1, name2, spline_data=spline_data)

        grow_point = edge.get_start()
        if from_point is not None:
            grow_point = from_point
        elif other_end:
            grow_point = edge.get_end()
        return GrowFromPoint(edge, grow_point, **anim_args)

    @override_animate(add_card)
    def _add_card_animate(self, card, pos=None, start_zoomed=False, anim_args=None):
        if anim_args is None:
            anim_args = {}
        card = self.add_card(card, pos=pos, start_zoomed=start_zoomed)
        return GrowFromCenter(card, **anim_args)

    def add_card_from(
        self,
        from_name,
        to_add,
        pos=None,
        start_zoomed=False,
        spline_data=None,
    ):
        card = self.add_card(to_add, pos=pos, start_zoomed=start_zoomed)
        link = self.add_link(from_name, to_add, spline_data=spline_data)

        return card, link

    @override_animate(add_card_from)
    def _add_card_from(
        self,
        from_name,
        to_add,
        pos=None,
        spline_data=None,
        start_zoomed=False,
        anim_args=None,
    ):
        if anim_args is None:
            anim_args = {}
        card, link = self.add_card_from(
            from_name,
            to_add,
            pos=pos,
            spline_data=spline_data,
            start_zoomed=start_zoomed,
        )
        start = link.get_start()
        # return AnimationGroup(
        return AnimationGroup(
            GrowFromPoint(card, start, **anim_args),
            GrowFromPoint(link, start, **anim_args),
        )

    def calculate_layout(links, additional_cards=[], prev_pos=None, seed=2, esep=0.25):
        def add_node(G, name):
            if prev_pos is not None and name in prev_pos:
                G.add_node(name, pos=f"{pos[0]},{pos[1]}")
            else:
                G.add_node(name)

        G = pygraphviz.AGraph(strict=True, directed=False)
        cards = []
        for link in links:
            if link[0] not in cards:
                cards.append(link[0])
                add_node(G, link[0])
            if link[1] not in cards:
                cards.append(link[1])
                add_node(G, link[1])
            G.add_edge(link)

        for c in additional_cards:
            if c not in cards:
                cards.append(c)
                add_node(G, c)

        scale_factor = 0.01
        args = f"-Nshape=box -start={seed} -Nwidth={1.6} -Nheight={0.9} -Goverlap=false -Gesep={esep} -Gsplines=true"

        G.layout(
            prog="neato",
            args=args,
        )
        print(args)

        card_pos = {}
        for c in cards:
            node = pygraphviz.Node(G, c)
            try:
                xs = node.attr["pos"].split(",")
                # 72 points per inch according to graphviz documentation
                card_pos[c] = tuple(float(x) / 72 for x in xs) + (0.0,)

            except:
                raise Exception(f"Missing position data from GraphViz for node {c}")

        spline_data = {}
        for l in links:
            edge = pygraphviz.Edge(G, l[0], l[1])
            try:
                ps = edge.attr["pos"].split(" ")
                spline_data[l] = []
                for p in ps:
                    xs = p.split(",")
                    # 72 points per inch according to graphviz documentation
                    spline_data[l].append(tuple(float(x) / 72 for x in xs) + (0.0,))
            except:
                raise Exception(
                    f"Missing spline data from GraphViz for edge ({l[0]}, {l[1]})"
                )
        return card_pos, spline_data

    def change_layout(self, new_card_positions, new_spline_data):

        for name, card in self.cards.items():
            # try:
            if name in new_card_positions:
                card.move_to(new_card_positions[name])
            else:
                print(f"Missing position data for ({name})")
            # except KeyError:
            #     raise Exception(
            #         f"Position data for card {name}, not found in new_card_positions"
            #     )
        for (name1, name2), edge in self.links.items():
            # try:

            if (name1, name2) in new_spline_data:
                new_edge = SplineEdge(
                    new_spline_data[(name1, name2)], stroke_opacity=edge.stroke_opacity
                )
                edge.become(new_edge)
            elif (name2, name1) in new_spline_data:
                new_edge = SplineEdge(
                    new_spline_data[(name2, name1)], stroke_opacity=edge.stroke_opacity
                )
                edge.become(new_edge)
            else:
                print(f"Missing spline data for ({name1}, {name2})")
            # except KeyError:
            #     raise Exception(
            #         f"Spline data for link ({name1}, {name2}), not found in new_spline_data"
            #     )
        self.card_positions = new_card_positions
        self.spline_data = new_spline_data

    @override_animate(change_layout)
    def _animate_change_layout(
        self, new_card_positions, new_spline_data, anim_args=None
    ):
        if anim_args is None:
            anim_args = {}

        anims = []
        for name, card in self.cards.items():
            # try:
            if name in new_card_positions:
                anims.append(
                    card.animate.move_to(new_card_positions[name], **anim_args)
                )
            else:
                print(f"Missing position data for ({name})")
            # except KeyError:
            #     raise Exception(
            #         f"Position data for card {name}, not found in new_card_positions"
            #     )
        for (name1, name2), edge in self.links.items():
            # try:
            if (name1, name2) in new_spline_data:
                new_edge = SplineEdge(
                    new_spline_data[(name1, name2)],
                    stroke_opacity=edge.stroke_opacity,
                )
                anims.append(edge.animate.become(new_edge, **anim_args))
            elif (name2, name1) in new_spline_data:
                new_edge = SplineEdge(
                    new_spline_data[(name2, name1)],
                    stroke_opacity=edge.stroke_opacity,
                )
                anims.append(
                    edge.animate.become(new_edge, **anim_args),
                )
            else:
                print(f"Missing spline data for ({name1}, {name2})")
            # except KeyError:
            #     raise Exception(
            #         f"Spline data for link ({name1}, {name2}), not found in new_spline_data"
            #     )

        self.card_positions = new_card_positions
        self.spline_data = new_spline_data
        return AnimationGroup(anims)

    def remove_card(self, name):
        if name in self.cards:
            return self.cards.pop(name)
        return None

    def remove_link(self, name1, name2):
        if (name1, name2) in self.links:
            return self.links.pop((name1, name2))
        elif (name2, name1) in self.links:
            return self.links.pop((name2, name1))
        return None

    @override_animate(remove_link)
    def _animate_remove_link(self, name1, name2, anim_args=None):
        if anim_args is None:
            anim_args = {}
        removed = self.remove_link(name1, name2)
        if removed is not None:
            return AnimationGroup(
                removed.animate.move_to(self.card_positions[name1])
                .scale(0)
                .set_opacity(0)
            )
        return AnimationGroup(*[])

    def get_graph_as_group(self):
        return Group(*list(self.cards.values()), *list(self.links.values()))

    def get_cards_as_group(self, *names):
        return Group(*[self.cards[n] for n in names])

    def get_graph_as_list(self):
        return list(self.cards.values()) + list(self.links.values())

    def update_card_icons(self, frame_width):
        for c in self.cards.values():
            if frame_width <= 1.6:
                c.show_img(c.get_current_slide())
            else:
                c.show_img(c.get_current_icon())

    @override_animate(update_card_icons)
    def _animate_update_card_icons(self, frame_width, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anims = []

        for c in self.cards.values():
            if frame_width <= 1.6:
                anims.append(c.animate.show_img(c.get_current_slide()))
            else:
                anims.append(c.animate.show_img(c.get_current_icon()))

        if len(anims) == 0:
            return self.animate.scale(1)
        return AnimationGroup(*anims)


MODERN_DAY_CARDS = ["Jen", "Eric", "Moody", "Ilsa", "Desjardins", "Serin", "Caldeira"]
