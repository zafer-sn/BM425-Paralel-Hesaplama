from threading import Condition
class WaitGroup:
    waiting_count = 0
    cv = Condition()
    def add(self, count):
        self.cv.acquire()
        self.waiting_count += count
        self.cv.release()
    def wait(self):
        self.cv.acquire()
        while self.waiting_count > 0:
            self.cv.wait()
        self.cv.release()
        """
            with self.cv:
                while self.waiting_count > 0:
                    self.cv.wait()
        """
    def done(self):
        self.cv.acquire()
        if self.waiting_count > 0:
            self.waiting_count -= 1
        if self.waiting_count == 0:
            self.cv.notify_all()
        self.cv.release()
