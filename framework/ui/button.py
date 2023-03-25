"""
The button module contains both basic and extensive buttons
that vary from plain to complex.
"""

import pygame


class Button(object):
    """
    Buttons are interactable objects that have several
    customizable parameters such as border radius, animation type
    and color. These buttons are also highly modular, meaning they
    can be applied to both static and dynamic images.
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
