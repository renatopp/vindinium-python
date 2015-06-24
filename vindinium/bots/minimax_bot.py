import random
import vindinium as vin
from vindinium.bots import BaseBot
from vindinium.ai import Minimax

__all__ = ['MinimaxBot']

class MinimaxBot(BaseBot):
    '''Minimax bot.'''
    
    search = None

    def start(self):
        self.search = Minimax(self.game, 8)

    def move(self):
        moves = self.search.find()
        return moves[0]