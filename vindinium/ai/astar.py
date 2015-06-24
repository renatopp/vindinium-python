import vindinium as vin
from vindinium.utils import HeapQueue

__all__ = ['AStar']

DIR_NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class AStar(object):
    '''A* algorithm specialized for vindinium.

    The A* algorithm receives an instance of ``vindinium.models.Map``` and  
    compute the best path when necessary. 

    Attributes:
        cost_avoid (float): cost to walk over an avoidable tile (consult the
          avoid_tiles attribute). Defaults to 4.
        cost_move (float): cost to walk over an empty tile. Defaults to 1.
        obstacle_tiles (list): a list of obstacles tile VALUES.
        avoid_tiles (list): a list of avoidable tile VALUES.
    '''
    def __init__(self, map):
        '''Constructor.

        Args:
            map (vindinium.models.Map): the map instance.
        '''
        self.cost_avoid = 4
        self.cost_move = 1
        self.obstacle_tiles = [vin.TILE_WALL, vin.TILE_TAVERN, vin.TILE_MINE]
        self.avoid_tiles = [vin.TILE_SPAWN]
        self._map = map

    def find(self, x0, y0, x1, y1):
        '''Find a path between (x0, y0) and (x1, y1).

        Args:
            x0 (int): initial position in X.
            y0 (int): initial position in Y.
            x1 (int): goal position in X.
            y1 (int): goal position in Y.
        
        Returns:
            (list) if the path has been found, e.g. ``[(0, 1), (0, 2), ...]``.
              Notice that, it does not include the initial position, but 
              include the goal.
            (None) otherwise.
        '''
        # To avoid access on the dot
        cost_move = self.cost_move
        cost_avoid = self.cost_avoid
        map = self._map
        adjacent = False

        # If obstacle, cancel search
        if map[x1, y1] in self.obstacle_tiles:
            adjacent = True

        # State x, y, g, parent
        start = (x0, y0, 0, None)
        queue = HeapQueue()
        visited = [(x0, y0)]
        state = None
        
        queue.push(start, 0)
        while not queue.is_empty():
            state = queue.pop()
            x, y, g, parent = state

            # Goal
            if (x==x1 and y==y1) or (adjacent and (abs(x-x1)+abs(y-y1))==1):
                break

            # Children
            for x_, y_ in self.__neighbors(x, y, visited):
                tile = map[x_, y_]
                g_ = g + (cost_avoid if tile in self.avoid_tiles else cost_move)
                h_ = abs(x_-x1)+abs(y_-y1)
                queue.push((x_, y_, g_, state), g_+h_)

        # If while does not break, it means that it didn't found any path
        else:
            return None

        # Prepare result
        result = []
        while state:
            result.insert(0, (state[0], state[1]))
            state = state[3]
        result.pop(0)

        return result

    def __neighbors(self, x, y, visited):
        '''Get the valid neighbors of a tile.'''
        m = self._map
        s = m.size
        for dx, dy in DIR_NEIGHBORS:
            tx, ty = x+dx, y+dy
            
            if not(-1<tx<s and -1<ty<s): continue

            tile = m[tx, ty]
            if tile not in self.obstacle_tiles and (tx, ty) not in visited:
                visited.append((tx, ty))
                yield tx, ty
