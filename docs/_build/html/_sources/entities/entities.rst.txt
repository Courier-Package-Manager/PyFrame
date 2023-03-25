Entities
========

The entities package is to hold core entities.
See the glossary for the definition of an entity.

Player
------

The default player class mainly pertains to the
basic needs of the developer such as movement, collision,
drawing and updating as well as additional support for
animation if needed.

Currently the player class serves as a placeholder file
and will later use entities as a superclass.

:doc:`Player Documentation <../entities/player>`

Sprite
------

Entity class used as super class for tiles.
This is a sprite class, *not meant to be used as an actual sprite but it can be done*. This is merely a dataclass to abstract tiles/entities from.

.. code-block::
   :caption: Note: not recommended for public use.

        from framework.entities.sprite import _Entity

        class MySprite(_entity):
            def __init__(self, x, y, width, height, color, rect,
                         surface):
                ...  # etc

Constructor holds variables that can't be declared
in the previous dataclass section.

Note that because the `alpha` property returns either `True`
or `False` the `self.alpha` declaration, whilst at
a surface level might seem redundant, effectively
states the following:

.. code-block::
   :caption: This is possible because both `SRCALPHA` and `false` are valid arguments  for `pygame.Surface(_, ...).

        alpha = True if pygame.SRCALPHA else False


This is possible because both SRCALPHA and false are
valid arguments in pygame.Surface(_, ...)

Additionally, the setter for the alpha property returns
true or false by default, but also can return SRCALPHA
when needed, such as in this case.


Tile2D
------

White (although color can be changed) 2D tile that has
physics (apart from gravity), the ability to collide with other entities,
the potential to collectively interact with other tiles as well.

Tiles can be used as follows:

.. code-block::

        from framework import Tile2D

        tile_with_rect = Tile2D(color=white, pygame.Rect(10, 20, 30, 40))
        tile_without_rect = Tile2D(x=10, y=20, color=red)
