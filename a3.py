def merger(a, b):
    list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i][1] < b[j][1]:
            list.append(a[i])
            i += 1
        else:
            list.append(b[j])
            j += 1  
    while i < len(a):
        list.append(a[i])
        i += 1
    while j < len(b):
        list.append(b[j])
        j += 1
    return list

class node:
    def __init__(self, key, left, right, ylist):
        self._key = key
        self._left = left
        self._right = right
        self._ylist = ylist
    def ylist(self):
        return self._ylist
    def leftchild(self):
        return self._left
    def rightchild(self):
        return self._right
    def isleaf(self):
        return self._left==None and self._right==None
    def key(self):
        return self._key
    
def searchbranch(data, xmin, xmax):
    if data.isleaf():
        return data
    elif data.key()[0] < xmin or data.key()[0] == xmin:
        return searchbranch(data.rightchild(), xmin, xmax)
    elif data.key()[0] > xmax or data.key()[0] == xmax:
        return searchbranch(data.leftchild(), xmin, xmax)
    else:
        return data


def min(first, last, x, a):
    ans = -1
    while first <= last:
        mid = first + (last - first + 1)//2
        Value = a[mid][1]
        if Value < x:
            first = mid+1
        elif Value > x:
            ans = mid
            last = mid-1
        elif Value == x:
            first = mid+1
    return ans

def max(first, last, x, a):
    ans = -1
    while first <= last:
        mid = first + (last - first + 1)//2
        Value = a[mid][1]
        if Value < x:
            ans = mid
            first = mid+1
        elif Value > x:
            last = mid-1
        elif Value == x:
            last = mid-1
    return ans
 

def solve(list, ymin, ymax):
    ans = []
    n = len(list)
    min_index = min(0, n-1, ymin, list)
    max_index = max(0, n-1, ymax, list)
    if min_index == -1 or max_index == -1:
        return ans
    else:
        i = min_index
        while i < max_index + 1:
            ans.append(list[i])
            i += 1
    return ans



 
def finalsearcherleft(node, xmin, xmax, ymin, ymax):
    if node.isleaf():
        if xmin<node.key()[0]<xmax and  ymin<node.key()[1]<ymax:
            return [node.key()]
        else:
            return []
    elif xmin<node.key()[0]<xmax:
        x=solve(node.rightchild().ylist(),ymin, ymax)
        x.extend(finalsearcherleft(node.leftchild(), xmin, xmax, ymin, ymax))
        return x
    else:
        return finalsearcherleft(node.rightchild(), xmin, xmax, ymin, ymax)
    

def finalsearcherright(node, xmin, xmax, ymin, ymax):
    if node.isleaf():
        if xmin<node.key()[0]<xmax and  ymin<node.key()[1]<ymax:
            return [node.key()]
        else:
            return []
    elif xmin<node.key()[0]<xmax:
        x=solve(node.leftchild().ylist(),ymin, ymax)
        x.extend(finalsearcherright(node.rightchild(), xmin, xmax, ymin, ymax))
        return x
    else:
        return finalsearcherright(node.leftchild(), xmin, xmax, ymin, ymax)

  
def rooter(list, i, j):
    if i-j==1:
        return node(None ,None, None, None)
    elif i-j==0:
        x = node(list[i-1], None, None,[list[i-1]])
    else:
        a = rooter(list,i,(i+j)//2)
        b = rooter(list,((i+j)//2)+1,j)        
        x = node(list[((i+j)//2)-1],  a , b, merger(a.ylist(),b.ylist()))
    return x




    
class PointDatabase:
    def __init__(self, pointlist):         
        self.xlist =sorted(pointlist)
        n = len(self.xlist)
        self.data = rooter(self.xlist, 1, n)
    def searchNearby(self, q, d):
        xmin = q[0]-d
        ymin = q[1]-d
        xmax = q[0]+d
        ymax = q[1]+d
        if len(self.xlist)==1:
            if xmin<self.xlist[0][0]<xmax and ymin<self.xlist[0][1]<ymax:
                return self.xlist
            else:
                return []
        elif len(self.xlist) == 0:
            return []
        else:
            if searchbranch(self.data, xmin, xmax).isleaf():
                if xmin<searchbranch(self.data, xmin, xmax).key()[0]<xmax and  ymin<searchbranch(self.data, xmin, xmax).key()[1]<ymax:
                    return [searchbranch(self.data, xmin, xmax).key()]
                else:
                    return []
            else:
                k=finalsearcherleft(searchbranch(self.data, xmin, xmax).leftchild(), xmin, xmax, ymin, ymax)
                k.extend(finalsearcherright(searchbranch(self.data, xmin, xmax).rightchild(), xmin, xmax, ymin, ymax))
                return k



