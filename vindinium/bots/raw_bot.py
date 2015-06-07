__all__ = ['RawBot']

class RawBot(object):
    '''Raw bot. This bot does not process the state.

    Implement the following methods to use:

    - start(state): called when the game starts.
    - move(state): called when the game requests a move from this bot.
    - end(): called after the game finishes.

    Attributes:
        id (int): the bot's id.
        state (dict): the unprocessed state from server.
    '''
    id = None
    state = None

    def _start(self, state):
        '''Wrapper to start method.'''
        self.id = state['hero']['id']
        self.state = state
        self.start()

    def _move(self, state):
        '''Wrapper to move method.'''
        self.state = state
        return self.move()

    def _end(self):
        '''Wrapper to end method.'''
        self.end()
        
    def start(self):
        '''Called when the game starts.'''
        pass

    def move(self):
        '''Called when the game requests a move from this bot.'''
        pass

    def end(self):
        '''Called after the game finishes.'''
        pass
