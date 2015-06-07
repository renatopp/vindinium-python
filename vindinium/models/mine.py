__all__ = ['Mine']

class Mine(object):
    '''A mine object.
    
    Attributes:
        x (int): the mine position in X.
        y (int): the mine position in Y.
        owner (int): the hero's id that owns this mine.
    '''
    
    def __init__(self, x, y):
        '''Constructor.

        Args:
            x (int): the mine position in X.
            y (int): the mine position in Y.
        '''
        self.x = x
        self.y = y
        self.owner = None
