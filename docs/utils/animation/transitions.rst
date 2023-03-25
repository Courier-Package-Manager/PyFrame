Transitions
===========
Transitions are primarily for simplifying process 
of the (quite laborious) task of animation in pygame.

I myself have found that transitions are, not neccessarily hard,
but more of a tedious thing to write out continuously. Some people derive pleasure from this though. We call those people masochists.


Mask
----
Mask used as a cover in stringer and swipe transitions.
Not intended for external use.

Swipe Transitions
-----------------

The `Swipe` class is for transitions that pertain to
anything that needs to be moved from one side of the
screen (off screen) to the juxtaposing side.

This is normally done through a series of vector
motions, and, depending on how fancy you want to
get, it can be quite the task.

This class aims to simplify that process, and make it
as easy as possible to implement smooth, good looking
transitions with as little code as possible.

Available transitions for the Swipe class:
 - up_to_down
