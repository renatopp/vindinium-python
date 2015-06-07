import time

__all__ = ['Timer']

class Timer(object):
    '''Timer helper.

    A timer object helps to verify how much time has been taken to execute some
    code.

    Example:
        You can use this class in two ways. First as a with statement::

            with Timer() as timer:
                # your code here
            print timer.elapsed

        Notice that you can pass ``True`` as argument to Timer in order to 
        allow it to print the elapsed time when the with finishes.
  
        Alternatively, you can use Timer like the tic toc functions of Matlab::
  
            timer = Timer()
            timer.tic()
            # your code here
            print timer.toc()

    Attributes:
        elapsed (float): the elapsed time between ``tic()`` and ``toc()``.
    '''

    def __init__(self, do_print=False):
        '''Constructor.

        Args:
            do_print (bool): whether timer should print the result after 
              ``with`` ends or not. Default to False.
        '''
        self._do_print = do_print
        self._start_time = 0
        self.elapsed = 0

    def __enter__(self):
        '''Enters with'''
        self.tic()
        return self

    def __exit__(self, type, value, traceback):
        '''Leaves with'''
        self.toc()

        if self._do_print:
            print 'Elapsed time is %f seconds.'%self.elapsed

    def tic(self):
        '''Start the timer.'''
        self._start_time = time.time()

    def toc(self):
        '''Stops the timer and returns the elapsed time.

        Returns
            (float) the elapsed time.
        '''
        self.elapsed = time.time() - self._start_time
        return self.elapsed
