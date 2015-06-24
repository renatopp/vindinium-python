import random
import vindinium as vin
from vindinium.bots import BaseBot
from vindinium.ai import AStar

__all__ = ['AggressiveBot']

class AggressiveBot(BaseBot):
    '''Aggressive bot.'''
    
    search = None

    def start(self):
        self.search = AStar(self.game.map)
        self.target = None

    def move(self):
        print self.hero.life
        self.target = self._get_best_target()
        distance = vin.utils.distance_manhattan(self.hero.x, self.hero.y, 
                                                self.target.x, self.target.y)
        in_spawn = self.target.x == self.target.spawn_x and self.target.y == self.target.spawn_y

        if self.hero.life <= 40 and self.hero.gold > 2:
            return self._go_to_nearest_tavern()

        elif distance < 5 and not in_spawn:
            return self._go_to(self.target.x, self.target.y)

        elif self.hero.life <= 60 and self.hero.gold > 2:
            return self._go_to_nearest_tavern()

        else:
            return self._go_to(self.target.x, self.target.y)

    def _get_best_target(self):
        target = None
        for hero in self.game.heroes:
            if hero.id == self.id: continue

            if target is None or hero.mine_count > target.mine_count:
                target = hero

        return target

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