'''Awesome python client for Vindinium.

Vindinium is an online and continuous competition where you control a bot in a
turn-based game, consult `the site <http://vindinium.org>`_ to know more. 
Note: this client is based on the `ornicar's client 
<https://github.com/ornicar/vindinium-starter-python>`_.

This library provides several base and simple bots, helper structures and 
common algorithms that allow you to create bots in an easy and fast way,
focusing on the strategy and specific techniques of your bot.

The library has the following features:

- Bots:
    - RawBot: a bot that does nothing.
    - BaseBot: a bot that process the state and create and update a Game object.
    - RandomBot: a bot that perform random movements.
    - MinerBot: a bot that looks for mines continuously.
    - AggressiveBot: a bot that only goes after other bots.

- Models (used by base bot to create the game structure):
    - Game: stores all other models.
    - Map: stores static information about the map.
    - Mine: represents a mine in the map.
    - Hero: represents a hero in the game.
    - Tavern: represents a tavern in the game.
  
- AI algorithms (in general, already specialized for vindinium):
    - AStar: the A* algorithm.

Note: this client fix the inconsistent axis of the server, so you don't have to
worry about that (if you're using the game model).

'''

from .client import *
from . import bots
from . import models
from . import ai
from . import utils

# CONSTANTS
# tile values
TILE_EMPTY  = 0
TILE_WALL   = 1
TILE_SPAWN  = 2
TILE_TAVERN = 3
TILE_MINE   = 4

# command values
NORTH = 'North'
SOUTH = 'South'
WEST  = 'West'
EAST  = 'East'
STAY  = 'Stay'

# direction
DIR_NORTH = ( 0, -1)
DIR_SOUTH = ( 0,  1)
DIR_WEST  = (-1,  0)
DIR_EAST  = ( 1,  0)
DIR_STAY  = ( 0,  0)
