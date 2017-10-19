#too easy fam...

def SumList(arr):
    size = 0
    index = 0
    while index < len(arr):
        size += arr[index]
        index += 1
    return size

#basic search

def searchForNumber(cls, num, arr):
    n = num
    i = 0
    a = arr
    s = len(arr)
    while i < s:
        if a[i] == num:
            return ("index", i)
        else:
            i += 1
    return False


#sear = searchForNumber(8, [1,10,8,4,5])

#binary search

def binary(n, arr):
    l = 0
    o = 0
    h = len(arr)-1
    while l <= h:
        o = (l+(h - l)/2)
        j = ("({0} = {1} + ({2} - {3})/2)").format(o, l, h, l)
        print(j)
        if n == arr[o]:
            return True
        else:
            if n < arr[o]:
                h = o - 1
            else:
                l = o + 1
    return False

# k = binary(6,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# print(k)

def sort(arr):
    newarr = []
    c = 0
    for i in arr:
        c += 1 #1, 2
        l = c - 1 #1, 2
        while l >= 0:
            if c - 1 == 0: #0
                newarr.append(i)
                break
            length = len(newarr)
            decre = length-(length-l)
            if i[k] > newarr[decre-1][k]:
                newarr.insert(l, i)
                l = -1
            else:
                if l == 0:
                    newarr.insert(0, i)
                    break
                l -= 1
    for i in newarr:
        print(" ".join(str(x) for x in i))

class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.visited = None

    def insert(self, value):
        if value > self.value and self.right == None:
            self.right = Node(value)
        if value > self.value and self.right != None:
            self.right.insert(value)
        if value < self.value and self.left == None:
            self.left = Node(value)
        if value < self.value and self.left != None:
            self.left.insert(value)

class Tree:
    def __init__(self, treearray):
        self.treearray = treearray
        if len(treearray) == 0:
            self.parent = None
        else:
            self.parent = Node(treearray[0])
            for i in treearray[0:]:
                self.parent.insert(i)

    def max(self):
        if self.parent == None:
            print("tree is empty mofo")
        else:
            return self.getMax(self.parent)

    def getMax(self, node):
        if node.right == None:
            return node.value
        if node.right != None:
            return self.getMax(node.right)

    def insertbigger(self, value):
        if self.parent == None:
            self.parent = Node(value)
        else:
            self.parent.insert(value)

    def DFS(self, G, V):
        G.append(V)
        print(V.value)
        if V.left is not None:
            if V.left not in G:
                self.DFS(G, V.left)

        if V.right is not None:
            if V.right not in G:
                self.DFS(G, V.right)

# searchDFS = Tree([5, 3, 7, 10])
# print(searchDFS.max())
# parentof = searchDFS.parent
# searchDFS.DFS([], parentof)


arr = [3,4,11,33,0]

def largestprofit(mon):
    j = len(mon)
    c = 0
    dif = 0
    while j > 0:
        for i in arr[c:len(mon)]:
            if arr[c] < (i):
                if i - arr[c] > dif:
                    dif = i - arr[c]
        j -= 1
        c += 1
    print(dif)

# largestprofit(arr)

message = 'find you will pain only go you recordings security the into if'

def reversewords(word):
    m = word.split(' ')
    l = ''
    for i in range(len(m)):
        l += m[len(m)-1-i] + ' '
    print(l)
# reversewords(message)
# print(searchmax.max())


o = 100
i = 2

# def recursivepowers(p, m, counter, rangee):
#     if n == m:
#         return counter
#     else:
#         d = 0
#         for i in range(root):
#             d += i**2
#             if d == 100:
#                 counter += 1
#                 recursivepowers(2, 100, counter, root-1)

# recursivepowers(2, 100, 0, range(1, 10))
a = [1,2,3,4,5]
for i in range(len(a)-1):
    m = a.pop(0)
    a.insert(5, m)
    # print(a)


def leftrotation(r, l):
    for i in range(l+1):
        m = r.pop(0)
        r.insert(len(r), m)
    print(r)

# leftrotation(a, 4)

# --------------- Stacks --------------------- #

expn = "{((})]]"
ano = "{()({})}"

def isbalanced(inp):
    l = []
    for i in inp:
        if i == "{" or i == "(" or i == "[":
            l.append(i)
            # print(l)
        elif i == "}":
            print(l, "before")
            if l.pop() != "{":
                return False
            print(l, "after")
        elif i == ")":
            print(l, "before")
            if l.pop() != "(":
                return False
            print(l, "after")
        elif i == "]":
            print(l, "before")
            if l.pop() != "[":
                return False
            print(l, "after")
    return len(l) == 0

# m = isbalanced(expn)
# print(m)

# given a list of daily stock price in a list A[i], find the span of the stock for each day. A span of stock
# is the max number of days for which the price of the stock was lower than that day
# eg [10, 8, 5, 3, 1, 4, 6, 9, 11] so 8 is day 2 and would be 0 and would also be 0 for 5, 3, 1 however 4 which is day 6
# is greater than 1 and 3 so day 5 and 4 therefore its span is 2

r = [10, 8, 5, 3, 1, 4, 6, 9, 11]

def stkmaxspna(arr):
    stk = []
    size = len(arr)
    n = [0]*size
    stk.append(0)
    n[0] = 1
    i = 1
    while i < size:
        while len(stk) != 0 and arr[stk[len(stk)-1]] <= arr[i]:
            print("{0} <= {1}".format(arr[stk[len(stk)-1]], arr[i]))
            stk.pop()
        if (len(stk) == 0):
            n[i] += 1
        else:
            n[i] = i - stk[len(stk)-1]
        stk.append(i)
        i += 1
    return n

n = stkmaxspna(r)

# print(n)
# -------------------------------------------- #


def maxspan(arr):
    n = [0]*len(arr)
    n[0] = 0
    i = 1
    s = len(arr)
    while i < s:
        n[i] = 0
        j = i - 1
        while j >= 0 and arr[i] > arr[j]:
            n[i] += 1
            j -= 1
        i += 1
    return n
# print(n)
