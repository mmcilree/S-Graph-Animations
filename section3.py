import manim as mm
import numpy as np

from card_scene import CardGraphScene
from graph import CardContents, MODERN_DAY_CARDS
from typing import cast


class Section3(CardGraphScene):
    def initialise_layout(self):

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

        self.unprepare_link("Eric", "Caldeira")
        self.unprepare_link("Eric", "VMS")
        self.unprepare_link("Jen", "VMS")
        self.unprepare_link("Jen", "Caldeira")

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

        self.prepare_link("Eric", "Desjardins")
        self.prepare_link("Desjardins", "Moody")
        self.prepare_link("Desjardins", "Artefacts")
        self.prepare_link("Eric", "Artefacts")

        self.calculate_layout()

        self.prepare_link("Caldeira", "Eric")
        self.prepare_link("Moody", "Jen")

        self.calculate_layout()
        self.update_layout()
        for l in self.edges:
            self.g.add_link(*l)
            self.add(self.g.links[l])
        for c in self.nodes:
            self.g.add_card(c)
            self.add(self.g.cards[c])
        self.set_icon("Eric", "2.0")

    def construct(self):
        # self.starth()
        self.next_section(skip_animations=True)
        self.initialise_layout()
        self.camera.frame.move_to(self.bounding_box())

        def sequence1():
            self.play(self.frame_cards())

            # "VM Straka is the name used by an unknown author,"
            # Show VMS card 1.4
            self.wait_until(0, 3, 800)
            self.set_slide("VMS", "1.4")
            self.play(self.fully_zoom_card("VMS"))

            # "and confidant FX Caldeira"
            # Show FXC card 3.5 (also can use title card 2 again from now on)
            self.wait_until(0, 20, 0)
            self.set_icon("Caldeira", "2.0")
            self.set_slide("Caldeira", "2.6")
            self.play(self.frame_cards("VMS", "Caldeira"))
            self.play(self.fully_zoom_card("Caldeira"))

        sequence1()

        remove_edges = [
            # ("Caldeira", "Eric"),
            # ("Eric", "Desjardins"),
            ("Jen", "Moody"),
            ("Eric", "Artefacts"),
            ("Desjardins", "Artefacts"),
        ]

        for r in remove_edges:
            self.unprepare_link(*r)

        self.prepare_link("Ekstrom", "Durand")
        self.prepare_link("S_Org", "VMS")
        self.prepare_link("S_Org", "Ekstrom")
        self.prepare_link("Sum_Tape", "Ekstrom")
        self.prepare_link("Wechsler", "Feuerbach")
        self.prepare_link("Durand", "Ferrara")
        self.prepare_link("Feuerbach", "S_Org")
        self.prepare_link("Summersby", "Caldeira")
        self.prepare_link("Summersby", "S_Org")
        self.prepare_link("Summersby", "Sum_Tape")
        self.prepare_link("MacInnes", "S_Org")
        self.prepare_link("Wechsler", "Durand")
        self.prepare_link("Wechsler", "Ferrara")
        self.prepare_link("Feuerbach", "Durand")
        self.prepare_link("Feuerbach", "Ferrara")
        self.prepare_link("Summersby", "Ekstrom")
        self.prepare_link("S_Org", "MacInnes")
        self.prepare_link("S_Org", "Vaclav")
        self.prepare_link("S_Org", "Bridge_Jump")
        self.prepare_link("Vaclav", "Bridge_Jump")

        # "it's time to talk about the S organisation"
        # Create and show S org card 1.1
        self.wait_until(1, 26, 700)

        self.calculate_layout(esep=0.06)

        def sequence2():
            self.play(
                self.frame_cards(margin=-2),
                *[self.remove_link(*r) for r in remove_edges],
                self.animate_update_layout(),
            )
            self.play(
                self.frame_cards("S_Org", margin=4),
                self.add_card("S_Org"),
                self.add_link("S_Org", "VMS", other_end=True),
            )
            self.play(self.fully_zoom_card("S_Org"))

            # "some suspects are clearly the basis for a group of characters featured in SoT."
            # Show S org 1.2
            self.wait_until(1, 39, 0)
            self.play(self.change_slide("S_Org", "1.2"))

            # "First, the oldest of the bunch: Torsten Ekstrom"
            # Create and zoom on Ekstrom 1.1
            self.wait_until(1, 58, 720)
            self.play(self.frame_cards("S_Org", "Ekstrom"))
            self.play(self.add_card("Ekstrom"))
            self.play(self.fully_zoom_card("Ekstrom"))

            # "in the Summersby tape"
            # Show Sum_tape and Ekstrom linking (Summersby tape 1.4 used from now on)
            self.wait_until(2, 8, 80)
            self.play(
                self.frame_cards("Ekstrom", "Sum_Tape"),
                self.add_link("Ekstrom", "Sum_Tape", other_end=True),
            )
            self.set_slide("Sum_Tape", "1.4")

            # "Obviously Summersby could [id]have been lying, but Desjardins firmly believed that Ekstrom "
            # Zoom back to Ekstrom 1.1
            self.wait_until(2, 12, 0)
            self.play(self.fully_zoom_card("Ekstrom"))

            # Also, he is the fourth person to suspiciously “fall from a balcony”,
            # Show Ekstrom 1.2
            self.wait_until(2, 19, 640)
            self.play(self.change_slide("Ekstrom", "1.2"))

            # "Next up is Amarante Durand"
            # Create Durand and show 1.1
            self.wait_until(2, 49, 260)
            self.play(self.frame_cards("Ekstrom", "Durand"), self.add_card("Durand"))
            self.play(self.fully_zoom_card("Durand"))

            # "She famously discovered a cave in the Dordogne containing ancient paintings"
            # Show Durand 1.2
            self.wait_until(2, 56, 970)
            # self.play(self.change_slide("Durand", "1.2"))

            # "Her and Ekstrom’s character analogues"
            # Link to Ekstrom, then zoom back in on 1.2
            self.wait_until(3, 3, 780)
            self.set_slide("Durand", "1.2")
            self.play(
                self.frame_cards("Durand", "Ekstrom"),
                self.add_link("Durand", "Ekstrom", other_end=True),
            )
            self.play(self.fully_zoom_card("Durand"))

            # "After his death"
            # Cut back to Durand 1.3
            self.wait_until(3, 19, 780)
            self.play(self.change_slide("Durand", "1.3"))

            # "We also know Durand was rumoured to be close to VMS"
            # Show Durand 1.4
            self.wait_until(3, 43, 640)
            self.play(self.change_slide("Durand", "1.4"))

            # "we have Tiago García Ferrara"
            # Create and zoom on Ferrara 1.1
            self.wait_until(3, 55, 0)
            self.play(self.frame_cards("Durand", "Ferrara"), self.add_card("Ferrara"))
            self.play(self.fully_zoom_card("Ferrara"))

            # "Ferrara turned coat and sold out Durand"
            # Switch to Ferrara 1.2
            self.wait_until(4, 14, 960)
            self.play(self.change_slide("Ferrara", "1.2"))

            # "He was outcast from society after the war"
            # Switch to Ferrara 1.3
            self.wait_until(4, 30, 380)
            self.play(self.change_slide("Ferrara", "1.3"))

            # "So this Spain incident was bad all around"
            # Back to Ferrara 1.3 then Zoom out
            self.wait_until(4, 42, 660)
            self.play(
                self.frame_cards("Ferrara", "Durand"),
                self.add_link("Ferrara", "Durand"),
            )

            # "Completely uninvolved in this was Reinhold Feuerbach"
            # Create and zoom on Feuerbach 1.1
            self.wait_until(4, 45, 500)
            self.play(
                self.frame_cards("Ferrara", "Durand", "Feuerbach"),
                self.add_card("Feuerbach"),
            )
            self.play(self.fully_zoom_card("Feuerbach"))

            # "1886 Haymarket Bombing"
            # Switch to Feuerbach 1.2
            self.wait_until(5, 6, 0)
            self.play(self.change_slide("Feuerbach", "1.2"))

            # "In 1937 he was living in Germany"
            # Show feuerbach 1.3
            self.wait_until(5, 15, 980)
            self.play(self.change_slide("Feuerbach", "1.3"))

            # "Horst Wechsler"
            # Horst box emerges, pan to/zoom on 1.1
            self.wait_until(5, 29, 0)
            self.play(
                self.frame_cards("Feuerbach", "Wechsler"),
                self.add_card_from("Feuerbach", "Wechsler"),
            )

            self.play(self.fully_zoom_card("Wechsler"))

            # "Upon Feuerbach’s death,"
            # Switch to Wechsler 1.2
            self.wait_until(5, 39, 180)
            self.play(self.change_slide("Wechsler", "1.2"))

            self.wait_until(5, 48, 220)
            self.play(self.frame_cards("Feuerbach", "Durand", "Ekstrom", "Ferrara"))

            # "you’ll notice that these four"
            # Circle three candidates
            self.wait_until(5, 52, 240)
            self.play(
                self.circle_card("Feuerbach"),
                self.circle_card("Durand"),
                self.circle_card("Ekstrom"),
            )

            # "Victor Martin Summersby"
            # Create and zoom into Summersby 1.1
            self.wait_until(6, 0, 500)
            self.play(
                self.clear_circles(),
                self.frame_cards("Ekstrom", "Durand", "Summersby", "Sum_Tape"),
            )
            self.play(
                self.add_card_from("Sum_Tape", "Summersby"),
                self.frame_cards("Sum_Tape", "Summersby"),
            )
            self.play(self.fully_zoom_card("Summersby"))

            # "FXC says he was the only friend of VMS'"
            # Link Sum to Caldeira
            self.wait_until(6, 22, 280)

            self.play(
                self.frame_cards("Summersby", "Caldeira"),
            )
            self.play(self.add_link("Summersby", "Caldeira"))
            # Although Summersby doesn’t have a proper [je]character in SoT,
            # [je]Back to Sum, now 1.2
            self.set_slide("Summersby", "1.2")
            self.wait_until(6, 30, 780)
            self.play(self.fully_zoom_card("Summersby"))

            # "the most canonically popular candidate: Guthrie MacInnes.[jf]"
            # [jf]Create and zoom on MacInnes 1.1
            self.wait_until(6, 44, 140)
            self.play(self.frame_cards("MacInnes", margin=2))
            self.play(self.add_card("MacInnes"))
            self.play(self.fully_zoom_card("MacInnes"))

            # "is something called Multitudinalism[jh]"
            # [jh]Switch to MacInnes 1.2
            self.wait_until(7, 10, 380)
            self.play(self.change_slide("MacInnes", "1.2"))

            # "But Eric claims "If there's no real self[ji]"
            # [ji]MacInnes 1.3
            self.wait_until(7, 25, 40)
            self.play(self.change_slide("MacInnes", "1.3"))

            # "M"acInnes died peacefully of old age in 1969 (unlike the others).
            # [jk]Cut back to MacInnes 1.4
            self.wait_until(7, 52, 120)
            self.play(self.change_slide("MacInnes", "1.4"))

            # "but is named in the foreword: Vaclav Straka.[jl]"
            # [jl]Create and show Vaclav 1.1
            self.wait_until(8, 2, 860)
            self.play(self.frame_cards("Vaclav", margin=2))
            self.play(self.add_card("Vaclav"))
            self.play(self.fully_zoom_card("Vaclav"))

            # "his biography starts with him being born[jm]"
            # [jm]Vaclav 1.2
            self.wait_until(8, 11, 380)
            self.play(self.change_slide("Vaclav", "1.2"))

            # "and ends with him committing suicide [jn]"
            # [jn]Vaclav 1.3
            self.wait_until(8, 16, 0)
            self.play(self.change_slide("Vaclav", "1.3"))

            self.play(
                self.add_card("Bridge_Jump"), self.add_link("Vaclav", "Bridge_Jump")
            )

            # "But this is a bad argument"
            # Easy verison: Vaclav 1.4
            self.wait_until(9, 3, 0)
            self.play(self.change_slide("Vaclav", "1.4"))

            # "Equally though, [ju]we can’t just say “"
            # [ju]Back to Vaclav 1.5
            self.wait_until(9, 8, 100)
            self.play(self.change_slide("Vaclav", "1.5"))

            # "It could be one of these writers [jw]"
            # [jw]Circle S candidates minus Vaclav
            self.wait_until(9, 24, 420)
            self.play(
                self.frame_cards("Durand", "Ekstrom", "Feuerbach", "Ferrara"),
                self.circle_card("Durand"),
                self.circle_card("Ekstrom"),
                self.circle_card("Feuerbach"),
                self.circle_card("Ferrara"),
            )

            # "Ekstrom and Durand, and Durand and Ferrara. [jx]"
            # [jx]Highlight connection, or add now
            self.wait_until(9, 34, 900)
            self.play(
                self.clear_circles(),
                self.highlight_link("Durand", "Ekstrom", color=mm.BLUE_C),
            )
            self.play(self.highlight_link("Ferrara", "Durand"))

            # "Immediately, if Weschler was there then Feuerbach probably was too[jz]"
            # [jz]Connect Weschler then Feuerbach to other candidates
            self.wait_until(9, 49, 500)
            self.play(
                self.unhighlight_link("Durand", "Ekstrom"),
                self.unhighlight_link("Ferrara", "Durand"),
                self.add_link("Wechsler", "Ferrara"),
                self.add_link("Wechsler", "Durand"),
            )

            self.play(
                self.add_link("Feuerbach", "Durand"),
                self.add_link("Feuerbach", "Ferrara"),
            )
            # self.play(self.add_link("W))
            # "Summersby did claim to co-write the first VMS attributed book with Ekstrom[ke]"
            # [ke]Link Sum to Ekstrom, Zoom on Summersby tape box 1.4
            self.wait_until(10, 27, 640)
            self.play(self.frame_cards("Summersby", "Ekstrom", "Sum_Tape"))
            self.play(self.add_link("Summersby", "Ekstrom"))
            self.set_slide("Sum_Tape", "1.4")
            self.play(self.fully_zoom_card("Sum_Tape"))

            # "Unfortunately, since Ekstrom didn’t[kl] normally write for adults a"
            # [kl]Diagram - Zoom on Ekstrom 1.4
            self.wait_until(12, 8, 880)
            self.set_slide("Ekstrom", "1.4")
            self.play(self.frame_cards("Ekstrom", "Sum_Tape"))
            self.play(self.fully_zoom_card("Ekstrom"))

        sequence2()

        # "So all these individual ties further the idea that the candidates worked together.[km]"
        # [km]Reshuffle diagram so the candidates are all connected to the S organisation rather than each other. But leave Durand/ekstrom and durand/ferrara
        self.wait_until(12, 19, 0)
        new_edges = [
            ("Ekstrom", "S_Org"),
            ("Summersby", "S_Org"),
            ("Durand", "S_Org"),
            ("Feuerbach", "S_Org"),
            ("Ferrara", "S_Org"),
        ]
        remove_edges = [
            ("Ekstrom", "Durand"),
            ("Durand", "Ferrara"),
            ("Wechsler", "Durand"),
            ("Wechsler", "Ferrara"),
            ("Feuerbach", "Durand"),
            ("Feuerbach", "Ferrara"),
            ("Summersby", "Ekstrom"),
        ]

        for e in new_edges:
            self.prepare_link(*e)

        for e in remove_edges:
            self.unprepare_link(*e)

        self.play(
            self.frame_cards(
                "Ekstrom", "Durand", "Feuerbach", "Ferrara", "Wechsler", "Summersby"
            )
        )

        s_org_pos = self.current_pos("S_Org")

        self.calculate_layout(esep=0.06)

        def sequence3():

            self.play(
                self.frame_cards(
                    "Ekstrom", "Durand", "Feuerbach", "Ferrara", "Summersby"
                ),
                *[self.remove_link(*r) for r in remove_edges],
                self.animate_update_layout(),
                *[self.add_link(*e, from_point=s_org_pos) for e in new_edges],
                run_time=3,
            )

            self.play(self.frame_cards())

            # "because that doesn’t identify who Caldeira’s Straka was[kn]"
            # [kn]Zoom on Caldeira and Straka
            self.wait_until(12, 32, 40)
            self.play(self.frame_cards("Caldeira", "VMS"))

            # "V. Finch is probably Summersby[kr]"
            # [ks]Link Sum with S_org in background

            # "why exactly does VMS need to stay secret anyway[ku]"
            # [ku]Zoom back on VMS card 1.4
            self.set_slide("VMS", "1.4")

            self.wait_until(13, 37, 60)
            self.play(self.fully_zoom_card("VMS"))

        sequence3()

        # "Re-introducing Hermes Bouchard:[kv]"
        # [kv]Create and zoom on Bouchard 1.1
        self.prepare_link("Calais", "Bouchard")
        self.prepare_link("Prix", "Bouchard")
        self.prepare_link("Sant_Deaths", "Bouchard")
        self.prepare_link("Prix", "Calais")
        self.prepare_link("Calais", "VMS")
        self.prepare_link("Bouchard", "Arp")
        self.prepare_link("Wechsler", "Arp")

        self.unprepare_link("Ekstrom", "Sum_Tape")
        self.unprepare_link("Caldeira", "Summersby")
        self.calculate_layout(esep=0.06)

        def sequence4():
            self.play(
                self.frame_cards("Bouchard", margin=8),
                self.remove_link("Ekstrom", "Sum_Tape"),
                self.remove_link("Caldeira", "Summersby"),
                self.animate_update_layout(),
                self.add_card("Bouchard"),
                self.add_link(
                    "Bouchard", "Prix", from_point=self.layouts[-1][0]["Bouchard"]
                ),
            )
            self.play(self.fully_zoom_card("Bouchard"))
            # "Bouchard inspired antagonists in both Wineblood"
            # [kw]Switch to Bouchard 1.2
            self.wait_until(14, 0, 160)
            self.play(self.change_slide("Bouchard", "1.2"))

            # "So here’s the issue[kx]"
            # [kx]Pan to Prix Bouchard card 1.1, switch to 1.2
            self.wait_until(14, 11, 20)
            self.play(self.fully_zoom_card("Prix"))
            self.play(self.change_slide("Prix", "1.2"))

            # "Caldeira claims [ky]it was an accusation towards Bouchard."
            # [ky]Switch to 1.3
            self.wait_until(14, 19, 840)
            self.play(self.change_slide("Prix", "1.3"))

            # "deaths of syndicalist agitators and was behind a recent massacre [kz]of factory workers in Calais."
            # [kz]Create Calais massacre card and link to Bouchard and Prix Bouchard
            self.wait_until(14, 29, 500)
            self.play(self.frame_cards("Bouchard", "Prix", "Calais"))
            self.play(
                self.add_card_from("VMS", "Calais"),
                self.add_link("Calais", "Prix"),
                self.add_link("Bouchard", "Calais", other_end=True),
            )

            # "This is described by FXC in Chapter 4:[la]"
            # [la]Zoom into Calais card but fade to drawing of massacre (or other image) with quote appearing on top. Then at end of quote, fade back into actual Calais card
            self.wait_until(14, 31, 40)
            self.play(self.fully_zoom_card("Calais"))

            # "Eric says Straka’s note ["
            # [lb]Pan to Prix Bouchard 1.4
            self.wait_until(14, 58, 220)
            self.set_slide("Prix", "1.4")
            self.play(self.fully_zoom_card("Prix"))

            # "disappeared in 1983, and quotes it[lc]: "You seek a world populated by trick monkeys who dance to your tunes for the empty promise of coins""
            # [lc]Switch to Prix 1.5
            self.wait_until(15, 0, 0)
            self.play(self.change_slide("Prix", "1.5"))

            # " Jen and FXC[ld] both seem to agree that this accusation d"
            # [ld]Switch to Prix 1.6
            self.wait_until(15, 10, 380)
            self.play(self.change_slide("Prix", "1.6"))

            # "she confirmed that "Everything goes back to Calais"."
            # [le]Pan to Calais 1.2
            self.wait_until(15, 17, 60)
            self.set_slide("Calais", "1.2")
            self.play(self.fully_zoom_card("Calais"))

            # "likely[lf] suspect for the Santorini man murders."
            # [lf]Link Bouchard card to Santorini man murders
            self.wait_until(15, 21, 720)
            self.play(self.frame_cards("Bouchard", "Sant_Deaths"))
            self.play(self.add_link("Bouchard", "Sant_Deaths"))

            # "This was at least Desjardins’ theory.[lg]"
            # [lg]Could circle Dejardins (or not, for easy)
            self.wait_until(15, 25, 500)
            self.play(self.frame_cards("Desjardins", margin=2))
            self.play(self.circle_card("Desjardins"))

            # "But how exactly would Bouchard have that much influence if his company ended?[lh]"
            # [lh]Zoom back to Bouchard card 1.3
            self.wait_until(15, 28, 240)
            self.set_slide("Bouchard", "1.3")
            self.play(self.fully_zoom_card("Bouchard"))

            # "to spawn and control a bunch of shell companies["
            # [li]Switch to Bouchard 1.4
            self.wait_until(15, 36, 160)
            self.play(self.change_slide("Bouchard", "1.4"))

            # "manufacturer called Arp Syndikat.[lj]"
            # [lj]Create Arp card from Bouchard and zoom on arp 1.1
            self.wait_until(15, 45, 60)
            self.play(self.frame_cards("Bouchard", "Arp"))
            self.play(
                self.add_card_from("Bouchard", "Arp"),
                self.frame_cards("Bouchard", "Arp"),
            )

            # "In SoT itself, the Bouchard stand-in ("
            # [lk]ARP 1.2
            self.wait_until(16, 1, 960)
            self.play(self.change_slide("Arp", "1.2"))

            # "Hermes Bouchard had a son[lp]"
            # [lp]Zoom on Bouchard 1.5
            self.wait_until(16, 53, 680)
            self.set_slide("Bouchard", "1.5")
            self.play(self.fully_zoom_card("Bouchard"))

            # "interview about Vaclav Straka’s death[lq]"
            # [lq]Circle Prague jump and feuerbach
            self.wait_until(17, 17, 100)
            self.play(self.frame_cards("Feuerbach", "Bridge_Jump"))
            self.play(self.circle_card("Feuerbach"))
            self.play(self.circle_card("Bridge_Jump"))

            # "This is therefore huge - [lt]the earliest and only record w"
            # [lt]Move back to diagram, zoom on group as a whole if possible, connect S org to Prague bridge jump
            self.wait_until(17, 42, 20)
            self.play(
                self.frame_cards(
                    "Feuerbach", "Ferrara", "Ekstrom", "Durand", "S_Org", "Bridge_Jump"
                )
            )

        sequence4()
        self.play(
            self.animate_update_layout(),
            self.clear_circles(),
            self.opacity_except(
                "Feuerbach",
                "Ferrara",
                "Ekstrom",
                "Durand",
                "S_Org",
                "Bridge_Jump",
                "Vaclav",
            ),
            self.add_link("Bridge_Jump", "S_Org", other_end=True),
            run_time=3,
        )

        # "except an alive Vaclav Straka?[lu]"
        # [lu]Connect Vaclav card to S organisation
        self.play(self.pan_to("Vaclav"))
        # [lv]Possible reconfig
        # "His candidacy [lw]now works on multiple levels."
        # [lw]Zoom on Vaclav card 1.6
        self.set_slide("Vaclav", "1.6")

        self.play(self.fully_zoom_card("Vaclav"), run_time=3)
        self.play(
            self.opacity_except(
                "Feuerbach",
                "Ferrara",
                "Ekstrom",
                "Durand",
                "S_Org",
                "Bridge_Jump",
                "Vaclav",
                opacity=1,
            ),
        )
        # For context:[lx] the first four chapters consist of an unnamed
        # protagonist being reborn from a river, meeting a group who share names
        # with the birds in this hotel register, and witnessing a massacre of
        # striking workers organised by an evil factory owner.
        self.wait_until(18, 10, 860)
        self.play(
            self.frame_cards(
                "Feuerbach", "Ferrara", "Ekstrom", "Durand", "S_Org", "Bridge_Jump"
            ),
            run_time=6,
        )
        # [lx]Pan towards bridge jump, then over S org group, then over Calais
        # massacre. Don't need to totally zoom in, want to get picture of how
        # all connected.
        self.play(self.frame_cards("Calais", margin=9), run_time=6)

        # "best option for Caldeira, which she herself admits to Eric[ly]"
        # [ly]Either show quote, pan to Caldeira card, or stay on Vaclav for easiest
        self.wait_until(18, 28, 860)
        self.play(self.frame_cards("VMS", "Caldeira"))

        # "Vaclav was “holding his manuscript when he jumped"[lz]"
        # [lz]Go to Vaclav 1.7
        self.wait_until(18, 44, 360)
        self.set_slide("Vaclav", "1.7")
        self.play(self.fully_zoom_card("Vaclav"))

        # "One of the few things we know about Ekstrom is that he was a great swimmer at university.[ma]"
        # [ma]Zoom in on Ekstrom 1.5
        self.wait_until(18, 47, 440)
        self.play(self.frame_cards("Vaclav", "Ekstrom"))
        self.set_slide("Ekstrom", "1.5")
        self.play(self.fully_zoom_card("Ekstrom"))

        # "Then he and Durand[mc]"
        # [mc]Zoom out to show both E and D
        self.wait_until(18, 57, 420)
        self.play(
            self.frame_cards("Ekstrom", "Durand"),
        )

        # "timeline: Durand and Ekstrom[me]"
        # [me]Pan to above Durand and ekstrom (but not fully in), then Vaclav
        self.wait_until(19, 9, 500)
        self.play(
            self.highlight_card("Durand", color=mm.BLUE_E, width=8),
            self.highlight_card("Ekstrom", color=mm.BLUE_E, width=8),
        )

        self.wait_until(19, 11, 800)
        self.play(
            self.pan_to("Vaclav"), self.highlight_card("Vaclav", color=mm.GREEN_E)
        )

        self.wait_until(19, 16, 700)

        self.play(
            self.frame_cards(
                "Feuerbach",
                "Vaclav",
                "Ferrara",
                "Ekstrom",
                "Durand",
                # "S_Org",
                "Bridge_Jump",
            ),
            self.highlight_card("Ferrara", color=mm.PURPLE_E, width=8),
            self.highlight_card("Feuerbach", color=mm.PURPLE_E, width=8),
        )
        # "like-minded friends[mf]"
        # [mf]Circle group OR just show in pan

        # "use Vaclav’s anonymity to make political statements they otherwise couldn’t.[mg]"
        # [mg]Make Vaclav replace Straka. (replace VMS card with title 2)

        self.wait_until(19, 22, 880)
        self.play(
            *[
                self.unhighlight_card(c)
                for c in ["Feuerbach", "Ferrara", "Ekstrom", "Durand", "Vaclav"]
            ]
        )
        self.wait_until(19, 23, 880)
        self.prepare_link("VMS", "Bridge_Jump")
        self.prepare_link("Singh", "S_Org")
        self.unprepare_link("Vaclav", "Bridge_Jump")
        self.nodes.remove("Vaclav")
        # self.set_icon("VMS", "2.0")
        vms = self.g.cards["VMS"]
        # vms.show_img(vms.get_current_icon())
        old_link = self.g.links[("Vaclav", "Bridge_Jump")]
        self.calculate_layout(esep=0.08)
        vaclav = cast(CardContents, self.remove_card("Vaclav"))
        vaclav.name = "VMS"
        bridge_jump = self.g.cards["Bridge_Jump"]
        vaclav.set_z_index(10)

        bridge_jump.set_z_index(8)
        self.g.cards["MacInnes"].set_z_index(8)

        vms_copy = vms.copy().move_to(vaclav.get_center()).set_z_index(15)
        vms_copy.set_opacity(0)
        new_link = self.g.add_link(
            "VMS",
            "Bridge_Jump",
            spline_data=self.layouts[-1][1][("VMS", "Bridge_Jump")],
        ).set_opacity(0)

        if not self.skip_animations:
            self.play(
                self.camera.frame.animate.move_to(
                    vaclav.get_center()
                ).scale_to_fit_width(4),
            )
        d0 = vms.get_center() - vaclav.get_center()

        def t_func(p1, p2):
            return 1 - np.dot(p2.get_center() - p1.get_center(), d0) / np.dot(d0, d0)

        t_updater = lambda f: f.move_to(vaclav.get_center()).scale_to_fit_width(
            4 + 8 * t_func(vaclav, vms)
        )
        # print(dist)
        self.camera.frame.add_updater(t_updater)
        vms_img = vms_copy.get_image("2.0")
        self.g.remove_link("Vaclav", "Bridge_Jump")
        self.play(
            old_link.animate.become(new_link).set_opacity(1),
            self.animate_update_layout(),
            # vaclav.animate.show_img("2.0"),
            # self.add_link("VMS", "Bridge_Jump"),
            vaclav.animate.move_to(self.current_pos("VMS")),
            # vms_img.animate.move_to(self.current_pos("VMS")).set_opacity(1),
            rate_functions=mm.lingering,
            run_time=6,
        )
        # Hand off from the morphed stand-in to the canonical VMS->Bridge_Jump
        # link: reveal new_link first, then drop old_link, so the edge never
        # blinks out (new_link was created at opacity 0 as the become() target).
        new_link.set_opacity(1)
        self.add(new_link)
        self.remove(old_link)
        self.set_icon("VMS", "2.0")
        vms.show_img(vms.get_current_icon())
        self.camera.frame.remove_updater(t_updater)

        self.play(mm.FadeOut(vaclav), self.frame_cards("VMS", margin=3))
        self.remove(vaclav)
        # "were at the Calais massacre, and Chapter 3 of SoT suggests that Vaclav himself could have been[mh]"
        # [mh]Show connection between V and Mas
        self.wait_until(19, 37, 640)

        self.play(
            self.frame_cards("VMS", "Calais"),
            self.highlight_link("Calais", "VMS", mm.PURE_RED),
        )
        # "As to why Vaclav went [mj]along with all this, who knows?"
        # [mj]Zoom in on VMS 2.1
        self.wait_until(19, 49, 980)
        self.set_slide("VMS", "2.1")
        self.play(self.fully_zoom_card("VMS"))

        # "Here’s the rub though: this is all really speculation[mn]"
        # [mn]Show whole diagram
        self.wait_until(20, 49, 760)
        self.play(self.frame_cards("VMS", margin=2))
        self.play(self.frame_cards(), run_time=6)

        # "MacInnes and Summersby[mr] are probably the two most i"
        # [mr]Link MacInnes to S org card, highlight him and Summersby
        self.wait_until(21, 28, 480)
        self.play(self.frame_cards("MacInnes", "Summersby"))
        self.play(
            self.add_link("MacInnes", "S_Org", other_end=True),
            self.circle_card("MacInnes"),
            self.circle_card("Summersby"),
        )

        # "Singh[mt][mu] is the only relevant one,"
        # [mu]Make card in background
        self.wait_until(21, 39, 480)
        self.play(
            self.clear_circles(),
            self.add_card("Singh"),
            self.add_link("Singh", "S_Org"),
        )

        # "Although this all seems to be going swimmingly[my]"
        # [my]Show whole diagram
        self.wait_until(22, 11, 620)
        self.frame_cards(
            "MacInnes", "Summersby", "Singh", "Wechsler", "VMS", "Caldeira"
        )

        # "the S must have fallen apart[mz] at some point."
        # [mz]Show S org card 1.3
        self.wait_until(22, 13, 460)
        self.set_slide("S_Org", "1.3")
        self.play(self.fully_zoom_card("S_Org"))

        # "sold out the original group. [nc]"
        # [nc]When we cut back to card before zooming out, show S_org 1.4
        self.wait_until(22, 20, 520)
        self.play(self.change_slide("S_Org", "1.4"))

        # "this is a reference to the Ferrara-Durand betrayal[nd]"
        # [nd]Pan to show both)
        self.wait_until(22, 25, 200)
        self.play(
            self.frame_cards("Durand", "Ferrara"),
        )

        # "Jen and Eric specifically mention MacInnes[ne]"
        # [ne]Pan to MacInnes
        self.wait_until(22, 28, 460)
        self.play(self.pan_to("MacInnes"))

        # "Here’s where Caldeira’s ciphers [nf]"
        # [nf]Pan to Caldeira
        self.wait_until(22, 32, 880)
        self.play(self.pan_to("Caldeira"))

        # "Jen and Eric say Looper split from the S in 1926[nh]"
        # [nh]Cut to Looper card 1.2
        self.set_slide("Looper", "1.2")
        self.wait_until(22, 50, 500)
        self.play(self.fully_zoom_card("Looper"))

        # "But to complicate matters further,[ni]"
        # [ni]Switch to Looper 1.3
        self.wait_until(22, 57, 260)
        self.play(self.change_slide("Looper", "1.3"))

        # "MacInnes is the one who betrayed Dur[nk]and."
        # [nk]Highlight MacInnes in red and Ferrara in green
        self.wait_until(23, 15, 240)
        self.play(self.frame_cards("MacInnes", "Durand", "Ferrara"))
        self.play(
            self.highlight_card("MacInnes"), self.highlight_card("Ferrara", mm.GREEN_C)
        )

        # "not just on the past but the present too,[nl]"
        # [nl]Pan to present part of diagram
        self.wait_until(23, 27, 840)
        self.play(
            self.frame_cards("Jen", "Eric", "Moody", "Ilsa", "Caldeira", "Desjardins")
        )

        # "Professor Moody has been receiving funding[nm][nn] from the MacInnes Foundation "
        # [nm]Link Moody to MacInnes (may rejig diagram)
        self.prepare_link("Moody", "MacInnes")
        self.prepare_link("MacInnes", "Caldeira")
        self.prepare_link("Summersby", "VMS")
        self.calculate_layout(esep=0.06)
        self.wait_until(23, 31, 600)
        self.frame_cards()
        self.play(
            # self.frame_cards("Moody", "MacInnes", "Jen", "Eric"),
            self.animate_update_layout(),
            self.add_link("MacInnes", "Moody", from_point=self.layouts[-2][0]["Moody"]),
            run_time=3,
        )
        # [nn]From now on, use Moody 1.4 if zooming
        self.set_slide("Moody", "1.4")

        # "him more about her interactions with MacInnes. [no]"
        # [no]link MacInness and Caldeira
        self.wait_until(23, 41, 820)
        self.play(self.add_link("MacInnes", "Caldeira"))

        # "a trick he tried on both FXC and Durand[np] to poor results."
        # [np]Highlight MacInnes links to Caldeira and Durand
        self.wait_until(23, 50, 840)
        self.play(self.pan_to("Caldeira"))

        self.wait_until(23, 51, 500)
        self.play(self.pan_to("Durand"))

        # "why did MacInnes not know how to contact Straka himself?"
        # [ns]Go back to diagram
        self.wait_until(24, 23, 320)
        self.play(self.pan_to("MacInnes"))

        # "his true identity were the original members[nt]"
        # [nt]Highlight original members (or card that says original S)
        self.wait_until(24, 32, 580)
        ORIGINAL_S = ["VMS", "Ekstrom", "Durand", "Feuerbach", "Ferrara"]
        self.play(
            self.frame_cards(*ORIGINAL_S),
        )
        self.play(
            self.highlight_card("VMS"),
            *[self.highlight_card(c, color=mm.BLUE_C) for c in ORIGINAL_S],
            self.highlight_card("S_Org", color=mm.BLUE_C),
            *[self.highlight_link(c, "S_Org", color=mm.BLUE_E) for c in ORIGINAL_S],
            self.unhighlight_card("MacInnes"),
        )

        # "however Jen mentions that Summersby[nu]"
        # [nu]Link Summersby and Straka or highlight Summersby
        self.wait_until(24, 35, 440)
        self.play(self.frame_cards("Summersby", "VMS"))
        self.play(
            self.add_link("Summersby", "VMS"),
            *[self.unhighlight_card(c) for c in ORIGINAL_S],
            self.unhighlight_card("S_Org"),
            *[self.unhighlight_link(c, "S_Org") for c in ORIGINAL_S],
        )

        # "her the Summersby tape[nv]"
        # [nv]Zoom to tape card 1.5
        self.wait_until(24, 48, 720)
        self.set_slide("Sum_Tape", "1.5")
        self.play(self.fully_zoom_card("Sum_Tape"))

        # "sidelined member of the S: Horst Wechsler.[nw]"
        # [nw]Pan over to Horst, zoom on wechsler 1.1
        self.wait_until(24, 58, 980)
        self.play(self.frame_cards("Wechsler", margin=3))
        self.play(self.fully_zoom_card("Wechsler"))

        # " there is a man called Gernot Klein who looks exactly like Wechsler."
        # [ob]Link Weschler and Arp.
        self.wait_until(25, 44, 920)
        self.play(self.frame_cards("Wechsler", "Arp"))
        self.play(self.add_link("Wechsler", "Arp"))

        # (If need to show Arp again, remember to add add quote from Jen or bullet point)

        # "Did Wechsler leave Dublin because he knew Feuerbach[oc] was going to be targeted?"
        # [oc]Zoom on Wechsler card 1.2
        self.wait_until(25, 47, 600)
        self.set_slide("Wechsler", "1.2")
        self.play(self.fully_zoom_card("Wechsler"))

        # "The answer seems to be for money and success.[od]"
        # [od]Switch to wechsler 1.3
        self.wait_until(25, 54, 300)
        self.play(self.change_slide("Wechsler", "1.3"))

        # "Perhaps this was Weschler,[of]"
        # [of]Back to Wechsler 1.4
        self.wait_until(26, 26, 240)
        self.play(self.change_slide("Wechsler", "1.4"))

        # "at Arp he had power and influence and respec[og]"
        # [og]Zoom out, highlight Wechsler/Arp and Weschler/S org
        self.wait_until(26, 32, 20)
        self.play(
            self.frame_cards("Wechsler", "Arp", "S_Org"),
            self.highlight_link("Wechsler", "Feuerbach", color=mm.BLUE_E),
            self.highlight_link("Wechsler", "Arp"),
        )

        self.prepare_link("Caldeira", "Desjardins")
        self.prepare_link("Signe", "Durand")
        self.prepare_link("Desjardins", "Signe")
        self.prepare_link("Signe", "Summersby")
        self.prepare_link("Signe", "Ekstrom")
        self.prepare_link("Summersby", "Signe")
        self.prepare_link("VMS", "Signe")
        self.calculate_layout()
        # "our old friend Desjardins. [om]"
        # [om]Zoom to Dejardins card 1.3
        self.wait_until(27, 55, 400)
        self.play(
            self.frame_cards("Desjardins", margin=3),
            self.animate_update_layout(),
            run_time=3,
        )
        self.set_slide("Desjardins", "1.3")
        self.play(
            self.fully_zoom_card("Desjardins"),
            self.unhighlight_link("Wechsler", "Feuerbach"),
            self.unhighlight_link("Wechsler", "Arp"),
        )

        # " woman [op]called Signe Rabe in Carcassonne in 1952."
        # [op]New Signe Rabe card emerges from Dejardins, zoom on Signe 1.1
        self.wait_until(28, 17, 980)
        self.play(self.frame_cards("Desjardins", "Signe"))
        self.play(
            self.add_card_from("Desjardins", "Signe"),
            self.frame_cards("Desjardins", "Signe"),
        )
        self.play(self.fully_zoom_card("Signe"))

        # "Signe’s date of birth is listed as 4th Nov 1930 a"
        # [or]Cut back to Signe card 1.2
        self.wait_until(28, 34, 580)
        self.play(self.change_slide("Signe", "1.2"))

        # "So logic dictates A. Rabe is Amarante Durand[ot] and Signe is Durand’s daughter.[ou]"
        # [ot]Switch to Signe 1.3
        self.wait_until(28, 44, 660)
        self.play(self.change_slide("Signe", "1.3"))

        # "and Signe is Durand’s daughter.[ou]"
        # [ou]Zoom out, link Signe to Durand and Ekstrom
        self.wait_until(28, 47, 940)
        self.play(
            self.frame_cards("Signe", "Durand"),
            self.add_link("Signe", "Durand"),
            self.add_link("Ekstrom", "Signe"),
        )

        # "Weeping with joy to see his daughter an[ox]d surrogate son together perhaps."
        # [ox]Back to diagram, pan to Signe then Vaclav
        self.wait_until(29, 8, 960)
        self.play(self.pan_to("Signe"))
        self.play(self.pan_to("VMS"))

        # "and she says s[pc]he only knew the name b"
        # [pc]Show Caldeira, MacInnes, Durand and Bouchard
        self.wait_until(29, 27, 140)
        self.frame_cards("Caldeira", "MacInnes", "Durand", "Bouchard")

        # "FXC did meet Desjardins.[pd]"
        # [pd]Zoom out, link FXC to Desjardins
        self.wait_until(29, 45, 660)
        self.frame_cards("Caldeira", "Desjardins")
        self.play(self.add_link("Caldeira", "Desjardins"))

        # "Turns out Signe[pf] died in 1956 after a long illness,"
        # [pf]Pan back to Signe and zoom on Signe 1.4
        self.wait_until(30, 1, 200)
        self.play(self.frame_cards("Signe", margin=2))
        self.set_slide("Signe", "1.4")
        self.play(self.fully_zoom_card("Signe"))

        # "This tragedy adds to[pg] Desjardins’ motivations and could explain w"
        # [pg]Zoom out to whole diagram
        self.wait_until(30, 4, 500)
        self.play(self.frame_cards(*MODERN_DAY_CARDS, "MacInnes"), run_time=4)

        # "why he fell out with Moody[ph]"
        # [ph]Highlight connection between Moody and Des (or circle M)
        self.wait_until(30, 9, 0)
        self.play(self.pan_to("Moody"), self.highlight_link("Desjardins", "Moody"))

        # "started getting funding from MacInnes,[pi]"
        # [pi]Highlight connection between Moody and Mac (or circle M)
        self.wait_until(30, 11, 180)
        self.play(self.pan_to("MacInnes"), self.highlight_link("Moody", "MacInnes"))

        # "the guy who orphaned Signe"
        # deleted this one, double check..
        self.wait_until(30, 13, 180)
        self.play(self.pan_to("Signe"), self.highlight_link("Signe", "Durand"))

        # " Hence Desjardins knew he could trust Eric[pk]"
        # [pk]Highlight connection between Des and Eric, or zoom into Des and highlight bullet point "sent Eric obsidian piece"
        self.wait_until(30, 19, 440)
        self.play(
            self.frame_cards("Desjardins", "Eric"),
            self.highlight_link("Desjardins", "Eric", mm.BLUE_C),
        )

        # "Back to Signe though[pl]"
        # [pl]Pan back to Signe 1.5
        self.wait_until(30, 26, 60)
        self.play(self.pan_to("Signe"))
        self.play(self.fully_zoom_card("Signe"))

        # "one of these “uncles” must have been Summersby.[pn]"
        # [pn]Zoom out, link Sum to Sig
        self.wait_until(30, 45, 980)
        self.play(self.frame_cards("Summersby", "Signe"))
        self.play(self.add_link("Summersby", "Signe"))

        # "we think the other is Vaclav. [po]"
        # [po]Link Sig to Vaclav
        self.wait_until(30, 49, 680)
        self.play(self.frame_cards("Signe", "Summersby", "VMS"))
        self.play(self.add_link("Signe", "VMS"))

        # "Firstly, when recording his tape, [pp]"
        # [pp]Zoom in on tape card 1.6
        self.wait_until(31, 6, 0)
        self.set_slide("Sum_Tape", "1.6")
        self.play(self.fully_zoom_card("Sum_Tape"))

        # "(Summersby is absolutely the best S member, for the record)[pq]"
        # [pq]Add bullet point (or crown haha)
        self.wait_until(31, 18, 980)
        self.play(self.frame_cards("Summersby", margin=3))

        # "to postpone meeting with Caldeira.[pr]"
        # [pr]Pan to show Vaclav and Caldeira
        self.wait_until(31, 26, 840)
        self.play(self.frame_cards("Caldeira", "VMS"))

        # "he and Vaclav swore secrecy[ps]"
        # [ps]Link Vaclav and Summersby strongly
        self.wait_until(31, 36, 680)
        self.play(
            self.frame_cards("VMS", "Summersby"), self.add_link("VMS", "Summersby")
        )

        # [pt]Pan to Signe
        # another one I accidentally deleted
        self.wait_until(31, 39, 820)
        self.play(self.pan_to("Signe"))
        if not self.skip_animations:
            self.play(
                self.camera.frame.animate.scale_to_fit_width(
                    self.g.cards["Signe"].width + 0.2
                ),
                run_time=4,
            )

        # "We are coming to the end of this section[pu]"
        # [pu]Zoom out to show whole diagram
        self.wait_until(31, 48, 840)
        self.play(self.frame_cards(), run_time=6)

        # "Did Straka really die in Havana?[pw]"
        # [pw]Zoom on VMS 2.2
        self.wait_until(32, 11, 260)
        self.set_slide("VMS", "2.2")
        self.play(self.fully_zoom_card("VMS"))

        # "but there’s essentially no evidence[px] that he didn’t"
        # [px]Switch to VMS 2.3
        self.wait_until(32, 17, 20)
        self.play(self.change_slide("VMS", "2.3"))

        # "lines up with all other S-related deaths[py]"
        # [py]Zoom out to highlight all mysterious death victims
        self.wait_until(32, 21, 400)
        self.play(self.frame_cards(*ORIGINAL_S))

        # ================================================================
        # SECTION 4 — Ship of Theseus, The Novel
        # Card-diagram shots only. Live-action, on-screen quotes, the
        # Caldeira-vs-Straka / key-events tables, timeline highlights and
        # the side-by-side drawing montages are all handled elsewhere and
        # deliberately omitted here. No time-sync: shots run back-to-back.
        # The full diagram is already live from the end of section 3;
        # "Vaclav" is now the VMS card (merged above).
        # ================================================================
        def section4():
            # "we have to explore what Ship of Theseus tells us about its author"
            # PLAN: Show full diagram
            self.play(self.frame_cards())
            self.wait(1)

            # "SoT was somewhat inspired by events and people in Vaclav's real life"
            # PLAN: Can show diagram again
            self.play(self.frame_cards())
            self.wait(1)

            # "S's journey from nobody to the influential assassin ... the S organisation"
            # PLAN: Show S org on diagram
            # move from Vaclav and Caldeira to Vaclax zoom, then fade from
            self.play(self.frame_cards("VMS", "Ekstrom", "Durand"))
            self.wait(1)

            # "the companionship and admiration S comes to feel for ... Ekstrom and Durand"
            # PLAN: Highlight connections on diagram, then stay on Durand/Vaclav's
            self.play(
                self.highlight_link("S_Org", "Ekstrom", color=mm.GREEN_E),
                self.highlight_link("S_Org", "Durand", color=mm.GREEN_E),
                self.highlight_link("S_Org", "VMS", color=mm.GREEN_E),
            )
            self.wait(1)
            self.play(
                self.unhighlight_link("S_Org", "Ekstrom"),
                self.highlight_link("S_Org", "Durand", color=mm.PINK),
                self.highlight_link("S_Org", "VMS", color=mm.PINK),
            )
            self.wait(1)
            self.play(
                self.unhighlight_link("S_Org", "Ekstrom"),
                self.unhighlight_link("S_Org", "Durand"),
                self.unhighlight_link("S_Org", "VMS"),
            )
            self.wait(1)

            # "it seems almost spiritual ... the ship's customs de-emphasise individualism"
            # PLAN: Show S org in diagram, highlight
            self.play(
                self.frame_cards("S_Org", margin=3),
                self.highlight_card("S_Org", color=mm.BLUE_E),
            )
            self.wait(1)
            self.play(self.unhighlight_card("S_Org"))
            self.wait(1)

            # "the S has this kind of larger-scale legacy as a continuous composite organisation"
            # PLAN: Show full diagram
            self.play(self.frame_cards())
            self.wait(1)

            # "Vevoda starts out as a psychopathic businessman ... Hermes Bouchard"
            # PLAN: Show Bouchard drawing
            self.play(self.fully_zoom_card("Bouchard"))
            self.wait(1)

            # "it's implied the 'new S' is a continuation too ... still directly linked to Bouchard"
            # PLAN: Link Mysterious men to Bouchard on diagram (or circle both)
            self.play(
                self.frame_cards("Myst_Men", "Bouchard"),
            )
            self.wait(1)
            self.prepare_link("Myst_Men", "Bouchard")
            self.calculate_layout()
            self.play(self.animate_update_layout(), run_time=3)
            self.wait(1)
            self.play(self.add_link("Myst_Men", "Bouchard"))
            self.wait(1)

            # "Moody is the new MacInnes, selling out academic integrity for money"
            # PLAN: Highlight Moody and MacInnes link in red on diagram
            self.play(
                self.frame_cards("Moody", "MacInnes"),
                self.highlight_link("Moody", "MacInnes", color=mm.PURE_RED),
            )
            self.wait(1)
            self.play(self.unhighlight_link("Moody", "MacInnes"))
            self.wait(1)

            # "Back to the characterisation of Vaclav" (the VMS card now stands in for Vaclav)
            # PLAN: Vaclav old drawing
            self.play(self.fully_zoom_card("VMS"))
            self.wait(1)

            # "Stenfalk's death clearly weighs on his conscience"
            # PLAN: Add Ekstrom drawing next to Vaclav
            self.play(self.frame_cards("VMS", "Ekstrom"))
            self.wait(1)

            # "the sheet of paper with strange anagrams ... What if Vaclav and Ekstrom were meeting"
            # PLAN: Show Ekstrom 1.5
            self.set_slide("Ekstrom", "1.5")
            self.play(self.fully_zoom_card("Ekstrom"))
            self.wait(1)

            # "S also feels hugely guilty about all the subsequent people he failed to save"
            # PLAN: Show full diagram with all relevant parties
            self.play(self.frame_cards())
            self.wait(1)

            # "changed to Pfeifer later by Caldeira ... point blame at someone like Weschler or MacInnes"
            # PLAN: Show Weschler and MacInnes on diagram
            self.play(
                self.frame_cards("Wechsler", "MacInnes"),
                self.highlight_card("Wechsler"),
                self.highlight_card("MacInnes"),
            )
            self.wait(1)

            # "his depression and resignation to futility reaches a peak in the Winter City"
            # PLAN: Show Vaclav drawing (winter-city background added elsewhere)
            self.play(
                self.unhighlight_card("Wechsler"),
                self.unhighlight_card("MacInnes"),
                self.fully_zoom_card("VMS"),
            )
            self.wait(1)

        section4()

        # ================================================================
        # SECTION 5 — Part O' The Tradition (speculative history)
        # Card-diagram shots only, back-to-back, no time-sync.
        # ================================================================
        def section5():
            # "we're going to be generous and try our best to make up a story that ties it all together"
            # "Sometime in the late 16th / early 17th century there lived Arquimedes de Sobreiro"
            # PLAN: Make the whole diagram disappear except Sobreiro, then fill people
            #       back in as they are named. Zoom on Sobreiro 1.1.
            self.set_slide("Sobreiro", "1.1")
            self.play(
                self.frame_cards("Sobreiro", margin=10)
            )  # dim everything but Sobreiro
            self.play(self.opacity_except("Sobreiro"), run_time=2)
            self.wait(1)
            self.play(self.fully_zoom_card("Sobreiro"))
            self.wait(1)
            # TODO: choreograph fading each card back in as it is mentioned below,
            #       rather than the single blanket restore used here for now.

            # "He gathered a 'crew as a composite of traditions'"
            # PLAN: Switch to Sobreiro 1.2
            self.play(self.change_slide("Sobreiro", "1.2"))
            self.wait(1)

            # "some descendent followers of Sobreiro continued to preserve his tradition"
            # PLAN: Zoom out slowly, pan to S org (not zoomed)
            self.play(
                self.opacity_except(opacity=1)
            )  # (diagram progressively restored)
            self.wait(1)
            self.play(self.frame_cards("S_Org", margin=4), run_time=4)
            self.wait(1)

            # "Nineteen obsidian pieces for nineteen original crew members"
            # PLAN: Pan to Artefacts
            self.play(self.pan_to("Artefacts"))
            self.wait(1)

            # "though the archer himself was dead, The Archer's Tales kept his philosophy alive"
            # PLAN: Show Sobreiro 1.3
            self.play(self.fully_zoom_card("Sobreiro"))
            self.play(self.change_slide("Sobreiro", "1.3"))
            self.wait(1)

            # "Until of course, the S organisation of Ekstrom, Durand, Feuerbach, Ferrara, and Straka"
            # PLAN: Zoom into S org 1.4
            self.set_slide("S_Org", "1.4")
            self.play(self.fully_zoom_card("S_Org"))
            self.wait(1)

            # "They adopted his symbol"
            # PLAN: Switch to S org 1.5
            self.play(self.change_slide("S_Org", "1.5"))
            self.wait(1)

            # "shared his predilection for Birds, and ... fought for his cause of anarchy and freedom"
            # PLAN: Switch to S org 1.6
            self.play(self.change_slide("S_Org", "1.6"))
            self.wait(1)

            # "passed down ... to the family of Torsten Ekstrom ... when Durand discovered her cave paintings"
            # PLAN: Show Durand and Ekstrom on diagram, then zoom out to show all those linked to the S
            self.play(self.frame_cards("Durand", "Ekstrom"))
            self.wait(1)
            self.prepare_link("Caldeira", "Sobreiro")
            self.prepare_link("S_Org", "Sobreiro")
            self.play(self.frame_cards())
            self.calculate_layout()
            self.play(self.animate_update_layout(), run_time=3)
            self.wait(1)
            self.play(
                self.add_link("S_Org", "Sobreiro"),
                self.frame_cards("S_Org", "Durand", "Ekstrom", "Sobreiro", "VMS"),
            )
            self.wait(1)

            # "Is it possible that F.X. Caldeira possessed another copy of the Archer's Tales?"
            # PLAN: Connect Caldeira to Sobreiro on diagram (or draw on top)
            self.play(self.frame_cards("Caldeira", "Sobreiro", margin=5))
            self.play(self.animate_update_layout(), run_time=3)
            self.wait(1)
            self.play(self.add_link("Caldeira", "Sobreiro", width=12))
            self.wait(1)

            # "we can assume that Ekstrom's copy was kept safe by Straka and Summersby after Ekstrom's death"
            # PLAN: Highlight Ekstrom, then Straka and Summersby
            self.play(self.highlight_card("Ekstrom", width=8, color=mm.BLUE_E))
            self.play(
                self.highlight_card("Summersby", width=8, color=mm.BLUE_E),
                self.highlight_card("VMS", width=8, color=mm.BLUE_E),
            )
            self.wait(0.5)
            self.play(
                *[self.unhighlight_card(c) for c in ["Ekstrom", "Summersby", "VMS"]]
            )

            # "the Archer's Tales would connect him to both his place in the S and his hope with Caldeira"
            # PLAN: Highlight connections to use as a (blurred) background
            self.play(
                self.opacity_except(
                    "Caldeira",
                    "Sobreiro",
                    "VMS",
                    "Artefacts",
                    edges=[("Caldeira", "Sobreiro")],
                )
            )
            self.wait(1)
            self.play(
                self.opacity_except(opacity=1),
                self.unhighlight_link("Caldeira", "Sobreiro"),
            )
            self.wait(1)

            # "until it is stolen during the yellow/green phase ... We're guessing Moody sent Ilsa"
            # PLAN: Zoom on Ilsa card 1.4
            self.set_slide("Ilsa", "1.4")
            self.play(self.fully_zoom_card("Ilsa"))
            self.wait(1)

            # "she felt guilty after his death, the final straw for her relationship with Moody"
            # PLAN: Show Ilsa and Moody connection disappeared / crossed over
            self.play(self.frame_cards("Ilsa", "Moody"))
            self.wait(1)
            self.play(self.g.links[("Moody", "Ilsa")].animate.set_opacity(0))
            self.wait(1)

            # "Who are Serin? Who are the mysterious men ... stalking Jen and Eric?"
            # PLAN: Pan to each on diagram
            self.play(self.pan_to("Serin"), self.highlight_card("Serin", width=8))
            self.wait(1)
            self.play(self.pan_to("Myst_Men"), self.highlight_card("Myst_Men", width=8))
            self.wait(1)
            self.play(self.unhighlight_card("Serin"), self.unhighlight_card("Myst_Men"))

            # "Signe Rabe married Jean-Bernard Desjardins, and they started a new version of the S ... 'Serin'"
            # PLAN: Connect Des and Sig to the S, then link the S to Serin
            self.prepare_link("Desjardins", "Serin")
            self.prepare_link("Signe", "Serin")
            self.prepare_link("S_Org", "Serin")
            self.calculate_layout()
            self.play(
                self.frame_cards("Desjardins", "Signe", "S_Org", "Serin", margin=5)
            )
            self.play(self.animate_update_layout(), run_time=5)
            self.wait(1)
            self.play(
                self.add_link("Desjardins", "Serin"),
                self.add_link("Signe", "Serin"),
            )
            self.wait(1)
            self.play(self.add_link("S_Org", "Serin"))
            self.wait(1)

            # "They have the archer's tales, and the ongoing royalties to Straka's books"
            # PLAN: Highlight Desjardins and signe connection to S Org and S Org to Sobreiro and S Org to Straka
            self.play(
                self.opacity_except(
                    "Desjardins", "Signe", "Serin", "Sobreiro", "S_Org", "VMS"
                )
            )
            self.play(
                self.highlight_link("Desjardins", "Serin", color=mm.BLUE_E, width=12),
                self.highlight_link("Signe", "Serin", color=mm.BLUE_E, width=12),
                self.highlight_link("S_Org", "Sobreiro", color=mm.BLUE_E, width=12),
                self.highlight_link("Serin", "S_Org", color=mm.BLUE_E, width=12),
            )

            self.wait(0.5)
            self.play(self.highlight_link("S_Org", "VMS", color=mm.GREEN_E, width=12))

            self.wait(1)
            self.play(
                self.opacity_except(opacity=1),
                *[
                    self.unhighlight_link(*l)
                    for l in [
                        ("Desjardins", "Serin"),
                        ("Signe", "Serin"),
                        ("S_Org", "Sobreiro"),
                        ("VMS", "S_Org"),
                        ("S_Org", "Serin"),
                    ]
                ],
            )

            # "Bouchard meanwhile had plenty of traitors from the original S (MacInnes, Looper, Weschler)"
            # PLAN: Pan to the three traitors on diagram
            self.play(
                self.frame_cards("Bouchard", margin=5),
                self.highlight_card("Bouchard", width=8),
            )
            self.play(
                self.frame_cards("MacInnes", "Looper", "Wechsler", "Bouchard"),
            )
            self.play(
                self.camera.frame.animate.shift((mm.LEFT + mm.DOWN) * 0.5),
                self.highlight_card("MacInnes", width=8),
                run_time=0.5,
            )
            self.play(
                self.camera.frame.animate.shift((mm.RIGHT) * 0.5),
                self.highlight_card("Looper", width=8),
                run_time=0.5,
            )
            self.play(
                self.camera.frame.animate.shift((mm.UP) * 0.5),
                self.highlight_card("Wechsler", width=8),
                run_time=0.5,
            )

            self.wait(1)
            self.play(
                *[
                    self.unhighlight_card(c)
                    for c in ["MacInnes", "Looper", "Wechsler", "Bouchard"]
                ],
            )

            # "All of this ... the birds and the wolves, is cyclical"
            # PLAN: Show diagram (birds & wolves sketch handled elsewhere)
            self.starth()
            self.play(self.frame_cards())
            self.wait(1)

            # "the present Straka and Caldeira, Durand and Ekstrom, Sola and Sobreiro ... Jen and Eric"
            # PLAN: Show diagram, move from Vaclav and Caldeira up to Jen and Eric

            self.play(self.frame_cards("VMS", "Caldeira", margin=5))
            self.play(
                self.highlight_link("VMS", "Caldeira", color=mm.PINK),
                self.opacity_except("VMS", "Caldeira", "Jen", "Eric"),
            )
            self.play(
                self.frame_cards("Jen", "Eric"),
                self.highlight_link("Jen", "Eric", color=mm.PINK),
                run_time=3,
            )
            self.wait(1)
            self.play(
                self.opacity_except(opacity=1),
                self.unhighlight_link("Jen", "Eric"),
                self.unhighlight_link("VMS", "Caldeira"),
            )
            self.endh()

            # ---- Section 6 (Final thoughts): single diagram beat ----
            # "there's a huge amount you can get to with ... effort, and then more with speculation"
            # PLAN: Show diagram focusing on S org, then pan to Sobreiro side
            self.play(self.fully_zoom_card("S_Org"))
            self.play(self.frame_cards("S_Org", margin=14), run_time=10)
            self.wait(1)
            self.play(self.pan_to("Sobreiro"), run_time=3)
            self.wait(1)
            self.endh()

        section5()
