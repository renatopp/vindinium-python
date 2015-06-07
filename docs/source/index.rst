Vindinium Python
================

Awesome python client for Vindinium.

Vindinium is an online and continuous competition where you control a bot in a
turn-based game, consult `the site <http://vindinium.org>`_ to know more. 
Note: this client is based on the `ornicar's client 
<https://github.com/ornicar/vindinium-starter-python>`_.

This library provides several base and simple bots, helper structures and 
common algorithms that allow you to create bots in an easy and fast way,
focusing on the strategy and specific techniques of your bot.

Note: this client fix the inconsistent axis of the server, so you don't have to
worry about that (if you're using the game model).

Basic Guide
-----------

.. toctree::
   :maxdepth: 2

   guide/installation
   guide/getting_started
   guide/snippets


API
---

Main Module
~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   api/client


Bots
~~~~

Contains the base classes for you to create new bots and simple bots examples.

.. toctree::
   :maxdepth: 2

   api/bots.raw_bot
   api/bots.base_bot
   api/bots.random_bot
   api/bots.miner_bot


Models
~~~~~~

Used by ``BaseBot`` to create the game structure. Consult the ``Game`` class to
see what it can do.

.. toctree::
   :maxdepth: 2

   api/models.game
   api/models.map
   api/models.hero
   api/models.mine
   api/models.tavern


Artificial Intelligence
~~~~~~~~~~~~~~~~~~~~~~~

Bunch of artificial intelligence methods and structures. In general, these 
methods are already specialized for vindinium (e.g., AStar is already 
configured for grid).

.. toctree::
   :maxdepth: 2

   api/ai.heap_queue
   api/ai.astar


Utils
~~~~~

Utility functions and classes.

.. toctree::
   :maxdepth: 2

   api/utils.timer
   api/utils.functions



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

