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

    def insert(self, value):
        if value > self.value and self.right == None:
            self.right = Node(value)
        if value > self.value and self.right is not None:
            self.right.insert(value)
        if value < self.value and self.left == None:
            self.left = Node(value)
        if value < self.value and self.left is not None:
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
r = [1,5,4,3,2]

def leftrotation(r, l):
    for i in range(l+1):
        m = r.pop(0)
        r.insert(len(r), m)
    print(r)

y = leftrotation(r, 5)
print y

# leftrotation(a, 4)

# --------------- Stacks --------------------- #

# expn = "{((})]]"
# ano = "{()({})}"

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
            # print("{0} <= {1}".format(arr[stk[len(stk)-1]], arr[i]))
            stk.pop()
        if (len(stk) == 0):
            n[i] += 1
        else:
            n[i] = i - stk[len(stk)-1]
        stk.append(i)
        i += 1
    return n

# n = stkmaxspna(r)

# print(n)
# -------------------------------------------- #


def maxspan(you):
    h = [0]*len(you)
    h[0] = 0
    i = 0
    s = len(you)
    while i < s:
        h[i] = 1
        j = i - 1
        while j >= 0 and you[i] > you[j]:
            h[i] += 1
            j -= 1
        i += 1
    return h

k = maxspan(r)
# print(k)

a = "aaaaba"
# print(len(a))
def palindrome(str):
    for i in range(len(str)):
        t = str[:i] + str[i+1:] # we basically want to grab only len -1 elements so one element will always be missing.
        # print(t)
        if t == t[::-1]: # this is how to reverse an array
            return True
    return False

l = palindrome(a)
# print(l)

j = 4

def howmany(n):
    if n == 1:
        return 1
    else:
        k = ["0"]*n
        k[0] = "1"
        l = ""
        for i in range(len(k)-1):
            j = 0
            c = 1
            while j <= len(k[i]):
                if len(k[i]) == 0:
                    k[i] += "11"
                elif k[i][i-1] == k[i][j-1]:
                    c += 1
                else:
                    l += str(c) + str(j-1)
                    c = 0
                j += 1
            k[i] = l
            # print(k)
# for i in range(len(a)):

# howmany(j)

# S = [1, 0, -1, 0, -2, 2]
# moo = 0

s = "abaa"
t = "baab"
p = t.count(s[1])
# print(p)
def anagram(s, t):
    state = False
    if len(s) is not len(t):
        return False

    for i in range(len(s)):
        if s.count(s[i]) - t.count(s[i]) == 0:
            state = True
        else:
            return False
    return state

h = anagram(s, t)
print(h)

def reverseString():
    s = "hello world"
    n = ""
    m = s.split(" ")[::-1]
    for i in m:
        n += i + " "
    print(n)

u = "hello world"

def stackreverse(u):
    stk = []
    new = ""
    word = u.split(" ")
    for i in word:
        stk.append(i)
    print(stk)
    for i in range(len(stk)):
        new += stk.pop() + " "
    print(new.strip())

stackreverse(u)


non = [1,2,3,4,5,5,6,7,8,9]
def duplicate(o):
    for i in range(len(non)-1):
        if non[i] == non[i+1]:
            return non[i]
    return "no duplicate"

po = duplicate(non)
# print(po)



max = [10,7,4,3,2,5,8,11]

def maxprofits(max):
    new = []
    for i in range(len(max)):
        count = 0
        j = i
        while max[i] > max[j-1]:
            j -= 1
            count += 1
        new.append(count)
    print(new)

maxprofits(max)


expn = "{((})]]"
ano = "{(({}))}"


class Stack:

    def __init__(self, items):
        self.items = []

    def popLast(self, items):
        return self.items.pop()

    def pushLast(self, items, value):
        return self.items.append(value)

    def length(selfs, items):
        return len(items)

class Node2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, num):
        if num < self.value and self.left is not None:
            self.left.insert(num)
        if num > self.value and self.right is not None:
            self.right.insert(num)
        if num < self.value and self.left is None:
            self.left = Node(num)
        if num > self.value and self.right is None:
            self.right = Node(num)

class Tree2:

    def __init__(self, inputt):
        if len(inputt) == 0:
            return
        else:
            self.parent = Node(inputt[0])
            for i in inputt[0:]:
                self.parent.insert(i)

    def maxintree(self):
        if self.parent == None:
            return "no parent"
        else:
            return self.getMax(self.parent)

    def getMax(self, node):
        if node.right == None:
            return node.value
        else:
            return self.getMax(node.right)

    def DFS(self, g, v):
        g.append(v)
        if v.left is not None:
            if v.left not in g:
                self.DFS(g, v.left)
        if v.right is not None:
            if v.right not in g:
                self.DFS(g, v.right)

tre2 = Tree2([1,3,5,2,9])
print(tre2.getMax(tre2.parent))

maxy = [8,7,4,3,2,1]

def maxreturn(m):
    min = m[0]
    max = m[0]
    for i in range(len(maxy)-1):
        if maxy[i+1] < maxy[i]:
            if maxy[i+1] < min:
                min = maxy[i + 1]
        else:
            max = maxy[i+1]
    return max - min

y = maxreturn(maxy)
print(y)


ex = [1,2,2,3,3,3,2,4]
r = [1,2,2,2,4]
# ex[-5:-2] = []
r[-4:-1] = []
# print(ex, r)

def connectthree(new):
    arr = new
    print(arr)
    c = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            c += 1
            if c == 2:
                print(-i-1, -i+2, i, i+1)
                arr[-i-1:-i+2] = []
                connectthree(arr)
                return
        else:
            c = 0
    return arr
#
# l = connectthree(ex)
# print(l)


upto = 30
def fib(upto):
    arr = [1]
    total = arr[0]
    def recur(arr, total):
        print(arr)
        if len(arr) == upto:
            return arr
        else:
            arr.append(total)
            h = arr[len(arr)-1] + arr[len(arr)-2]
            recur(arr, h)
        return arr

    po = recur(arr, total)
    return po

po = fib(upto)
print(po)

