from . import BWidget

class ArrowButton(BWidget):
    def __init__(self, master=None, cnf={}, **kw):
        BWidget.__init__(self, master, 'ArrowButton', cnf, **kw)