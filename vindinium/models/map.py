__all__ = ['Map']

class Map(object):
    '''Represents static elements in the game, such as walls, paths, taverns, 
    mines and spawn points.

    Attributes:
        size (int): the board size (in a single axis).
    '''
    
    def __init__(self, size):
        '''Constructor.
        
        Args:
            size (int): the board size.
        '''
        self.size = size
        self.__board = [[0 for i in xrange(size)] for j in xrange(size)]

    def __getitem__(self, key):
        '''Returns an item in the map.'''
        return self.__board[key[0]][key[1]]

    def __setitem__(self, key, value):
        '''Sets an item in the map.'''
        self.__board[key[0]][key[1]] = value

    def __str__(self):
        '''Pretty map.'''
        s = ' '
        s += '-'*(self.size) + '\n'
        for y in xrange(self.size):
            s += '|'
            for x in xrange(self.size):
                s += str(self[x, y] or ' ')
            s += '|\n'
        s += ' ' + '-'*(self.size)
        return s