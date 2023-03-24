import pygame
from dataclasses import dataclass

white = 255, 255, 255


@dataclass
class _Entity:
    """
    Description
    -----------
    Entity class used as super class for tiles.
    This is a sprite class, ** not meant to be used as an actual
    sprite but it can be done. This is merely a dataclass
    to abstract tiles/entities from.

    > If you *really* want to use this class.
    Usage
    -----
    >>> from framework.entities.sprite import _Entity
    >>> class MySprite(_entity):
    >>>     def __init__(self, x, y, width, height, color, rect,
    >>>                  surface):
    >>>         ...  # etc

    :param x: int or float relative position
    :type x: int | float
    :param y: int or float relative position
    :type y: int | float
    :param width:   tile width as integer (default=50)
    :type width: int
    :param height: tile height as integer (default=50)
    :type height: int
    :param color: color of tile (red, green, blue, <optional alpha>)
    :type color: tuple
    :param rect: pygame.Rect object if needing a pre-defined rect
    :type rect: None | pygame.rect.Rect
    :param surface: pygame surface type (if using an image)
    :type surface: pygame.SurfaceType | None
    :param image: Mandatory as all sprites must have an image property.
    :type image: None | pygame.surfaceType
    """

    color: tuple
    rect: pygame.Rect
    x: int | float
    y: int | float
    width: int
    height: int
    surface: None | pygame.SurfaceType = None
    image: pygame.SurfaceType

    def __init__(self):
        """
        Description
        -----------
        Constructor holds variables that can't be declared
        in the previous dataclass section.

        :instancevar self.image: mandatory image variable.
        :type self.image: pygame.SurfaceType

        Note
        ----
        Because the `alpha` property returns either `True`
        or `False` the self.alpha_ declaration, whilst at
        a surface level might seem redundant, effectively
        states the following:

        >>> alpha = pygame.SRCALPHA if True else False

        This is possible because both SRCALPHA and false are
        valid arguments in pygame.Surface(_, ...)

        Additionally, the setter for the alpha property returns
        true or false by default, but also can return SRCALPHA
        when needed, such as in this case.
        """

        self.alpha_ = pygame.SRCALPHA if self.alpha else self.alpha
        self.image = pygame.Surface((self.width, self.height), self.alpha_)

    @property
    def alpha(self):
        """Returns if the sprite is transparent compatible.

        :rtype: bool
        """

        return self._alpha

    @alpha.setter
    def alpha(self, value=False):
        """Sets the alpha transparency.

        This is based on the `color` parameter and its' RGB state.

        :param __value: *Ignore parameter*
        """

        if not value:
            self._alpha = len(self.color) == 4
        else:
            return pygame.SRCALPHA
