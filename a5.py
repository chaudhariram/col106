class heaper:
    def __init__(self):
        self.data1 = []
        self.data2 = []
    def parent(self, i):
        return (i-1)//2
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    def swap(self, i, j):
        self.data1[i], self.data1[j] = self.data1[j], self.data1[i]
        self.data2[self.data1[i][1]],self.data2[self.data1[j][1]] = self.data2[self.data1[j][1]],self.data2[self.data1[i][1]]
    def is_leaf(self, i):
        return 2*(i+1) > len(self.data1)
    def heap_up(self, u):
        v = u
        while v != 0:
            if self.data1[self.parent(v)][0] < self.data1[v][0]:
                self.swap(self.parent(v), v)
                v = self.parent(v)
            else:
                break
    def is_empty(self):
        return self.data1 == []
    def heap_down(self, u):
        v = u
        while not self.is_leaf(v):
            if 2*(v+1) == len(self.data1):
                if self.data1[v][0] > self.data1[self.left_child(v)][0]:
                    self.swap(self.left_child(v), v)
                    v = self.left_child(v) 
                else:
                    break

        
            elif self.data1[v][0] < self.data1[self.left_child(v)][0] and self.data1[self.right_child(v)][0] <= self.data1[self.left_child(v)][0]:
                self.swap(self.left_child(v), v)
                v = self.left_child(v) 
            elif self.data1[v][0] < self.data1[self.right_child(v)][0] and self.data1[self.left_child(v)][0] <= self.data1[self.right_child(v)][0]:
                self.swap(self.right_child(v), v)
                v = self.right_child(v)
            else:
                break

    # def enqueue(self, a):
    #     self.data1.append[a]
    #     self.heap_up(len(self.data1) - 1)
    def extract_max(self):
        x = self.data1[0]
        self.data2[x[1]] = -1
        self.data2[self.data1[-1][1]] = 0
        self.data1[0] = self.data1[-1]
        self.data1.pop()
        self.heap_down(0)
        return x
    def fast_buildheap(self, n):
        i = 0
        l = []
        z = []
        while i < n:
            l.append([0, i, -1])
            i += 1
        self.data1 = l
        for k in range(n):
            z.append(k)
        self.data2 = z
    def ispresent(self, x):
        return self.data2[x] != -1
    def search(self, x):
        return self.data2[x]
    def get_value(self, x):
        return self.data1[self.data2[x]][0]
    def change_key(self, x, y, z):
        self.data1[self.data2[x]][0] = y
        if not z == -1:
            self.data1[self.data2[x]][2] = z            
        self.heap_up(self.data2[x])
    def checkrootvertex(self,t):
        return self.data1[0][1] == t

class graph:
    def __init__(self, n, links):
        self.data = []
        for i in range(n):
            self.data.append([])
        for i in range(len(links)):
            self.data[links[i][0]].append((links[i][1],links[i][2]))
            self.data[links[i][1]].append((links[i][0],links[i][2]))
    def searchnearby(self, x):
        return self.data[x]

def findMaxCapacity(n, links, s, t):
    pathlist = []
    for i in range(n):
            pathlist.append(0)    
    k = heaper()
    k.fast_buildheap(n)
    k.change_key(s, 1, -1)
    j = k.extract_max()
    j[0]=0
    y = graph(n, links)
    for x in range(len(y.searchnearby(s))):
        if k.ispresent(y.searchnearby(s)[x][0]):
            k.change_key(y.searchnearby(s)[x][0], y.searchnearby(s)[x][1], s)
    while not k.checkrootvertex(t):
        [a,b,c] = k.extract_max()
        pathlist[b] = c
        for x in range(len(y.searchnearby(b))):
            if k.ispresent(y.searchnearby(b)[x][0]):
                if min(a,y.searchnearby(b)[x][1]) > k.get_value(y.searchnearby(b)[x][0]):
                    k.change_key(y.searchnearby(b)[x][0],min(a,y.searchnearby(b)[x][1]), b)
                else:
                    k.change_key(y.searchnearby(b)[x][0],k.get_value(y.searchnearby(b)[x][0]), -1)
    [x1,x2, x3] = k.extract_max()
    list1 = []
    o = x3
    while o != s:
        list1.append(o)
        o = pathlist[o]
    list2 = [s]
    for p in range(len(list1)-1,-1,-1):
        list2.append(list1[p])
    list2.append(t)
    return (x1, list2)





# print(findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1))
# print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
# print(findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3))
# print(findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2))
# print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))

# print(findMaxCapacity(10,[(0,1,1), (1,2,2), (2,3,3), (3,4,4), (4,5,5), (5,6,6), (6,7,7), (7,8,8), (8,9,9), (9,5,10), (8,6,11), (4,1,12), (0,6,13), (5,2,14)], 0, 5))
# print( findMaxCapacity(8, [(0,1,5), (1,2,8), (2,3,6), (3,4,1), (4,5,15), (5,6,2), (6,7,3), (7,0,12), (1,5,7), (1,6,3), (2,5,9), (2,7,11), (3,7,14), (0,4,3), (0,5,4)], 0, 4 ))
# print(findMaxCapacity(8, [(0,1,20), (0,2,30), (0,3,40), (1,2,50), (1,3,60), (1,7,140), (2,3,70), (4,5,80), (4,6,90), (4,7,100), (5,6,110), (5,7,120), (6,7,130)], 0, 6))

#FINAL SUBMIT
