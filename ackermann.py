"""
This is still technically ongoing. I have an interest in recursion, and I think that the ackermann function is the pinnacle of recursion, as
it's one of the only functions I know of that isn't primatively recursive. For some unknown reason, python3.6 64bit doesn't want to run 
anything above ack(3,4), yet 32bit works fine. The inverse function is still being worked on, because I've been having difficulty deciphering 
the math behind it.
"""


import sys
sys.setrecursionlimit(100000000)


class Ackermann:
    def __init__(self):
        self.inverse = False
    
    def __str__(self):
        if self.inverse is False:
            return str(self.ack)
        else:
            return str(self.inverseAck)
    
    def ack(self, m, n):
        self.inverse = False
        if m == 0:
            return n + 1
        elif n == 0:
            return self.ack(m - 1, 1)
        else:
            return self.ack(m - 1, self.ack(m, n - 1))
    
    def inverseAck(self, m, n):
        pass
    
acker = Ackermann()
print(acker.ack(4, 1))
