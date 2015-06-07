import random
from vindinium.bots import RawBot

__all__ = ['RandomBot']

class RandomBot(RawBot):
    '''Random bot.'''
    
    def move(self):
        return random.choice(['Stay', 'North', 'West', 'East', 'South'])