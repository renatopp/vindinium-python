import vindinium

__all__ = ['dir_to_command', 'command_to_dir', 'path_to_command',
           'distance_manhattan', 'order_by_distance']

def dir_to_command(dx, dy):
    '''Converts a direction to a command.
    
    Args:
        dx (int): direction in X axis, must be 1, 0 or -1.
        dy (int): direction in Y axis, must be 1, 0 or -1.

    Returns:
        (string) a command.

    Raise:
        ValueError if direction is invalid.
    '''
    if   dx==-1 and dy== 0: return vindinium.WEST
    elif dx== 1 and dy== 0: return vindinium.EAST
    elif dx== 0 and dy==-1: return vindinium.NORTH
    elif dx== 0 and dy== 1: return vindinium.SOUTH
    elif dx== 0 and dy== 0: return vindinium.STAY

    raise ValueError('Invalid direction (%s, %s).'%(dx, dy))


def command_to_dir(command):
    '''Converts a command to a direction.
    
    Args:
        (string) the command.

    Returns:
        (tuple) a tuple (dx, dy) with the direction.

    Raise:
        ValueError if command is invalid.
    '''
    if   command == vindinium.NORTH: vindinium.DIR_NORTH
    elif command == vindinium.SOUTH: vindinium.DIR_SOUTH
    elif command == vindinium.WEST:  vindinium.DIR_WEST
    elif command == vindinium.EAST:  vindinium.DIR_EAST
    elif command == vindinium.STAY:  vindinium.DIR_STAY

    raise ValueError('Invalid command "%s".'%command)


def path_to_command(x0, y0, x1, y1):
    '''Converts an adjacent to a command.
    
    Args:
        x0 (int): initial position in X axis.
        y0 (int): initial position in Y axis.
        x1 (int): final position in X axis.
        y1 (int): final position in Y axis.

    Returns:
        (string) a command.

    Raise:
        ValueError if direction is invalid.
    '''
    dx = x1-x0
    dy = y1-y0
    return dir_to_command(dx, dy)

def distance_manhattan(x0, y0, x1, y1):
    '''Computes the manhattan distance between two points.

    Args:
        x0 (int): initial position in X axis.
        y0 (int): initial position in Y axis.
        x1 (int): final position in X axis.
        y1 (int): final position in Y axis.

    Returns
        (int) the distance.
    '''
    return abs(x0-x1)+abs(y0-y1)

def order_by_distance(x, y, objects):
    '''Returns a list of objects ordered by distance from a given point.

    You can use this to order mines or taverns by their distances from the 
    hero.

    Args:
        x (int): position in X.
        y (int): position in Y.
        objects (list): list of objects. The objects must implement the 
        attributes ``x`` and ``y``.
    
    Returns:
        (list) an ordered copy of ``objects``.
    '''

    return sorted(objects, key=lambda item:distance_manhattan(x, y, item.x, item.y))


