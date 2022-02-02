# https://leetcode.com/problems/number-of-boomerangs/

def numberOfBoomerangs(points):
    count = 0
    for point in points:
        pointMap = {}
        for secondPoint in points:
            x = point[0]-secondPoint[0]
            y = point[1]-secondPoint[1]
            dist = x**2+y**2
            if dist not in pointMap:
                pointMap[dist] = 0
            pointMap[dist] +=1
        
        for key,k in pointMap.items():
            count+= k*(k-1)
    
    return count

print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))