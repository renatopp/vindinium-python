import random
import vindinium as vin
from vindinium.bots import BaseBot
from vindinium.ai import AStar

__all__ = ['MinerBot']

class MinerBot(BaseBot):
    '''Miner bot.'''
    
    search = None

    def start(self):
        self.search = AStar(self.game.map)

    def move(self):
        if self.hero.life < 50:
            return self._go_to_nearest_tavern()
        else:
            return self._go_to_nearest_mine()

    def _go_to_nearest_mine(self):
        x = self.hero.x
        y = self.hero.y

        # Order mines by distance
        mines = vin.utils.order_by_distance(x, y, self.game.mines)
        for mine in mines:

            # Grab nearest mine that is not owned by this hero
            if mine.owner != self.hero.id:
                command = self._go_to(mine.x, mine.y)

                if command:
                    return command

        return self._random()

    def _go_to_nearest_tavern(self):
        x = self.hero.x
        y = self.hero.y

        # Order taverns by distance
        taverns = vin.utils.order_by_distance(x, y, self.game.taverns)
        for tavern in taverns:
            command = self._go_to(tavern.x, tavern.y)

            if command:
                return command

        return self._random()

    def _go_to(self, x_, y_):
        x = self.hero.x
        y = self.hero.y

        # Compute path to the mine
        path = self.search.find(x, y, x_, y_)

        # Send command to follow that path
        if path is None:
            return

        elif len(path) > 0:
            x_, y_ = path[0]

        return vin.utils.path_to_command(x, y, x_, y_)

    def _random(self):
        return random.choice(['Stay', 'North', 'West', 'East', 'South'])