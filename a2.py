class min_heap:
    def _init_(self):
        self.heap = []
    def root_key(self):
        return self.heap[0]
    def parent(self, i):
        return (i-1)//2
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def is_leaf(self, i):
        return 2*(i+1) > len(self.heap)
    def heap_up(self, u):
        v = u
        while self.heap[self.parent(v)] > self.heap[v]:
            self.swap(self.parent(v), self.heap[v])
            v = self.parent(v)
    def heap_down(self, u):
        v = u
        while not self.is_leaf(v):
            if 2*(u+1) == len(self.heap):
                if self.heap[v] > self.heap[self.left_child(v)]:
                    self.swap(self.left_child(v), v)
                v = self.left_child(v)                  
            elif (self.heap[v] > self.heap[self.left_child(v)] or self.heap[v] > self.heap[self.right_child(v)]):
                if self.heap[self.left_child(v)] < self.heap[self.right_child(v)]:
                    self.swap(self.left_child(v), v)
                    b = self.left_child(v) 
                else:
                    self.swap(self.right_child(v), v)
                    b = self.right_child(v)
                v = b
    def enqueue(self, a):
        self.heap.append[a]
        self.heap_up(len(self.heap) - 1)
    def extract_min(self):
        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_down(0)
        return x
    def fast_buildheap(self, l):
        self.heap = l
        for k in range(len(self.heap)-1, 0, -1):
            self.heap_down(k)
        self.heap_down(0)



def v1_calci(m1,m2,v1,v2):
    return ((m1-m2)/(m1+m2))*v1 + 2*(m2/(m1+m2))*v2
def v2_calci(m1,m2,v1,v2):
    return 2*(m1/(m1+m2))*v1-((m1-m2)/(m1+m2))*v2


def listCollisions(M, x, v, m, T):
    n = len(M)
    init_tuples = []
    for i in range(n - 1):
        if v[i + 1] - v[i] < 0:
            init_tuples.append(((x[i + 1] - x[i])/(v[i] - v[i+1]), i,1))
    s = min_heap()
    s.fast_buildheap(init_tuples)
    ans = []
    if len(s.heap) != 0:
        l = [0]*n
        time = 0
        k = 1
        collisionCounter = 0
        a = [0]*(n-1)
        while collisionCounter < m and time < T:
        
            if len(s.heap) == 0:
                break
            k += 1

            (t, i,zoro) = s.extract_min()
            if(t > T or collisionCounter > m):
                break
            
            if(zoro > a[i]):
                collisionCounter += 1
                a[i] = zoro
                x[i] += v[i]*(t-l[i])
                v[i] = v1_calci(M[i],M[i+1],v[i],v[i+1])
                l[i] = t
                
                time = t
                ans.append((round(t, 4), i, round(x[i], 4)))

                x[i+1] += v[i+1]*(t-l[i+1])
                v[i+1] = v2_calci(M[i],M[i+1],v[i],v[i+1])
                l[i+1] = t
                
                if i-1 >= 0:
                    if v[i]-v[i-1] < 0:
                        t1 = time + (x[i]+v[i]*(t-l[i])-(x[i-1]+v[i-1]*(t-l[i-1])))/(v[i-1]-v[i])
                        s.heap.append((t1, i-1,k))
                        s.heap_up(len(s.heap)-1)
                        k+=1

                if i+3 <= n:
                    if v[i+2]-v[i+1] < 0:
                        t2 = time +(x[i+2]+v[i+2]*(t-l[i+2])-(x[i+1]+v[i+1]*(t-l[i+1])))/(v[i+1]-v[i+2])
                        s.heap.append((t2, i+1,k))
                        s.heap_up(len(s.heap)-1)   
                        k+=1

    return(ans)




















































    


        
            


