from dataclasses import dataclass


@dataclass
class Swipe:
    """
    The `Swipe` class is for transitions that pertain to
    anything that needs to be moved from one side of the
    screen (off screen) to the juxtaposing side.

    This is normally done through a series of vector
    motions, and, depending on how fancy you want to
    get, it can be quite the task.

    This class aims to simplify that process, and make it
    as easy as possible to implement smooth, good looking
    transitions with as little code as possible.
    """

    def __init__(self,
                 color=list[tuple] | tuple):
        """
        :param color: NOTE this can be more than one color!
        """

        def up_to_down(self, parameter_list):
            pass
