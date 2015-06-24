import random

def terminal(minimax, game, state):
    '''Verifies if a given state is terminal or not.'''
    return state.turn >= game.max_turns*4

MOVES = {
    # 'Stay'  : (0, 0),
    'North' : (0, -1),
    'West'  : (-1, 0),
    'South' : (0, 1),
    'East'  : (1, 0)
}
def generate(minimax, game, state):
    '''Generates the children of a given state.'''
    id = state.turn%4
    hero = state.heroes[id]
    x = hero['x']
    y = hero['y']
    size = game.map.size

    result = []
    for move, dir in MOVES.iteritems():
        x_, y_ = x+dir[0], y+dir[1]
        if not(-1<x_<size and -1<y_<size): continue
        s = state.clone()
        s.simulate(move)
        result.append(s)
    return result

def evaluate(minimax, game, state):
    '''Evaluate the state.'''
    id = (game.turn%4)+1
    hero = state.heroes[id-1]
    
    value = 0
    distance = None
    for (x, y), owner in state.mines.iteritems():
        mod = 1 if (owner==id) else -1

        # mine ownership
        value += 0 if owner is None else mod*1000

        # mine distance
        if mod != 1:
            d = abs(hero['x']-x)+abs(hero['y']-y)
            if distance is None or d < distance:
                distance = d

    value -= distance or 0

    # life
    value += round(hero['life']/10)

    return value
    
def sort(minimax, game, states):
    '''Sort the state children.'''
    return reversed(states)