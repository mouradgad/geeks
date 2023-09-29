import math
type = "concave"
R=3,521
if type == "concave":
    print (math.floor(R/2))
elif type == "convex":
    print (math.floor(-(R/2)))