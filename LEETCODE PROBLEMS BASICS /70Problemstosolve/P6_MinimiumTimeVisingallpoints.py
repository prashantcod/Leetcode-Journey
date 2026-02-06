#! Minimium Time Visiting all points 
def MinimiumTime(points):
  result = 0
  x1 , y1 = points.pop(0)
  print(x1,y1)
  while points: 
    x2 ,y2 = points.pop()
    result += max(abs(y2-y1),abs(x2-x1))
    x1,y1 = x2,y2 
  return result
  
points = [[1,1],[3,4],[-1,0]]
sol = MinimiumTime(points)
print(sol)