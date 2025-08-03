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

    def construct(self):
        self.initialise_layout()
        self.start_HERE()

        self.play(self.frame_cards())
