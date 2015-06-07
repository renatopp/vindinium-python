Snippets
========

Except when explicit saying otherwise, use the following base code::
  
    import vindinium
  
    class MyBot(vindinium.bots.BaseBot):
        # stuff here
        pass


Random Bot
----------

A random bot::

    import random
    import vindinium

    class RandomBot(vindinium.bots.RawBot):
        moves = [
          vindinium.STAY,
          vindinium.NORTH,
          vindinium.EAST,
          vindinium.WEST,
          vindinium.SOUTH
        ]
        def move(self):
            return random.choice(self.moves)



Move to specific position
-------------------------

Uses A* to find a path to some specific location::

    def start(self):
        self.search = vindinium.ai.AStar(self.game.map)

    def move(self):
        return self.go_to(3, 4)

    def go_to(self, x_, y_):
        x = self.hero.x
        y = self.hero.y

        # Compute path to the mine
        path = self.search.find(x, y, x_, y_)

        # Send command to follow that path
        if len(path) > 0:
            x_, y_ = path[0]

        return vin.utils.path_to_command(x, y, x_, y_)


Move to nearest tavern
----------------------

Consider the ``go_to`` method::

    def go_to_nearest_tavern(self):
        x = self.hero.x
        y = self.hero.y

        # Order taverns by distance
        taverns = vin.utils.order_by_distance(x, y, self.game.taverns)
        return self.go_to(taverns[0].x, taverns[1].y)


Move to nearest enemy/neutral mine
----------------------------------

Consider the ``go_to`` method::

    def go_to_nearest_mine(self):
        x = self.hero.x
        y = self.hero.y

        # Order mines by distance
        mines = vin.utils.order_by_distance(x, y, self.game.mines)
        
        for mine in mines:
            # Grab nearest mine that is not owned by this hero
            if mine.owner != self.id:
                return self.go_to(mine.x, mine.y)

        return vindinium.STAY
