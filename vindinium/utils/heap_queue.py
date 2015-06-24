import heapq

__all__ = ['HeapQueue']

class HeapQueue(object):
    '''A priority queue implementation (it uses the heapq builtin module).

    Based on http://www.redblobgames.com/pathfinding/a-star/implementation.html
    '''

    def __init__(self):
        '''Constructor.'''
        self._queue = []
    
    def is_empty(self):
        '''Verifies if the queue is empty or not.
        
        Returns:
            (bool) whether if the queue is empty or not.
        '''
        return len(self._queue) == 0
    
    def push(self, item, priority):
        '''Pushes an item to the queue, given a priority.

        Args:
            item (object) any object.
            priority (int) a priority value.
        '''
        heapq.heappush(self._queue, (priority, item))
    
    def pop(self):
        '''Pops an item from the queue.

        Returns:
            (object) the stored item.
        '''
        return heapq.heappop(self._queue)[1]