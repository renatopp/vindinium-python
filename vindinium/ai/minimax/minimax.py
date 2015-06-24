import random
import vindinium
from .state import State
from . import functions as f

__all__ = ['Minimax']

class Minimax(object):
    '''Minimax algorithm.

    This class actually implements a negamax algorithm with alpha-beta pruning.
    You can pass specific functions to this class in order to override the
    default behavior. Consult ``vindinium.ai.minimax.functions`` to see the 
    default implementation of these functions.

    Attributes:
        game (vindinium.models.Game): a game instance.
        max_depth (int): maximum depth of the algorithm.
    '''

    def __init__(self, game, max_depth=5, f_terminal=f.terminal, 
                                          f_evaluate=f.evaluate,
                                          f_generate=f.generate,
                                          f_sort=f.sort):
        '''Constructor.


        Arguments:
            game (vindinium.models.Game): a game instance.
            max_depth (int): maximum depth of the algorithm. Defaults to 5.
            f_terminal (function): a function to verify if a state is terminal.
            f_evaluate (function): a function to evaluate the value of a state.
            f_generate (function): a function to generate a state children.
            f_sort (function): a function to sort the state children list.
        '''
        self.game = game
        self.max_depth = max_depth
        self._f_terminal = f_terminal
        self._f_evaluate = f_evaluate
        self._f_generate = f_generate
        self._f_sort = f_sort

    def find(self):
        '''Finds the best move, given the maximum depth.

        Returns:
            (list) a list of next expected commands (from your bot and the 
                enemies).
        '''
        state = State(self.game)
        value, state = self._minimax(state, self.max_depth)
        result = []

        while state.last_move:
            result.append(state.last_move)
            state = state.parent

        return result

    def _minimax(self, state, depth, alpha=-float('inf'), 
                                     beta=float('inf'),
                                     color=0):
        '''Nagamax function.'''
        state._value = 0
        game = self.game
        mod = 1 if color%4 == 0 else -1

        if depth == 0 or self._f_terminal(self, game, state):
            return (mod*self._f_evaluate(self, game, state), state)

        best_value = -float('inf')
        best_state = None
        next_states = self._f_generate(self, game, state)
        next_states = self._f_sort(self, game, next_states)

        for next_state in next_states:
            value, state_ = self._minimax(next_state, depth-1, -beta, -alpha, color+1)
            if color%4==0 or (color+1)%4==0:
                value = -value

            if (value > best_value) or (value == best_state and random.random() < 0.3):
                best_state = next_state
                best_value = value

            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return (best_value, best_state)
