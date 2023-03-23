import time

class Timer:

    """A timer class that can be used to time things
    """

    def __init__(self, top: int):
        self._start_time = None
        self.top = top
    
    def _check_timer_not_none(self, error_message: str):
        """Check if the timer has been started and raise an exception if it has not"""
        if self._start_time != None:
            raise Exception(error_message)

    def _check_timer_none(self, error_message: str):
        """Check if the timer has not been started and raise an exception if it has"""
        if self._start_time == None:
            raise Exception(error_message)
    
    def is_time_up(self):
        """Check if there is time left"""
        if self._start_time == None:
            return False

        elapsed_time = time.perf_counter() - self._start_time
        return elapsed_time > self.top
    
    def is_timer_running(self):
        """Check if the timer is running"""
        return self._start_time is not None
    
    def clear(self):
        """Clear the timer"""
        self._start_time = None

    def start(self):
        """Start a new timer"""
        self._check_timer_not_none("Timer is already running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer"""
        self._check_timer_none("Timer is already stopped. Use .start() to start it")

        self._start_time = None
    
    def get_time_left(self):
        """Get the time left"""

        if self._start_time is None:
            return self.top

        elapsed_time = time.perf_counter() - self._start_time
        return self.top - elapsed_time
    
    
    def clear_and_start(self):
        """Clear the timer and start it"""
        self.clear()
        self.start()