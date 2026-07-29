import manim as mm
import numpy as np
from typing import cast
from graph import CardGraph, LINK_WIDTH, LINK_COLOR


class NullAnim(mm.Animation):
    def __init__(
        self,
        mobject,
        **kwargs,
    ):
        super().__init__(
            mobject,
            **kwargs,
        )


NULL_ANIM = NullAnim(mm.Dot())


class CardGraphScene(mm.MovingCameraScene):
    camera: mm.MovingCamera

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.camera.background_color = "#F1E9D2"
        self.nodes = []
        self.edges = []
        self.not_added = []
        self.layouts = []
        self.ovals = []
        self.crosses = {}
        self.g = CardGraph()
        self.skip_animations = True
        self.time_s = 0

    def prepare_card(self, name):
        if name not in self.nodes:
            self.nodes.append(name)

    def prepare_link(self, name1, name2, not_added=False):
        self.prepare_card(name1)
        self.prepare_card(name2)
        if (name1, name2) not in self.edges:
            self.edges.append((name1, name2))

        # For skipping animations
        if not_added:
            self.not_added.append((name1, name2))

    def remove_card(self, name):
        if name in self.nodes:
            self.nodes.remove(name)
            # Remove all edges connected to this node
            self.edges = [e for e in self.edges if name not in e]
        return self.g.remove_card(name)

    def unprepare_link(self, name1, name2):
        if (name1, name2) in self.edges:
            self.edges.remove((name1, name2))
        elif (name2, name1) in self.edges:
            self.edges.remove((name2, name1))

    def add_card(self, name, start_zoomed=False):
        if self.skip_animations:
            self.g.add_card(name, start_zoomed=start_zoomed)
            self.add(self.g.cards[name])
            return NULL_ANIM
        return self.g.animate.add_card(name, start_zoomed=start_zoomed)

    def add_card_from(self, name1, name2, start_zoomed=False):
        if self.skip_animations:
            self.add_card(name2)
            self.add_link(name1, name2)
            return NULL_ANIM
        return self.g.animate.add_card_from(name1, name2, start_zoomed=start_zoomed)

    def add_link(
        self,
        name1,
        name2,
        other_end=False,
        from_point=None,
        color=LINK_COLOR,
        width=LINK_WIDTH,
    ):
        if self.skip_animations:
            self.g.add_link(name1, name2)
            self.add(self.g.links[name1, name2])
            return NULL_ANIM

        return self.g.animate.add_link(
            name1, name2, other_end=other_end, from_point=from_point, color=color, width=width  # type: ignore[attr-defined]
        )

    def remove_link(self, name1, name2):
        self.unprepare_link(name1, name2)
        if (name1, name2) in self.g.links:
            self.remove(self.g.links[name1, name2])
        elif (name2, name1) in self.g.links:
            self.remove(self.g.links[name2, name1])

        if self.skip_animations:
            link = self.g.remove_link(name1, name2)
            self.remove(link)
            return NULL_ANIM
        ret = self.g.animate.remove_link(
            name1,
            name2,
            to_point=mm.midpoint(
                self.layouts[-1][0][name1], self.layouts[-1][0][name2]
            ),
        )

        return ret

    def calculate_layout(
        self,
        seed=2,
        prev=True,
        esep=0.25,
    ):

        prev_pos = self.layouts[-1] if len(self.layouts) > 0 and prev else None

        self.layouts.append(
            CardGraph.calculate_layout(
                self.edges,
                additional_cards=self.nodes,
                esep=esep,
                seed=seed,
                prev_pos=prev_pos,
            )
        )

    def update_layout(self):
        self.g.change_layout(*self.layouts[-1])

    def animate_update_layout(self):
        if self.skip_animations:
            self.g.change_layout(*self.layouts[-1])
            return NULL_ANIM
        return self.g.animate.change_layout(*self.layouts[-1])

    def current_pos(self, name):
        return self.layouts[-1][0][name]

    def bounding_box(self, *names):
        if len(names) == 0:
            names = self.nodes
        points = []
        for n in names:
            points.append(self.layouts[-1][0][n])

        arr = np.array(points)
        # Adjust for the fact that these are the center points of boxes of size 1.6 x 0.9
        half_width = 1.6 / 2
        half_height = 0.9 / 2
        min_x = (arr[:, 0] - half_width).min()
        max_x = (arr[:, 0] + half_width).max()
        min_y = (arr[:, 1] - half_height).min()
        max_y = (arr[:, 1] + half_height).max()
        width = max_x - min_x
        height = max_y - min_y
        center = np.array([(min_x + max_x) / 2, (min_y + max_y) / 2, 0])
        rect = mm.Rectangle(width=width, height=height).move_to(center)
        return rect

    def fully_zoom_card(self, name):
        if self.skip_animations:
            return NULL_ANIM

        move_camera = cast(
            mm.Animation,
            self.camera.frame.animate.scale_to_fit_width(1.58).move_to(
                self.current_pos(name)
            ),
        )

        update_icons = cast(
            mm.Animation,
            self.g.animate.update_card_icons(1.58),
        )
        return mm.AnimationGroup(move_camera, update_icons)

    def zoom_card(self, name, width=2):
        if self.skip_animations:
            return NULL_ANIM
        card = self.g.cards[name]
        move_camera = cast(
            mm.Animation,
            self.camera.frame.animate.scale_to_fit_width(width).move_to(
                card.get_center()
            ),
        )
        update_icons = cast(mm.Animation, self.g.animate.update_card_icons(1.58))

        return mm.AnimationGroup(move_camera, update_icons)

    def circle_card(self, name):
        if self.skip_animations:
            card = self.g.cards[name]
            oval = mm.DashedVMobject(
                mm.Ellipse(
                    width=card.width + 0.2,
                    height=card.height + 0.2,
                    color=mm.PURE_RED,
                    stroke_width=LINK_WIDTH,
                    z_index=1,
                )
            ).move_to(card.get_center())
            oval.set_z_index(20)
            self.ovals.append(oval)
            return NULL_ANIM

        card = self.g.cards[name]
        oval = mm.DashedVMobject(
            mm.Ellipse(
                width=card.width + 0.2,
                height=card.height + 0.2,
                color=mm.PURE_RED,
                stroke_width=LINK_WIDTH,
                z_index=1,
            )
        ).move_to(card.get_center())

        oval.set_z_index(20)
        self.ovals.append(oval)
        return mm.Create(oval)

    def clear_circles(self):
        if self.skip_animations:
            while len(self.ovals) > 0:
                o = self.ovals.pop()
                self.remove(o)
            return NULL_ANIM
        anims = []
        while len(self.ovals) > 0:
            o = self.ovals.pop()
            anims.append(mm.FadeOut(o))
        return mm.AnimationGroup(*anims)

    def frame_cards(self, *cards, margin=0.5, no_update=False, shift=None):
        if self.skip_animations:
            return NULL_ANIM
        box = self.bounding_box(*cards)

        if shift is not None:
            box.shift(shift)

        zoom_camera = cast(mm.Animation, self.camera.auto_zoom([box], margin=margin))
        update_icons = (
            [NULL_ANIM]
            if no_update
            else [
                cast(
                    mm.Animation,
                    self.g.animate.update_card_icons(
                        box.width + margin,
                    ),
                )
            ]
        )
        return mm.AnimationGroup(zoom_camera, *update_icons)

    def highlight_link(self, name1, name2, color=mm.PURE_RED, width=12):
        if self.skip_animations:
            return NULL_ANIM

        if (name1, name2) not in self.g.links:
            return (
                self.g.links[(name2, name1)]
                .animate.set_stroke_width(width)
                .set_color(color)
            )
        else:
            return (
                self.g.links[(name1, name2)]
                .animate.set_stroke_width(width)
                .set_color(color)
            )

    def unhighlight_link(self, name1, name2):
        if self.skip_animations:
            return NULL_ANIM
        if (name1, name2) not in self.g.links:
            return (
                self.g.links[(name2, name1)]
                .animate.set_stroke_width(LINK_WIDTH)
                .set_color(LINK_COLOR)
            )
        else:
            return (
                self.g.links[(name1, name2)]
                .animate.set_stroke_width(LINK_WIDTH)
                .set_color(LINK_COLOR),
            )

    def highlight_card(self, name, color=mm.PURE_RED, width=12):
        if self.skip_animations:
            return NULL_ANIM
        return self.g.cards[name].rect.animate.set_stroke(width=width, color=color)

    def unhighlight_card(self, name):
        if self.skip_animations:
            return NULL_ANIM
        return self.g.cards[name].rect.animate.set_stroke(
            width=LINK_WIDTH, color=LINK_COLOR
        )

    def cross_card(self, name):
        if self.skip_animations:
            return NULL_ANIM

        self.crosses[name] = (
            mm.Text(
                "×",
                color=mm.PURE_RED,
                font="Helvetica",
                font_size=200,
                z_index=1,
            )
            .set_opacity(0.5)
            .move_to(self.current_pos(name))
            .scale_to_fit_width(self.g.cards[name].width)
        )

        self.add(self.crosses[name])
        return mm.GrowFromCenter(self.crosses[name])

    def uncross_card(self, name):
        if self.skip_animations:
            return NULL_ANIM

        return self.crosses[name].animate.set_opacity(0)

    def pan_to(self, name):
        if self.skip_animations:
            return NULL_ANIM
        return self.camera.frame.animate.move_to(self.current_pos(name))

    def opacity_except(self, *names, edges=None, opacity=0.2):

        anims = []
        if self.skip_animations:
            if edges is None:
                anims += [
                    l.set_stroke(opacity=opacity)
                    for (n, l) in self.g.links.items()
                    if n[0] not in names or n[1] not in names
                ]
            else:
                anims += [
                    l.set_stroke(opacity=opacity)
                    for (n, l) in self.g.links.items()
                    if n not in edges
                ]

            anims += [
                c.set_opacity(opacity)
                for (n, c) in self.g.cards.items()
                if n not in names
            ]
            return NULL_ANIM

        if edges is None:
            anims += [
                l.animate.set_stroke(opacity=opacity)
                for (n, l) in self.g.links.items()
                if n[0] not in names or n[1] not in names
            ]
        else:
            anims += [
                l.animate.set_stroke(opacity=opacity)
                for (n, l) in self.g.links.items()
                if n not in edges
            ]

        anims += [
            c.animate.set_opacity(opacity)
            for (n, c) in self.g.cards.items()
            if n not in names
        ]

        return mm.AnimationGroup(*anims)

    def starth(self):
        self.skip_animations = False
        self.next_section(skip_animations=False)

    def endh(self):
        self.skip_animations = True
        self.next_section(skip_animations=True)

    def change_slide(self, name, key):
        if self.skip_animations:
            self.set_slide(name, key)
            return NULL_ANIM
        self.g.cards[name].current_slide = key
        return self.g.cards[name].animate.show_img(key, lag_ratio=0.3)

    def set_slide(self, name, key):
        self.g.cards[name].current_slide = key

    def set_icon(self, name, key):
        self.g.cards[name].current_icon = key

    def wait_until(self, min, sec, cent):
        if self.skip_animations:
            return

        until_sec = min * 60 + sec + 0.001 * cent
        if until_sec > self.time:
            wait_time = until_sec - self.time
            self.play(mm.Wait(frozen_frame=True), run_time=wait_time)
        else:
            print(f"No time to wait! ({min}:{sec}.{cent})")

    def play(self, *args, run_time=1.5, **kwargs):
        # self.time += run_time
        for a in args:
            if isinstance(a, NullAnim):
                return

        super().play(*args, run_time=run_time, **kwargs)

    def wait(self, duration, *args, **kwargs):
        # self.time += duration
        super().wait(duration, *args, **kwargs)
