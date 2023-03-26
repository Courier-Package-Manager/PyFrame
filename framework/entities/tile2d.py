from .sprite import _Entity, white


class Tile2D(_Entity):
    """
    Description
    -----------
    White (although color can be changed) 2D tile that has
    physics (apart from gravity), the ability to collide with other entities,
    the potential to collectively interact with other tiles as well.

    Usage
    -----
    >>> from framework import Tile2D
    >>> tile_with_rect = Tile2D(color=white, pygame.Rect(10, 20, 30, 40))
    >>> tile_without_rect = Tile2D(x=10, y=20, color=red)

    :param _Entity: Super class entity, contains useful properties.
    :type _Entity: object
    """

    def __init__(self, x, y, width=50, height=50, color=white, rect=None,
                 surface=None):
        """
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
        """

        super().__init__(x, y, width, height, color, rect, surface)
