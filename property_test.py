class Score:
    def __init__(self):
        self._math = 0
        self._writing = 0

    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value): 
        if value < 10:
            self._math = 0
        elif value > 100:
            self._math = 100
        else:
            self._math = value

score = Score()
score.math = 50
print (score.math)

            
