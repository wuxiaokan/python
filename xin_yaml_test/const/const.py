import sys

class Const():
    con = {}
    def __setattr__(self, key, value):
       self.con[key] = value

    def __getattr__(self, key):
        return self.con[key]

sys.modules[__name__] = Const()
