#domi A* apo eclass

class State:
    def __init__(self):
        # g+h
        self._f = 0
        #euretiki sinartisi
        self._h = 0
        #posa vimata ekane o pextis mexri auto to state
        self._g = 0
        #proigoumeno state
        self._father = None
        self._total_time = 0

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @property
    def father(self):
        return self._father

    @property
    def total_time(self):
        return self._total_time

    @f.setter
    def f(self, f):
        self._f = f

    @g.setter
    def g(self, g):
        self._g = g

    @h.setter
    def h(self, h):
        self._h = h

    @father.setter
    def father(self, f):
        self._father = f

    @total_time.setter
    def total_time(self, time):
        self._total_time = time

    def __lt__(self, s):
        return self.f < s.f