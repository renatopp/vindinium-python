__all__ = ['Hero']

class Hero(object):
    '''Represents a hero in the game.

    Attributes:
        id (int): the hero's id.
        name (string): the bot's name.
        user_id (string): the bot's id (None in training mode).
        elo (int): the bot's ELO (None in training mode).
        crashed (bool): True if the bot has been disconnected. 
        mine_count (int): the number of mines this hero owns.
        gold (int): current amount of gold earned by this hero.
        life (int): current hero's life.
        last_dir (string): last bot movement (may be None).
        x (int): the bot's position in the X axis.
        y (int): the bot's position in the Y axis.
        spawn_x (int): the bot's spawn position in X.
        spawn_y (int): the bot's spawn position in Y.
    '''
    
    def __init__(self, hero):
        '''Constructor.
        
        Args:
            hero (dict): the hero data from the server.
        '''
        # Constants
        self.id         = hero['id']
        self.name       = hero['name']
        self.user_id    = hero.get('userId')
        self.elo        = hero.get('elo')
        
        # Variables
        self.crashed    = hero['crashed']
        self.mine_count = hero['mineCount']
        self.gold       = hero['gold']
        self.life       = hero['life']
        self.last_dir   = hero.get('lastDir')
        self.x          = hero['pos']['y']
        self.y          = hero['pos']['x']
        self.spawn_x    = hero['spawnPos']['y']
        self.spawn_y    = hero['spawnPos']['x']
