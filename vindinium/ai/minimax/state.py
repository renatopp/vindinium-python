from . import simulation

class State(object):
    def __init__(self, game=None):
        if isinstance(game, State):
            self.last_move = game.last_move
            self.parent = game
            self._game = game._game
            self.turn = game.turn
            self.heroes = [h.copy() for h in game.heroes]
            self.mines = game.mines.copy()
        else:
            self.last_move = None
            self.parent = None
            self._game = game
            self.turn = game.turn
            self.heroes = []
            self.mines = {}
            self._populate()

    def _populate(self):
        for hero in self._game.heroes:
            h = dict(
                x          = hero.x,
                y          = hero.y,
                gold       = hero.gold,
                mine_count = hero.mine_count,
                life       = hero.life,
                spawn_x    = hero.spawn_x,
                spawn_y    = hero.spawn_y
            )
            self.heroes.append(h)

        for mine in self._game.mines:
            self.mines[(mine.x, mine.y)] = mine.owner

    def clone(self):
        return State(self)

    def simulate(self, move):
        self.last_move = move
        simulation.simulate(self, move)

    def __str__(self):
        s = 'Heroes (turn %d/%s): \n'%(self.turn, self.last_move or '')
        for i, hero in enumerate(self.heroes):
            s += '    %d: (%d, %d, l%03d, $%d, m%d)\n'%\
                    (i, hero['x'], hero['y'], 
                        hero['life'], hero['gold'], 
                        hero['mine_count'])

        return s