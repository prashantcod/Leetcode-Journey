#! Check if it's a Straight Line : 

def Checking(coordinates):
    (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
    for x3, y3 in coordinates[2:]:
		    if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
			         return False
    return True
      

coordinates = [[0,0],[0,1],[0,-1]]
value =Checking(coordinates)
print(value)