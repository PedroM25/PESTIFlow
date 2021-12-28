from abc import ABC


class ExtractionUI(ABC):
    """ This class must NOT be instantiated. Parent UI class for all feature extraction variants; each one might
    display a loading bar, some informative text to inform the user on the progress of the operation

    UI class must only have access to info that will be displayed, everything else stays in the controller class

    UI was deliberately made with one method so as to give liberty to developers wishing to make a different UI for
    different extractions. By doing this, we do not bind the same UI to all extractors or fall in the trap of making
    UI too strict and complicated of changing
    """

    def __init__(self, intro):
        self._print_intro(intro)

    def _print_intro(self, string):
        print("+----" + "-" * len(string) + "----*")
        print("|    " + string + "    |")
        print("+----" + "-" * len(string) + "----*")
