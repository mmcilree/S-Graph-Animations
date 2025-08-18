from manim import *
from graph import *


class Section2(CardGraphScene):
    def sequence1(self):
        # Create and zoom fully on Jen
        self.camera.frame.move_to(self.current_pos("Jen")).scale_to_fit_width(4)
        self.wait_until(2, 12, 660)
        self.play(self.add_card("Jen"))
        self.play(self.fully_zoom_card("Jen"))

        self.wait_until(2, 20, 520)

        # Create "Thomas"=Eric, link to Jen, zoom fully on "Thomas"
        self.play(self.frame_cards("Jen", "Eric"))
        self.play(self.add_link("Jen", "Eric"), self.add_card("Eric"))
        self.play(self.fully_zoom_card("Eric"))
        self.wait_until(2, 23, 80)
        self.play(self.change_slide("Eric", "1.2"))

        self.wait_until(2, 30, 00)

        # Create Moody (emerge/pan from “Thomas”, staying zoomed in)
        self.play(
            self.add_card_from("Eric", "Moody", start_zoomed=True),
            self.fully_zoom_card("Moody"),
            run_time=1.5,
        )
        self.wait_until(2, 48, 960)

        # Show Jen and “Thomas”
        self.play(self.frame_cards("Jen", "Eric"))

        self.wait_until(2, 52, 960)
        # Put red X over Thomas card
        self.play(self.cross_card("Eric"))

        # Make Jen-”Thomas” connection disappear then reappear (for 5 secs eg)
        self.play(self.g.links[("Jen", "Eric")].animate.set_opacity(0))

        self.wait_until(2, 55, 500)
        # Zoom fully in on “Thomas” card
        self.play(
            self.fully_zoom_card("Eric"),
            self.uncross_card("Eric"),
            self.g.links[("Jen", "Eric")].animate.set_opacity(1),
        )

        self.play(self.change_slide("Eric", "2.1"))
        self.set_icon("Eric", "2.0")

        self.wait_until(3, 14, 520)
        self.play(self.change_slide("Eric", "2.2"))

        self.wait_until(3, 22, 720)
        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric"))

        # Create VMS card, pan over to (not fully zoomed)
        self.play(self.frame_cards("Jen", "Eric", "VMS"))
        self.play(
            self.frame_cards("VMS", "Caldeira"),
            self.add_card("VMS"),
        )

        self.wait_until(3, 37, 560)
        # Create Caldeira and link to VMS
        self.play(
            self.add_card_from("VMS", "Caldeira"),
        )
        # Zoom fully on Caldeira
        self.play(self.fully_zoom_card("Caldeira"))
        self.wait_until(3, 53, 600)

        self.play(self.change_slide("Caldeira", "1.2"))
        self.wait_until(4, 28, 320)
        self.play(self.change_slide("Caldeira", "1.3"))

        # Zoom fully on VMS
        self.wait_until(4, 33, 700)
        self.play(self.fully_zoom_card("VMS"))
        self.wait_until(4, 41, 120)
        self.play(self.change_slide("VMS", "1.2"))
        self.wait_until(5, 25, 920)
        self.play(self.change_slide("VMS", "1.3"))

        self.wait_until(5, 44, 740)
        # Create Havana_incident (but don’t zoom), link to Caldeira and VMS
        self.play(self.frame_cards("VMS", "Caldeira", "Havana"))

        self.wait_until(5, 48, 0)
        self.play(
            self.add_card("Havana"),
            self.add_link("VMS", "Havana"),
            self.add_link("Caldeira", "Havana"),
        )

        self.wait_until(6, 30, 860)
        self.play(self.zoom_card("Havana"))
        self.wait_until(7, 4, 100)
        self.play(self.change_slide("Havana", "1.2"))
        self.wait_until(7, 7, 300)

        # Show all so far
        self.play(
            self.frame_cards(
                "VMS",
                "Caldeira",
                "Jen",
                "Eric",
            )
        )

        self.wait_until(7, 17, 540)

        # Highlight or pan between Jen, Eric, Caldeira and VMS
        self.play(self.circle_card("Jen"), run_time=0.5)
        self.play(self.circle_card("Eric"), run_time=0.5)
        self.play(self.circle_card("Caldeira"), run_time=0.5)
        self.play(self.circle_card("VMS"), run_time=0.5)
        self.wait(1)
        self.play(self.clear_circles())
        self.wait_until(7, 46, 900)
        # Zoom on Caldeira
        self.play(self.fully_zoom_card("Caldeira"))

        self.wait_until(7, 54, 560)

        self.set_icon("Caldeira", "2.0")
        self.play(self.change_slide("Caldeira", "2.1"))

        self.wait_until(8, 0, 480)
        self.play(self.change_slide("Caldeira", "2.2"))

        self.wait_until(8, 31, 620)
        self.play(self.change_slide("Caldeira", "2.3"))

        self.wait_until(8, 58, 100)
        self.play(self.change_slide("Caldeira", "2.4"))

        self.wait_until(9, 3, 100)
        # Reshuffle layout for all the new cards incoming
        self.play(
            self.frame_cards("VMS", "Caldeira", "Havana", "Jen", "Eric", "Moody"),
            run_time=3,
        )

    def sequence2(self):

        self.play(self.animate_update_layout(), run_time=3.5)

        self.wait_until(9, 10, 160)
        # Zoom out then partly zoom on VMS
        self.play(self.frame_cards("VMS", "Prix"))

        # Create Prix Bouchard card (emerge from VMS) and zoom in on
        self.play(self.add_card_from("VMS", "Prix"))
        self.play(self.fully_zoom_card("Prix"))

        self.wait_until(9, 35, 200)
        # Create Lewis Looper card (emerge from VMS)
        self.play(self.frame_cards("VMS", "Looper", "Prix"))
        self.play(self.add_card_from("VMS", "Looper"))

        self.wait_until(9, 55, 0)
        # Create Artefacts (partially zoom on but not fully) and link to VMS and Looper
        self.play(self.frame_cards("VMS", "Looper", "Artefacts"))
        self.play(
            self.add_card("Artefacts"),
            self.add_link("Looper", "Artefacts"),
            self.add_link("VMS", "Artefacts"),
        )

        self.wait_until(10, 3, 0)
        # Create Sobreiro (emerge from artefacts) and fully zoom in on
        self.play(
            LaggedStart(
                self.frame_cards("Artefacts", "Sobreiro"),
                self.add_card_from("Artefacts", "Sobreiro"),
                lag_ratio=0.5,
            )
        )
        # Create Sobreiro (emerge from artefacts) and fully zoom in on
        self.play(self.fully_zoom_card("Sobreiro"))

        self.wait_until(10, 18, 700)
        # Pan (still zoomed) to Artefacts
        self.play(self.fully_zoom_card("Artefacts"))

        self.wait_until(10, 25, 620)

        # Zoom out, create Santorini_deaths, fully zoom in on
        self.play(
            self.frame_cards("VMS", "Prix", "Sant_Deaths"),
            self.add_card("Sant_Deaths"),
        )
        self.play(self.fully_zoom_card("Sant_Deaths"))

        self.wait_until(10, 53, 0)

        # Zoom fully on Jen
        self.play(self.frame_cards())
        self.play(self.fully_zoom_card("Jen"))
        self.wait_until(10, 58, 0)

        self.play(self.change_slide("Jen", "1.2"))

        self.wait_until(11, 8, 280)

        self.play(self.change_slide("Jen", "1.3"))

        self.wait_until(11, 24, 600)

        # Zoom fully on Eric
        self.play(self.fully_zoom_card("Eric"))
        self.play(self.change_slide("Eric", "2.2"))

        self.wait_until(11, 47, 240)

        self.play(self.change_slide("Eric", "2.3"))

        self.wait_until(11, 53, 380)

        # Create Ilsa (emerge/pan from Eric), link with Moody and Jen but don’t show
        self.play(
            self.add_card_from("Eric", "Ilsa"),
            self.frame_cards("Eric", "Ilsa"),
        )
        # Zoom fully Ilsa, link with Moody and Jen but don’t zoom out
        self.play(
            self.fully_zoom_card("Ilsa"),
            self.add_link("Ilsa", "Jen"),
            self.add_link("Moody", "Ilsa"),
        )
        self.wait_until(12, 8, 380)

        # Zoom on Jen and Eric, highlight link
        self.play(
            self.frame_cards("Jen", "Eric"),
            self.highlight_link("Jen", "Eric", color=BLUE_E),
        )

        self.wait_until(12, 58, 500)

        # Create Sum_tape (linked to Eric and VMS), fully zoom in on
        self.play(
            self.unhighlight_link("Jen", "Eric"),
            self.frame_cards("Jen", "Eric", "Sum_Tape", "VMS"),
        )

        self.play(
            self.add_link("Eric", "Sum_Tape"),
            self.add_link("VMS", "Sum_Tape"),
            self.add_card("Sum_Tape"),
            self.fully_zoom_card("Sum_Tape"),
        )
        self.wait(1)

        self.wait_until(13, 18, 0)

        # Link Moody and Ilsa to Sum_tape
        self.play(self.frame_cards("Sum_Tape", "Moody", "Sum_Tape"))

        self.play(
            self.add_link("Moody", "Sum_Tape"),
            self.add_link("Ilsa", "Sum_Tape"),
        )

        self.set_slide("Sum_Tape", "1.2")
        self.wait_until(13, 30, 920)
        # Zoom fully on Sum_tape
        self.play(self.fully_zoom_card("Sum_Tape"))

        self.wait_until(13, 43, 0)
        # Zoom out slowly then show Jen/Eric/Moody/Ilsa
        self.play(self.frame_cards("Jen", "Eric", "Moody", "Ilsa"), run_time=4)

        self.wait_until(13, 52, 0)

        # Highlight Jen and Ilsa link
        self.play(self.highlight_link("Ilsa", "Jen"))

        self.wait_until(13, 59, 400)
        # Link Ilsa and Moody to Artefacts
        self.play(
            self.unhighlight_link("Ilsa", "Jen"),
            self.frame_cards("Moody", "Ilsa", "Artefacts"),
        )
        self.wait_until(14, 2, 400)
        self.play(
            self.add_link("Moody", "Artefacts"),
            self.add_link("Ilsa", "Artefacts"),
        )

        self.wait_until(14, 37, 80)

        # Create Mysterious_men and fully zoom in on
        self.play(
            self.frame_cards("Jen", "Eric", "Myst_Men"),
            self.add_card("Myst_Men"),
        )
        self.play(self.fully_zoom_card("Myst_Men"))

        self.wait_until(14, 47, 600)

        # Create Serin (linked to Eric), zoom on a little but not fully
        self.play(self.frame_cards("Serin", "Eric"))
        self.play(self.add_card("Serin"), self.add_link("Eric", "Serin"))
        self.wait_until(14, 55, 0)
        self.play(self.fully_zoom_card("Serin"))
        self.wait_until(15, 23, 880)

        self.play(self.frame_cards("Jen", "Eric", "Ilsa", "Moody"))

        self.wait_until(15, 31, 80)
        # Zoom (not fully) to Moody
        self.set_slide("Moody", "1.2")
        self.play(
            self.frame_cards("Moody", margin=2.5),
        )

        self.wait_until(15, 36, 600)

        # Vanish Sum_tape and Straka connection
        self.play(self.frame_cards("Sum_Tape", "VMS"))
        self.play(self.g.links["VMS", "Sum_Tape"].animate.set_opacity(0))

        self.wait_until(15, 44, 700)

        # Pan to Caldeira (not fully zoomed)
        self.play(self.pan_to("Caldeira"))

        self.wait_until(15, 56, 320)

        # Zoom fully on Artefacts
        self.play(
            self.fully_zoom_card("Artefacts"), self.change_slide("Artefacts", "1.3")
        )

        self.wait_until(16, 0, 840)

        self.change_slide("Jen", "1.5")
        # Zoom out and pan to Jen
        self.play(self.frame_cards("Jen", margin=2))
        self.play(self.fully_zoom_card("Jen"))

        self.wait_until(16, 22, 920)

        # Pan to Moody, then Sum_tape, then Artefacts
        self.play(self.frame_cards("Moody", margin=3))
        self.wait(0.5)
        self.play(self.pan_to("Sum_Tape"))
        self.wait(0.2)
        self.play(self.pan_to("Artefacts"))
        self.wait(0.5)

        self.wait_until(16, 32, 920)

        # Pan to Eric, add golden outline or green tick over card
        self.play(self.pan_to("Eric"))
        self.play(
            Circumscribe(self.g.cards["Eric"], color=YELLOW_D, stroke_width=8),
            run_time=1.5,
        )

        self.wait_until(16, 44, 560)

        # Pan to Ilsa
        self.play(self.pan_to("Ilsa"))
        self.wait_until(16, 48, 0)

        # Pan to Mysterious_men
        self.play(self.pan_to("Myst_Men"))

    def sequence3(self):
        self.wait_until(16, 52, 320)

        # Create Dejardins and link to Eric, fully zoom in on
        self.play(self.frame_cards(*MODERN_DAY_CARDS))
        self.play(self.animate_update_layout())

        self.wait_until(16, 52, 320)
        self.play(self.frame_cards("Eric", "Desjardins", "Moody"))
        self.play(self.add_card("Desjardins"), self.add_link("Eric", "Desjardins"))
        self.play(self.fully_zoom_card("Desjardins"))

        self.wait_until(17, 9, 880)
        # Zoom out halfway and link Dejardins to Moody
        self.play(self.frame_cards("Eric", "Desjardins", "Moody"))
        self.play(self.add_link("Desjardins", "Moody"))

        self.wait_until(17, 19, 680)

        # Pan to Serin
        self.play(self.pan_to("Serin"), run_time=3)

        self.wait_until(17, 25, 800)

        # Link Desjardins and Eric to Artefacts
        self.play(self.frame_cards("Desjardins", "Eric", "Artefacts"))
        self.play(
            self.add_link("Desjardins", "Artefacts"), self.add_link("Eric", "Artefacts")
        )

        self.wait_until(17, 47, 360)

        # Zoom fully on Desjardins
        self.play(self.fully_zoom_card("Desjardins"))
        self.play(self.change_slide("Desjardins", "1.2"))
        self.wait_until(17, 55, 560)

        # Zoom fully/pan to Serin
        self.play(self.fully_zoom_card("Serin"))

        self.wait_until(18, 24, 80)

        # Zoom out, pan to Ilsa
        self.play(self.frame_cards("Ilsa", margin=3))

        self.wait_until(18, 53, 640)
        # Zoom fully on Caldeira
        # Bonus - link Eric and Caldeira
        self.play(self.frame_cards("Eric", "Caldeira"))

    def sequence4(self):
        self.wait_until(18, 55, 0)

        self.play(self.animate_update_layout())
        self.play(
            self.frame_cards("Eric", "Caldeira"),
            self.add_link("Eric", "Caldeira", other_end=True),
            run_time=2,
        )
        self.set_slide("Caldeira", "2.5")

        self.wait_until(18, 56, 880)
        self.play(self.fully_zoom_card("Caldeira"))
        self.play(self.change_slide("Caldeira", "3.1"))
        self.set_icon("Caldeira", "3.0")

        self.wait_until(19, 16, 0)
        self.play(self.change_slide("Caldeira", "3.2"))

        self.wait_until(19, 24, 40)
        self.play(self.change_slide("Caldeira", "3.3"))

        self.wait_until(19, 25, 680)
        # Show Jen/Eric/Caldeira/VMS, highlight all
        self.play(self.frame_cards("Jen", "Eric", "Caldeira", "VMS"))

        self.play(
            self.opacity_except(
                "Jen",
                "Eric",
                "VMS",
                "Caldeira",
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")],
            ),
            self.highlight_link("Jen", "Eric", color=BLUE_E),
            self.highlight_link("VMS", "Caldeira", color=PURE_RED),
        )

        # Zoom fully on Eric
        self.play(
            self.opacity_except(
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")], opacity=1
            ),
            self.unhighlight_link("Jen", "Eric"),
            self.unhighlight_link("VMS", "Caldeira"),
        )

        self.set_slide("Eric", "2.4")
        self.wait_until(19, 35, 360)
        self.play(self.fully_zoom_card("Eric"))

        self.wait_until(20, 8, 829)
        self.play(self.change_slide("Eric", "2.5"))

        self.wait_until(20, 14, 780)
        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric"))

        self.wait_until(20, 35, 0)
        self.play(self.frame_cards("Jen", "Eric", "Caldeira", "VMS"))

        self.wait_until(20, 41, 0)
        # Zoom fully on Mysterious_men
        self.play(self.fully_zoom_card("Myst_Men"))
        self.set_slide("Sant_Deaths", "1.2")
        self.wait_until(21, 1, 460)
        self.play(self.frame_cards("Sant_Deaths", margin=4))
        self.play(self.fully_zoom_card("Sant_Deaths"), run_time=2)

        self.wait_until(21, 9, 980)
        self.play(self.pan_to("Myst_Men"), margin=4)
        self.set_slide("Myst_Men", "1.2")
        self.play(self.fully_zoom_card("Myst_Men"))

        self.set_slide("Jen", "1.6")
        self.wait_until(22, 54, 140)
        # Zoom fully on Jen
        self.play(self.fully_zoom_card("Jen"))

        self.wait_until(22, 56, 740)
        self.play(self.change_slide("Jen", "1.7"))

        self.wait_until(23, 19, 80)
        self.play(self.change_slide("Jen", "1.8"))

        self.wait_until(23, 23, 40)
        # Highlight/circle Jen/Eric and VMS/Caldeira
        self.play(
            self.frame_cards("Jen", "Eric", "VMS", "Caldeira"),
        )
        self.play(
            self.opacity_except(
                "Jen",
                "Eric",
                "VMS",
                "Caldeira",
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")],
            ),
            run_time=2,
        )
        self.wait(5)
        self.play(
            self.opacity_except(
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")], opacity=1
            ),
        )
        self.wait_until(23, 57, 80)

        # Link Jen and Moody
        self.play(self.frame_cards("Jen", "Moody"))

        self.play(
            self.add_link("Jen", "Moody"),
            self.g.cards["Moody"].animate.scale(1),
            self.g.cards["Jen"].animate.scale(1),
        )

        self.wait_until(24, 10, 480)

        # Pan to Artefacts
        self.play(self.frame_cards("Artefacts", margin=2))

    def sequence5(self):
        self.wait_until(24, 18, 0)

        # Show Moody, Artefacts, Sum_tape and Sobreiro
        self.play(
            self.frame_cards("Moody", "Artefacts", "Sum_Tape", "Sobreiro"),
        )
        self.play(
            self.opacity_except("Moody", "Artefacts", "Sum_Tape", "Sobreiro"),
        )

        # Highlight Artefacts, cross over Tape and Sobreiro
        self.play(
            self.highlight_card("Artefacts"),
        )
        self.play(self.cross_card("Sum_Tape"), self.cross_card("Sobreiro"))

        self.wait_until(24, 55, 560)
        # Pan to Eric
        self.play(
            self.unhighlight_card("Artefacts"),
            self.uncross_card("Sum_Tape"),
            self.uncross_card("Sobreiro"),
            self.opacity_except(
                "Moody", "Artefacts", "Sum_Tape", "Sobreiro", opacity=1
            ),
            self.frame_cards("Eric", margin=2.5),
        )

        self.wait_until(25, 1, 600)

        # Link Mysterious_men and Jen
        self.play(self.frame_cards("Myst_Men", "Jen", "Eric"))
        self.play(
            self.add_link("Myst_Men", "Jen"),
            self.g.cards["Myst_Men"].animate.scale(1),
            self.g.cards["Jen"].animate.scale(1),
        )
        self.wait(0.5)

        # Link Mysterious_men and Eric briefly then vanish
        self.play(
            self.add_link("Myst_Men", "Eric"),
            self.g.cards["Myst_Men"].animate.scale(1),
            self.g.cards["Eric"].animate.scale(1),
        )

        self.wait(0.5)
        self.play(self.g.links[("Myst_Men", "Eric")].animate.set_stroke(opacity=0))
        self.wait(1)

        self.set_slide("Myst_Men", "1.3")
        # Zoom fully on Mysterious_men
        self.play(self.fully_zoom_card("Myst_Men"))
        self.wait(1)

        self.set_slide("Ilsa", "1.3")
        self.set_slide("Eric", "2.6")
        self.wait_until(27, 47, 100)
        # Zoom fully on Ilsa
        self.play(self.fully_zoom_card("Ilsa"))

        self.wait_until(27, 58, 300)

        # Zoom fully/pan to Eric
        self.play(self.fully_zoom_card("Eric"))
        self.wait_until(28, 4, 0)

        self.play(self.change_slide("Eric", "2.7"))

        self.wait_until(28, 16, 460)

        # Show Eric and Ilsa and highlight link in green
        self.play(
            LaggedStart(
                self.frame_cards("Eric", "Ilsa", "Moody"),
                self.highlight_link("Eric", "Ilsa", color=GREEN_E),
                lag_ratio=0.5,
            ),
            self.g.cards["Ilsa"].animate.scale(1),
        )

        # Highlight Moody/Eric link in red
        self.play(self.highlight_link("Eric", "Moody", color=PURE_RED))

        self.set_slide("Moody", "1.3")
        self.wait_until(28, 21, 900)
        self.play(self.fully_zoom_card("Moody"))

        self.wait_until(28, 34, 700)
        self.set_slide("Sum_Tape", "1.3")
        # Zoom fully on Sum_tape
        self.play(
            self.unhighlight_link("Eric", "Moody"),
            self.unhighlight_link("Eric", "Ilsa"),
            self.frame_cards("Sum_Tape", margin=3),
        )
        self.wait_until(28, 40, 0)

        self.fully_zoom_card("Sum_Tape"),

        self.wait_until(29, 1, 740)
        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric"))

        self.wait_until(29, 4, 660)
        # Pan to VMS
        self.play(self.pan_to("VMS"))

        self.wait_until(29, 11, 140)
        self.set_slide("Serin", "1.3")
        # Pan to Serin
        self.play(self.pan_to("Serin"))
        self.play(self.fully_zoom_card("Serin"))

        self.wait_until(29, 42, 900)
        self.play(self.fully_zoom_card("Jen"))
        self.play(self.change_slide("Jen", "1.9"))

        self.wait_until(29, 58, 940)
        self.play(self.fully_zoom_card("Caldeira"))
        self.wait_until(30, 3, 00)

        self.play(self.change_slide("Caldeira", "3.4"))

        self.wait_until(30, 25, 560)
        self.play(
            self.frame_cards("Eric", "Moody"), self.highlight_link("Eric", "Moody")
        )

        self.wait_until(30, 52, 0)
        self.play(
            self.frame_cards("Artefacts", margin=2),
            self.unhighlight_link("Eric", "Moody"),
            self.highlight_card("Artefacts"),
        )

        self.wait_until(30, 56, 0)
        self.play(self.fully_zoom_card("Jen"))
        self.play(self.change_slide("Jen", "1.9"))

        self.wait_until(32, 30, 0)
        self.play(
            self.frame_cards("Jen", "Eric", "Myst_Men"),
            self.unhighlight_link("Eric", "Moody"),
            self.circle_card("Myst_Men"),
        )

        self.wait_until(32, 41, 160)
        self.play(self.frame_cards("VMS", margin=5), run_time=10)
        self.play(self.frame_cards("VMS", margin=2), run_time=6)

    def construct(self):
        self.next_section(skip_animations=True)
        self.start_HERE()
        # Initial set up
        self.prepare_link("Jen", "Eric")
        self.prepare_link("Eric", "Moody")
        self.prepare_link("Jen", "Ilsa")
        self.prepare_link("Eric", "Ilsa")
        self.prepare_link("Moody", "Ilsa")

        self.prepare_link("VMS", "Caldeira")
        self.prepare_link("VMS", "Havana")
        self.prepare_link("Caldeira", "Havana")

        # Temporary to keep layout compact
        self.prepare_link("Eric", "Caldeira", not_added=True)
        self.prepare_link("Eric", "VMS", not_added=True)
        self.prepare_link("Jen", "VMS", not_added=True)
        self.prepare_link("Jen", "Caldeira", not_added=True)

        self.calculate_layout()
        self.update_layout()

        self.sequence1()

        self.remove_link("Eric", "Caldeira")
        self.remove_link("Eric", "VMS")
        self.remove_link("Jen", "VMS")
        self.remove_link("Jen", "Caldeira")

        self.prepare_link("VMS", "Prix")
        self.prepare_link("VMS", "Looper")
        self.prepare_link("VMS", "Artefacts")
        self.prepare_link("Looper", "Artefacts")
        self.prepare_link("Sobreiro", "Artefacts")
        self.prepare_card("Sant_Deaths")

        self.prepare_link("Eric", "Sum_Tape")
        self.prepare_link("VMS", "Sum_Tape")
        self.prepare_link("Moody", "Sum_Tape")
        self.prepare_link("Ilsa", "Sum_Tape")
        self.prepare_link("Moody", "Artefacts")
        self.prepare_link("Ilsa", "Artefacts")
        self.prepare_link("Myst_Men", "Jen")
        self.prepare_link("Myst_Men", "Eric")
        self.prepare_link("Eric", "Serin")

        self.calculate_layout(prev=False)

        self.sequence2()

        self.prepare_link("Eric", "Desjardins")
        self.prepare_link("Desjardins", "Moody")
        self.prepare_link("Desjardins", "Artefacts")
        self.prepare_link("Eric", "Artefacts")

        self.calculate_layout()

        self.sequence3()

        self.prepare_link("Caldeira", "Eric")
        self.prepare_link("Jen", "Moody")

        self.calculate_layout()

        self.sequence4()
        self.sequence5()
