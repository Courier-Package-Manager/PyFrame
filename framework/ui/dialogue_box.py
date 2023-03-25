"""
Dialogue boxes are commonly used when interacting
with NPC's and other entities that pertain to
RPG / gameplay elements, but, can be used with pretty
much anything.
"""

import pygame


class SimpleBox():
    """
    A simple dialogue box for npc interactions.
    Contains a simple border radius with a neat
    black outline.
    """

    def __init__(self, x, y, text, font=pygame.font.get_default_font()):
        self.text = text
        self.font = font
