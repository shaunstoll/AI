"""
Name: <Uriel (Shaun) Stoll>
Uni: <uds2104>
"""

# The function signatures are named for the questions they represent, for
# instance p1 is problem 1. Please do not modify any of the function signatures
# as they will be used for grading purposes

import numpy as np

def p1(k: int) -> str:

    s = ""
    s += str(fact(k))

    for i in range(k - 1, 0, -1):
        s += ", "
        s += str(fact(i))

    return s

def fact(k: int) -> int:

    assert k > -1, "int cannnot be negative."

    x = 1

    for i in range(k, 0, -1):
        x = x * i

    return x

def p2_a(x: list, y: list) -> list:
    y.sort(reverse = True)
    y.pop(len(y) - 1)
    return y

def p2_b(x: list, y: list) -> list:
    x.reverse()
    return x

def p2_c(x: list, y: list) -> list:
    return sorted((list(set(x + y))))

def p2_d(x: list, y: list) -> list:
    return [x, y]

def p3_a(x: set, y: set, z: set) -> set:
    return x.union(y, z)

def p3_b(x: set, y: set, z: set) -> set:
    return x.intersection(y, z)

def p3_c(x: set, y: set, z: set) -> set:
    return x.union(y, z) - x.intersection(y) - x.intersection(z) - y.intersection(z)

def p4_a() -> np.array:
    n = 1 #knight
    p = 2 #pawn
    arr = np.array([[n, n, n, n, n],
                    [n, 0, 0, 0, n],
                    [n, 0, p, 0, n],
                    [n, 0, 0, 0, n],
                    [n, n, n, n, n]])
    return arr

def p4_b(x: np.array) -> list:
    PAWN = 2 #to avoid magic numbers. PAWN is defined by 2
    row = 0  
    col = 1 
    min_row = 0
    min_col = 0
    MAX_ROW = (np.size(x, row)) - 1
    MAX_COL = (np.size(x, col)) - 1
    p_loc = np.where(x == PAWN) #p_loc stands for pawn location
    p_row = int(p_loc[row])
    p_col = int(p_loc[col])

    topTopLeftIndex = (p_row - 2, p_col - 1)
    topTopRightIndex = (p_row - 2, p_col + 1)
    topLeftIndex = (p_row - 1, p_col - 2)
    topRightIndex = (p_row - 1, p_col + 2)
    botLeftIndex = (p_row + 1, p_col - 2)
    botRightIndex = (p_row + 1, p_col + 2)
    botBotLeftIndex = (p_row + 2, p_col - 1)
    botBotRightIndex = (p_row + 2, p_col + 1)

    indices = [topTopLeftIndex, topTopRightIndex, topLeftIndex, topRightIndex, botLeftIndex, botRightIndex, botBotLeftIndex, botBotRightIndex]
    real_indices = []

    for i in indices:
        if i[row] >= min_row and i[row] <= MAX_ROW and i[col] >= min_col and i[col] <= MAX_COL:
            real_indices.append(i)

    return real_indices

def p5_a(x: dict) -> int:
    iso = 0  
    for i in x:
        if len(x.get(i)) == 0:
            iso += 1

    return iso

def p5_b(x: dict) -> int:    
    not_iso = 0  
    for i in x:
        if len(x.get(i)) != 0:
            not_iso += 1

    return not_iso

def p5_c(x: dict) -> list:
    unique = []
    for i in x:
        for j in x.get(i):
            edge = (i, j)
            if (j, i) not in unique:
                unique.append(edge)    
    return unique

def p5_d(x: dict) -> np.array:
    lettersToNum = {}
    num = 0
    for i in x:
        print(i)
        lettersToNum.update({i : num})
        num += 1

    matrix = np.zeros((len(lettersToNum), len(lettersToNum)), dtype = int)

    for i in x:
        for j in x.get(i):
            matrix[lettersToNum.get(i), lettersToNum.get(j)] = 1

    return matrix

#Question 6
class PriorityQueue(object):
    def __init__(self):
        self.arr = []
        self.prices = {'apple' : 5.0, 'banana' : 4.5, 'carrot' : 3.3, 'kiwi' : 7.4, 'orange' : 5.0, 'mango' : 9.1, 'pineapple' : 9.1}
        pass

    def push(self, x):
        index = 0
        for i in self.arr:
            if self.prices.get(x) > self.prices.get(i):
                self.arr.insert(index, x)
                return
            index += 1

        self.arr.append(x)

    def pop(self):
        assert len(self.arr) > 0, "Error: Popped empty queue"

        return self.arr.pop(0)

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print(p1(k=8))
    print('-----------------------------')
    print(p2_a(x=[], y=[1, 3, 5]))
    print(p2_b(x=[2, 4, 6], y=[]))
    print(p2_c(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print(p2_d(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print('------------------------------')
    print(p3_a(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_b(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_c(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print('------------------------------')
    print(p4_a())
    print(p4_b(p4_a()))
    print('------------------------------')
    graph = {
        'A': ['D', 'E'],
        'B': ['E', 'F'],
        'C': ['E'],
        'D': ['A', 'E'],
        'E': ['A', 'B', 'C', 'D'],
        'F': ['B'],
        'G': []
    }
    print(p5_a(graph))
    print(p5_b(graph))
    print(p5_c(graph))
    print(p5_d(graph))
    print('------------------------------')
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('kiwi')
    pq.push('orange')
    while not pq.is_empty():
        print(pq.pop())




















