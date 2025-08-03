from manim import *
from graph import *


class Section2(CardGraphScene):
    def sequence1(self):
        # Create and zoom fully on Jen
        self.camera.frame.move_to(self.current_pos("Jen")).scale_to_fit_width(4)

        self.play(self.add_card("Jen"))
        self.play(self.fully_zoom_card("Jen"))
        self.wait(1)

        # Create "Thomas"=Eric, link to Jen, zoom fully on "Thomas"
        self.play(self.frame_cards("Jen", "Eric"))
        self.play(self.add_link("Jen", "Eric"), self.add_card("Eric"))
        self.play(self.fully_zoom_card("Eric"))
        self.wait(1)

        # Create Moody (emerge/pan from “Thomas”, staying zoomed in)
        self.play(
            self.add_card_from("Eric", "Moody"),
            self.fully_zoom_card("Moody"),
        )
        self.wait(1)

        # Show Jen and “Thomas”
        self.play(self.frame_cards("Jen", "Eric"))

        # Put red X over Thomas card
        self.play(self.cross_card("Eric"))

        # Make Jen-”Thomas” connection disappear then reappear (for 5 secs eg)
        self.play(self.g.links[("Jen", "Eric")].animate.set_opacity(0))
        self.wait(1)
        self.play(
            self.g.links[("Jen", "Eric")].animate.set_opacity(1),
            self.uncross_card("Eric"),
        )

        # Zoom fully in on “Thomas” card
        self.play(self.fully_zoom_card("Eric"))
        self.wait(1)

        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric"))

        # Create VMS card, pan over to (not fully zoomed)
        self.play(self.frame_cards("Jen", "Eric", "VMS"))
        self.play(
            self.add_card("VMS"),
        )

        # Create Caldeira and link to VMS
        self.play(
            self.add_card_from("VMS", "Caldeira"),
            self.frame_cards("VMS", "Caldeira"),
        )
        self.wait(1)

        # Zoom fully on Caldeira
        self.play(self.fully_zoom_card("Caldeira"))
        self.wait(1)

        # Zoom fully on VMS
        self.play(self.fully_zoom_card("VMS"))
        self.wait(1)

        # Create Havana_incident (but don’t zoom), link to Caldeira and VMS
        self.play(self.frame_cards("VMS", "Caldeira", "Havana"))
        self.play(
            self.add_card("Havana"),
            self.add_link("VMS", "Havana"),
            self.add_link("Caldeira", "Havana"),
        )
        self.wait(1)

        # Show all so far
        self.play(self.frame_cards("VMS", "Caldeira", "Havana", "Jen", "Eric", "Moody"))

        # Highlight or pan between Jen, Eric, Caldeira and VMS
        self.play(self.circle_card("Jen"))
        self.play(self.circle_card("Eric"))
        self.play(self.circle_card("Caldeira"))
        self.play(self.circle_card("VMS"))
        self.wait(1)
        self.play(self.clear_circles())

        # Zoom on Caldeira
        self.play(self.fully_zoom_card("Caldeira"))
        self.wait(1)

    def sequence2(self):
        # Reshuffle layout for all the new cards incoming
        self.play(self.frame_cards("VMS", "Caldeira", "Havana", "Jen", "Eric", "Moody"))
        self.play(self.animate_update_layout())

        # Zoom out then partly zoom on VMS
        self.play(self.frame_cards("VMS", "Prix"))

        # Create Prix Bouchard card (emerge from VMS) and zoom in on
        self.play(self.add_card_from("VMS", "Prix"))
        self.play(self.fully_zoom_card("Prix"))
        self.wait(1)

        # Create Lewis Looper card (emerge from VMS)
        self.play(self.frame_cards("VMS", "Looper", "Prix"))
        self.play(self.add_card_from("VMS", "Looper"))
        self.play(self.fully_zoom_card("Looper"))
        self.wait(1)

        # Create Artefacts (partially zoom on but not fully) and link to VMS and Looper
        self.play(self.frame_cards("VMS", "Looper", "Artefacts"))
        self.play(
            self.add_card("Artefacts"),
            self.add_link("Looper", "Artefacts"),
            self.add_link("VMS", "Artefacts"),
        )

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
        self.wait(1)

        # Pan (still zoomed) to Artefacts
        self.play(self.fully_zoom_card("Artefacts"))
        self.wait(1)

        # Zoom out, create Santorini_deaths, fully zoom in on
        self.play(
            self.frame_cards("VMS", "Prix", "Sant_Deaths"),
            self.add_card("Sant_Deaths"),
        )
        self.play(self.fully_zoom_card("Sant_Deaths"))
        self.wait(1)

        # Zoom fully on Jen
        self.play(self.frame_cards())
        self.play(self.fully_zoom_card("Jen"))
        self.wait(1)

        # Zoom fully on Eric
        self.play(self.fully_zoom_card("Eric"))
        self.wait(1)

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
        self.wait(1)

        # Show Ilsa, Eric, Moody and Jen.
        self.play(self.frame_cards("Moody", "Ilsa", "Jen", "Eric"))

        # Zoom on Jen and Eric, highlight link
        self.play(
            self.frame_cards("Jen", "Eric"),
            self.highlight_link("Jen", "Eric", color=BLUE_E),
        )
        self.wait(1)

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

        # Zoom out halfway and pan to Moody, then Ilsa.
        self.play(self.frame_cards("Moody", margin=2))
        self.wait(0.5)
        self.play(self.camera.frame.animate.move_to(self.current_pos("Ilsa")))
        self.wait(0.5)

        # Link Moody and Ilsa to Sum_tape
        self.play(self.frame_cards("Sum_Tape", "Moody", "Sum_Tape"))

        self.play(
            self.add_link("Moody", "Sum_Tape"),
            self.add_link("Ilsa", "Sum_Tape"),
        )

        # Zoom fully on Sum_tape
        self.play(self.fully_zoom_card("Sum_Tape"))
        self.wait(1)

        # Zoom out slowly then show Jen/Eric/Moody/Ilsa
        self.play(self.frame_cards("Jen", "Eric", "Moody", "Ilsa"), run_time=3)

        # Highlight Jen and Ilsa link
        self.play(self.highlight_link("Ilsa", "Jen"))
        self.wait(1)

        # Link Ilsa and Moody to Artefacts
        self.play(
            self.unhighlight_link("Ilsa", "Jen"),
            self.frame_cards("Moody", "Ilsa", "Artefacts"),
        )
        self.wait(1)

        self.play(
            self.add_link("Moody", "Artefacts"),
            self.add_link("Ilsa", "Artefacts"),
        )

        # Create Mysterious_men and fully zoom in on
        self.play(
            self.frame_cards("Jen", "Eric", "Myst_Men"),
            self.add_card("Myst_Men"),
        )
        self.play(self.fully_zoom_card("Myst_Men"))
        self.wait(1)

        # Create Serin (linked to Eric), zoom on a little but not fully
        self.play(self.frame_cards("Serin", "Eric"))
        self.play(self.add_card("Serin"), self.add_link("Eric", "Serin"))
        self.wait(1)

        # Zoom (not fully) to Moody
        self.play(self.frame_cards("Moody", margin=2.5))
        self.wait(1)

        # Vanish Sum_tape and Straka connection
        self.play(self.frame_cards("Sum_Tape", "VMS"))
        self.play(self.g.links["VMS", "Sum_Tape"].animate.set_opacity(0))
        self.wait(1)

        # Pan to Caldeira (not fully zoomed)
        self.play(self.pan_to("Caldeira"))
        self.wait(1)

        # Zoom fully on Artefacts
        self.play(self.fully_zoom_card("Artefacts"))
        self.wait(1)

        # Zoom out and pan to Jen
        self.play(self.frame_cards("Jen", margin=3))
        self.wait(1)

        # Pan to Moody, then Sum_tape, then Artefacts
        self.play(self.pan_to("Moody"))
        self.wait(0.5)
        self.play(self.pan_to("Sum_Tape"))
        self.wait(0.5)
        self.play(self.pan_to("Artefacts"))
        self.wait(0.5)

        # Pan to Eric, add golden outline or green tick over card
        self.play(self.pan_to("Eric"))
        self.play(
            Circumscribe(self.g.cards["Eric"], color=YELLOW_D, stroke_width=8),
            run_time=1.5,
        )

        # Pan to Ilsa
        self.play(self.pan_to("Ilsa"))
        self.wait(1)

        # Pan to Mysterious_men
        self.play(self.pan_to("Myst_Men"))
        self.wait(1)

    def sequence3(self):
        # Create Dejardins and link to Eric, fully zoom in on
        self.play(self.frame_cards(*MODERN_DAY_CARDS))
        self.play(self.animate_update_layout())
        self.play(self.frame_cards("Eric", "Desjardins", "Moody"))
        self.play(self.add_card("Desjardins"), self.add_link("Eric", "Desjardins"))
        self.play(self.fully_zoom_card("Desjardins"))
        self.wait(1)

        # Zoom out halfway and link Dejardins to Moody
        self.play(self.frame_cards("Eric", "Desjardins", "Moody"))
        self.play(self.add_link("Desjardins", "Moody"))

        # Pan to Serin
        self.play(self.pan_to("Serin"))
        self.wait(1)

        # Link Desjardins and Eric to Artefacts
        self.frame_cards("Desjardins", "Eric", "Artefacts")
        self.play(
            self.add_link("Desjardins", "Artefacts"), self.add_link("Eric", "Artefacts")
        )
        self.wait(1)

        # Zoom fully on Desjardins
        self.play(self.fully_zoom_card("Desjardins"))
        self.wait(1)

        # Zoom fully/pan to Serin
        self.play(self.fully_zoom_card("Serin"))
        self.wait(1)

        # Zoom out, pan to Ilsa
        self.play(self.frame_cards("Ilsa", margin=3))
        self.wait(1)

        # Zoom fully on Caldeira
        # Bonus - link Eric and Caldeira
        self.play(self.frame_cards("Eric", "Caldeira"))

    def sequence4(self):
        self.play(
            LaggedStart(
                AnimationGroup(
                    self.animate_update_layout(), self.frame_cards("Eric", "Caldeira")
                ),
                self.add_link("Eric", "Caldeira"),
                lag_ratio=0.7,
            ),
            run_time=2,
        )

        self.play(self.fully_zoom_card("Caldeira"))
        self.wait(1)

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
        self.wait(1)

        # Zoom fully on Eric
        self.play(
            self.opacity_except(
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")], opacity=1
            ),
            self.unhighlight_link("Jen", "Eric"),
            self.unhighlight_link("VMS", "Caldeira"),
        )
        self.play(self.fully_zoom_card("Eric"))
        self.wait(1)

        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric", "Myst_Men"))
        self.wait(1)

        # Zoom fully on Mysterious_men
        self.play(self.fully_zoom_card("Myst_Men"))
        self.wait(1)

        # Zoom fully on Jen
        self.play(self.fully_zoom_card("Jen"))
        self.wait(1)

        # Highlight/circle Jen/Eric and VMS/Caldeira
        self.play(
            self.frame_cards("Jen", "Eric", "VMS", "Caldeira"),
            self.opacity_except(
                "Jen",
                "Eric",
                "VMS",
                "Caldeira",
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")],
            ),
        )
        self.wait(1)

        # Link Jen and Moody
        self.play(
            self.frame_cards("Jen", "Moody"),
            self.opacity_except(
                edges=[("Jen", "Eric"), ("VMS", "Caldeira")], opacity=1
            ),
        )

        self.play(
            self.add_link("Jen", "Moody"),
            self.g.cards["Moody"].animate.scale(1),
            self.g.cards["Jen"].animate.scale(1),
        )
        self.wait(1)

        # Pan to Artefacts
        self.play(self.pan_to("Artefacts"))
        self.wait(1)

    def sequence5(self):

        # Show Moody, Artefacts, Sum_tape and Sobreiro
        self.play(
            self.frame_cards("Moody", "Artefacts", "Sum_Tape", "Sobreiro"),
            self.opacity_except("Moody", "Artefacts", "Sum_Tape", "Sobreiro"),
        )

        # Highlight Artefacts, cross over Tape and Sobreiro
        self.play(
            self.highlight_card("Artefacts"),
            self.cross_card("Sum_Tape"),
            self.cross_card("Sobreiro"),
        )
        self.wait()

        # Pan to Eric
        self.play(
            self.unhighlight_card("Artefacts"),
            self.uncross_card("Sum_Tape"),
            self.uncross_card("Sobreiro"),
            self.opacity_except(
                "Moody", "Artefacts", "Sum_Tape", "Sobreiro", opacity=1
            ),
            self.pan_to("Eric"),
        )
        self.wait(1)

        # Link Mysterious_men and Jen
        self.play(self.frame_cards("Myst_Men", "Jen", "Eric"))
        self.play(
            self.add_link("Myst_Men", "Jen"),
            self.g.cards["Myst_Men"].animate.scale(1),
            self.g.cards["Jen"].animate.scale(1),
        )
        self.wait(1)

        # Link Mysterious_men and Eric briefly then vanish
        self.play(
            self.add_link("Myst_Men", "Eric"),
            self.g.cards["Myst_Men"].animate.scale(1),
            self.g.cards["Eric"].animate.scale(1),
        )

        self.wait(1)
        self.play(self.g.links[("Myst_Men", "Eric")].animate.set_stroke(opacity=0))
        self.wait(1)

        # Zoom fully on Mysterious_men
        self.play(self.fully_zoom_card("Myst_Men"))
        self.wait(1)

        # Zoom out to whole diagram
        self.play(
            self.frame_cards(*[c for c in self.nodes if c != "Sant_Deaths"]), run_time=3
        )
        self.wait(1)

        # Zoom fully on Ilsa
        self.play(self.fully_zoom_card("Ilsa"))
        self.wait(1)

        # Zoom fully/pan to Eric
        self.play(self.fully_zoom_card("Eric"))
        self.wait(1)

        # Show Eric and Ilsa and highlight link in green
        self.play(
            LaggedStart(
                self.frame_cards("Eric", "Ilsa", "Moody"),
                self.highlight_link("Eric", "Ilsa", color=GREEN_E),
                lag_ratio=0.5,
            ),
            self.g.cards["Ilsa"].animate.scale(1),
        )
        self.wait(1)

        # Highlight Moody/Eric link in red
        self.play(self.highlight_link("Eric", "Moody", color=PURE_RED))
        self.wait(1)

        # Zoom fully on Sum_tape
        self.play(
            self.unhighlight_link("Eric", "Moody"),
            self.unhighlight_link("Eric", "Ilsa"),
            self.fully_zoom_card("Sum_Tape"),
            self.g.cards["Sum_Tape"].animate.scale(1),
        )
        self.wait(1)

        # Show Jen and Eric
        self.play(self.frame_cards("Jen", "Eric"))
        self.wait(1)

        # Pan to VMS
        self.play(self.pan_to("VMS"))
        self.wait(1)

        # Pan to Serin
        self.play(self.pan_to("Serin"))
        self.wait(1)

        # Pan to Havana Incident
        self.play(self.pan_to("Havana"))
        self.wait(1)

        # Zoom fully on Caldeira
        self.play(self.fully_zoom_card("Caldeira"))
        self.wait(1)

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
        self.prepare_link("Moody", "Jen")

        self.calculate_layout()

        self.sequence4()
        self.sequence5()

        self.play(self.frame_cards())
