from manim import *
from graph import *


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
        self.next_section(skip_animations=True)
        self.skip_animations = False
        # self.starth()
        self.initialise_layout()
        self.camera.frame.move_to(self.bounding_box())
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

        sec_2_cards = self.nodes.copy()
        remove_edges = [
            ("Caldeira", "Eric"),
            ("Eric", "Desjardins"),
            ("Eric", "Artefacts"),
        ]

        for r in remove_edges:
            self.unprepare_link(*r)

        self.prepare_link("Ekstrom", "Durand")
        self.prepare_link("S_Org", "VMS")
        self.prepare_link("S_Org", "Ekstrom")
        self.prepare_link("Sum_Tape", "Ekstrom")
        self.prepare_link("Wechsler", "Feuerbach")
        self.prepare_link("Durand", "Ferrara")
        # self.prepare_link("Feuerbach", "S_Org")
        self.prepare_link("Summersby", "Caldeira")
        # self.prepare_link("Summersby", "S_Org")
        self.prepare_link("Summersby", "Sum_Tape")
        # self.prepare_link("MacInnes", "S_Org")
        self.prepare_link("Wechsler", "Durand")
        self.prepare_link("Wechsler", "Ferrara")
        self.prepare_link("Feuerbach", "Durand")
        self.prepare_link("Feuerbach", "Ferrara")
        self.prepare_link("Summersby", "Ekstrom")
        self.prepare_link("S_Org", "MacInnes")
        self.prepare_link("S_Org", "Vaclav")
        self.prepare_link("Vaclav", "Bridge_Jump")

        # "it's time to talk about the S organisation"
        # Create and show S org card 1.1
        self.wait_until(1, 26, 700)

        self.calculate_layout(prev=True)
        self.play(self.frame_cards(*sec_2_cards))

        print(self.nodes)
        self.play(
            self.animate_update_layout(),
            # *[self.remove_link(*r) for r in remove_edges],
        )
        self.play(self.frame_cards("S_Org", margin=4), self.add_card("S_Org"))
        self.play(self.fully_zoom_card("S_Org"))

        # "some suspects are clearly the basis for a group of characters featured in SoT."
        # Show S org 1.2
        self.wait_until(1, 39, 0)
        self.play(self.change_slide("S_Org", "1.2"))

        # "First, the oldest of the bunch: Torsten Ekstrom"
        # Create and zoom on Ekstrom 1.1
        self.wait_until(1, 58, 720)
        self.play(self.frame_cards("S_Org", "Ekstrom"), self.add_card("Ekstrom"))
        self.play(self.fully_zoom_card("Ekstrom"))

        # "in the Summersby tape"
        # Show Sum_tape and Ekstrom linking (Summersby tape 1.4 used from now on)
        self.wait_until(2, 8, 80)
        self.play(
            self.frame_cards("Ekstrom", "Sum_Tape"),
            self.add_link("Ekstrom", "Sum_Tape"),
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
        self.play(self.change_slide("Durand", "1.2"))

        # "Her and Ekstrom’s character analogues"
        # Link to Ekstrom, then zoom back in on 1.2
        self.wait_until(3, 3, 780)
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
            self.frame_cards("Ferrara", "Durand"), self.add_link("Ferrara", "Durand")
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

        self.play(self.add_card("Bridge_Jump"), self.add_link("Vaclav", "Bridge_Jump"))

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
            self.clear_circles(), self.highlight_link("Durand", "Ekstrom", color=BLUE_C)
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
            self.add_link("Feuerbach", "Durand"), self.add_link("Feuerbach", "Ferrara")
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

        self.starth()

        # "So all these individual ties further the idea that the candidates worked together.[km]"
        # [km]Reshuffle diagram so the candidates are all connected to the S organisation rather than each other. But leave Durand/ekstrom and durand/ferrara
        self.wait_until(12, 19, 0)
        self.prepare_link("Ekstrom", "S_Org")
        self.prepare_link("Summersby", "S_Org")
        self.prepare_link("Durand", "S_Org")
        self.prepare_link("Feuerbach", "S_Org")
        self.prepare_link("Ferrara", "S_Org")
        self.prepare_link("Summersby", "S_Org")
        remove_edges = [
            ("Ekstrom", "Durand"),
            ("Durand", "Ferrara"),
            ("Wechsler", "Durand"),
            ("Wechsler", "Ferrara"),
            ("Feuerbach", "Durand"),
            ("Feuerbach", "Ferrara"),
            ("Summersby", "Ekstrom"),
        ]

        self.calculate_layout()
        self.play(
            self.frame_cards(
                "Ekstrom", "Durand", "Feuerbach", "Ferrara", "Wechsler", "Summersby"
            )
        )
        self.play(
            self.animate_update_layout(),
            *[self.remove_link(*r) for r in remove_edges],
        )
        # "because that doesn’t identify who Caldeira’s Straka was[kn]"
        # [kn]Zoom on Caldeira and Straka

        # "V. Finch is probably Summersby[kr]"
        # [ks]Link Sum with S_org in background

        # "why exactly does VMS need to stay secret anyway[ku]"
        # [ku]Zoom back on VMS card 1.4

        # "Re-introducing Hermes Bouchard:[kv]"
        # [kv]Create and zoom on Bouchard 1.1

        # "Re-introducing Hermes Bouchard:[kv]"
        # [kw]Switch to Bouchard 1.2

        # "So here’s the issue[kx]"
        # [kx]Pan to Prix Bouchard card 1.1, switch to 1.2

        # "Caldeira claims [ky]it was an accusation towards Bouchard."
        # [ky]Switch to 1.3

        # "deaths of syndicalist agitators and was behind a recent massacre [kz]of factory workers in Calais."
        # [kz]Create Calais massacre card and link to Bouchard and Prix Bouchard

        # "This is described by FXC in Chapter 4:[la]"
        # [la]Zoom into Calais card but fade to drawing of massacre (or other image) with quote appearing on top. Then at end of quote, fade back into actual Calais card

        # "Eric says Straka’s note ["
        # [lb]Pan to Prix Bouchard 1.4

        # "disappeared in 1983, and quotes it[lc]: "You seek a world populated by trick monkeys who dance to your tunes for the empty promise of coins""
        # [lc]Switch to Prix 1.5

        # " Jen and FXC[ld] both seem to agree that this accusation d"
        # [ld]Switch to Prix 1.6

        # "she confirmed that "Everything goes back to Calais"."
        # [le]Pan to Calais 1.2

        # "likely[lf] suspect for the Santorini man murders."
        # [lf]Link Bouchard card to Santorini man murders

        # "This was at least Desjardins’ theory.[lg]"
        # [lg]Could circle Dejardins (or not, for easy)

        # "But how exactly would Bouchard have that much influence if his company ended?[lh]"
        # [lh]Zoom back to Bouchard card 1.3

        # "to spawn and control a bunch of shell companies["
        # [li]Switch to Bouchard 1.4

        # "manufacturer called Arp Syndikat.[lj]"
        # [lj]Create Arp card from Bouchard and zoom on arp 1.1

        # "In SoT itself, the Bouchard stand-in ("
        # [lk]ARP 1.2

        # "Hermes Bouchard had a son[lp]"
        # [lp]Zoom on Bouchard 1.5

        # "interview about Vaclav Straka’s death[lq]"
        # [lq]Circle Prague jump and feuerbach

        # "This is therefore huge - [lt]the earliest and only record w"
        # [lt]Move back to diagram, zoom on group as a whole if possible, connect S org to Prague bridge jump

        # "except an alive Vaclav Straka?[lu]"
        # [lu]Connect Vaclav card to S organisation

        # [lv]Possible reconfig

        # "His candidacy [lw]now works on multiple levels."
        # [lw]Zoom on Vaclav card 1.6

        # For context:[lx] the first four chapters consist of an unnamed protagonist being reborn from a river, meeting a group who share names with the birds in this hotel register, and witnessing a massacre of striking workers organised by an evil factory owner.
        # [lx]Pan towards bridge jump, then over S org group, then over Calais massacre. Don't need to totally zoom in, want to get picture of how all connected.

        # "best option for Caldeira, which she herself admits to Eric[ly]"
        # [ly]Either show quote, pan to Caldeira card, or stay on Vaclav for easiest

        # "Vaclav was “holding his manuscript when he jumped"[lz]"
        # [lz]Go to Vaclav 1.7

        # "One of the few things we know about Ekstrom is that he was a great swimmer at university.[ma]"
        # [ma]Zoom in on Ekstrom 1.5

        # "Then he and Durand[mc]"
        # [mc]Zoom out to show both E and D

        # "timeline: Durand and Ekstrom[me]"
        # [me]Pan to above Durand and ekstrom (but not fully in), then Vaclav

        # "like-minded friends[mf]"
        # [mf]Circle group OR just show in pan

        # "use Vaclav’s anonymity to make political statements they otherwise couldn’t.[mg]"
        # [mg]Make Vaclav replace Straka. (replace VMS card with title 2)

        # "were at the Calais massacre, and Chapter 3 of SoT suggests that Vaclav himself could have been[mh]"
        # [mh]Show connection between V and Mas

        # "As to why Vaclav went [mj]along with all this, who knows?"
        # [mj]Zoom in on VMS 2.1

        # "Here’s the rub though: this is all really speculation[mn]"
        # [mn]Show whole diagram

        # "MacInnes and Summersby[mr] are probably the two most i"
        # [mr]Link MacInnes to S org card, highlight him and Summersby

        # "Singh[mt][mu] is the only relevant one,"
        # [mu]Make card in background

        # "Although this all seems to be going swimmingly[my]"
        # [my]Show whole diagram

        # "the S must have fallen apart[mz] at some point."
        # [mz]Show S org card 1.3

        # "sold out the original group. [nc]"
        # [nc]When we cut back to card before zooming out, show S_org 1.4

        # "this is a reference to the Ferrara-Durand betrayal[nd]"
        # [nd]Pan to show both)

        # "Jen and Eric specifically mention MacInnes[ne]"
        # [ne]Pan to MacInnes

        # "Here’s where Caldeira’s ciphers [nf]"
        # [nf]Pan to Caldeira

        # "Jen and Eric say Looper split from the S in 1926[nh]"
        # [nh]Cut to Looper card 1.2

        # "But to complicate matters further,[ni]"
        # [ni]Switch to Looper 1.3

        # "MacInnes is the one who betrayed Dur[nk]and."
        # [nk]Highlight MacInnes in red and Ferrara in green

        # "not just on the past but the present too,[nl]"
        # [nl]Pan to present part of diagram

        # "Professor Moody has been receiving funding[nm][nn] from the MacInnes Foundation "
        # [nm]Link Moody to MacInnes (may rejig diagram)

        # [nn]From now on, use Moody 1.4 if zooming

        # "him more about her interactions with MacInnes. [no]"
        # [no]link MacInness and Caldeira

        # "a trick he tried on both FXC and Durand[np] to poor results."
        # [np]Highlight MacInnes links to Caldeira and Durand

        # "why did MacInnes not know how to contact Straka himself?"
        # [ns]Go back to diagram

        # "his true identity were the original members[nt]"
        # [nt]Highlight original members (or card that says original S)

        # "however Jen mentions that Summersby[nu]"
        # [nu]Link Summersby and Straka or highlight Summersby

        # "her the Summersby tape[nv]"
        # [nv]Zoom to tape card 1.5

        # "sidelined member of the S: Horst Wechsler.[nw]"
        # [nw]Pan over to Horst, zoom on wechsler 1.1

        # " there is a man called Gernot Klein who looks exactly like Wechsler."
        # [ob]Link Weschler and Arp.

        # (If need to show Arp again, remember to add add quote from Jen or bullet point)

        # "Did Wechsler leave Dublin because he knew Feuerbach[oc] was going to be targeted?"
        # [oc]Zoom on Wechsler card 1.2

        # "The answer seems to be for money and success.[od]"
        # [od]Switch to wechsler 1.3

        # "Perhaps this was Weschler,[of]"
        # [of]Back to Wechsler 1.4

        # "at Arp he had power and influence and respec[og]"
        # [og]Zoom out, highlight Wechsler/Arp and Weschler/S org

        # "our old friend Desjardins. [om]"
        # [om]Zoom to Dejardins card 1.3

        # " woman [op]called Signe Rabe in Carcassonne in 1952."
        # [op]New Signe Rabe card emerges from Dejardins, zoom on Signe 1.1

        # "Signe’s date of birth is listed as 4th Nov 1930 a"
        # [or]Cut back to Signe card 1.2

        # "So logic dictates A. Rabe is Amarante Durand[ot] and Signe is Durand’s daughter.[ou]"
        # [ot]Switch to Signe 1.3

        # "and Signe is Durand’s daughter.[ou]"
        # [ou]Zoom out, link Signe to Durand and Ekstrom

        # "Weeping with joy to see his daughter an[ox]d surrogate son together perhaps."
        # [ox]Back to diagram, pan to Signe then Vaclav

        # "and she says s[pc]he only knew the name b"
        # [pc]Show Caldeira, MacInnes, Durand and Bouchard

        # "FXC did meet Desjardins.[pd]"
        # [pd]Zoom out, link FXC to Desjardins

        # "Turns out Signe[pf] died in 1956 after a long illness,"
        # [pf]Pan back to Signe and zoom on Signe 1.4

        # "This tragedy adds to[pg] Desjardins’ motivations and could explain w"
        # [pg]Zoom out to whole diagram

        # "why he fell out with Moody[ph]"
        # [ph]Highlight connection between Moody and Des (or circle M)

        # "started getting funding from MacInnes,[pi]"
        # [pi]Highlight connection between Moody and Mac (or circle M)

        # "the guy who orphaned Signe"
        # deleted this one, double check..
        # " Hence Desjardins knew he could trust Eric[pk]"
        # [pk]Highlight connection between Des and Eric, or zoom into Des and highlight bullet point "sent Eric obsidian piece"

        # "Back to Signe though[pl]"
        # [pl]Pan back to Signe 1.5

        # "one of these “uncles” must have been Summersby.[pn]"
        # [pn]Zoom out, link Sum to Sig

        # "we think the other is Vaclav. [po]"
        # [po]Link Sig to Vaclav

        # "Firstly, when recording his tape, [pp]"
        # [pp]Zoom in on tape card 1.6

        # "(Summersby is absolutely the best S member, for the record)[pq]"
        # [pq]Add bullet point (or crown haha)

        # "to postpone meeting with Caldeira.[pr]"
        # [pr]Pan to show Vaclav and Caldeira

        # "he and Vaclav swore secrecy[ps]"
        # [ps]Link Vaclav and Summersby strongly

        # [pt]Pan to Signe
        # another one I accidentally deleted

        # "We are coming to the end of this section[pu]"
        # [pu]Zoom out to show whole diagram

        # "Did Straka really die in Havana?[pw]"
        # [pw]Zoom on VMS 2.2

        # "but there’s essentially no evidence[px] that he didn’t"
        # [px]Switch to VMS 2.3

        # "lines up with all other S-related deaths[py]"
        # [py]Zoom out to highlight all mysterious death victims
