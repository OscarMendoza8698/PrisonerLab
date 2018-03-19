from __future__ import print_function
import random

n = 100
def move(my_history, their_history, my_score, their_score, n):
    t = 1
    n = 100
    n1 = random.randint(0, n)
    if n1 > 50:
    if n1 < 50:
        return 'b'
    if their_history[-1]=='c':
        n = n + 10
    if their_history[-1]=='b':
        n = n - 10

def move(my_history, their_history, my_score, their_score):
    if their_history[-1]=='c':
        return 'b'
    if their_history[-1]=='b':
        return 'c'