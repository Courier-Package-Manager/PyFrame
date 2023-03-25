import pygame
from dataclasses import dataclass


@dataclass
class Mask:
    """
    Mask used as a cover in stringer and swipe transitions.
    Not intended for external use.
    """

    def __init__(self, size: list[int], color=(0, 0, 0), alpha=True):
        """
        :param size: Size as a list object, states the size of the  mask.
        :param color: Color as an RGB value. Pygame values can also be used.
        :param alpha: Does not correspond to color, parsed as a boolean value.
        """

        self.size = size
        self.color = color
        self.alpha = alpha


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

    def __init__(
            self,
            color=list[tuple] | tuple):
        """
        :param color: NOTE this can be more than one color!
        """

        self.surface = pygame.display.get_surface()

        def up_to_down(self):
            """ Swipe up to down """

            pass
