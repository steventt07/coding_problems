class Location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def generate_moves(Location,n):
    rightDaig = []
    leftDaig = []
    RD = Location.y-Location.x
    LD = Location.y+Location.x
    for x in range(1,n+1):
        if 0<x+RD<=n:
            rightDaig.append([x,x+RD])
        if 0<LD-x<=n:
            leftDaig.append([LD-x,x])
    return(rightDaig,leftDaig)
n = 4
rightDaig,leftDaig = generate_moves(Location(1,1),n)
print(rightDaig)
print(leftDaig)
U = n
D = 1
R = n
L = 1
if len(leftDaig)==0:
    UL,DR = 0,0
else:
    UL = leftDaig[0][0]
    DR = leftDaig[-1][0]
if len(rightDaig)==0:
    UR,DL = 0,0
else:
    UR = rightDaig[-1][1]
    DL = rightDaig[0][1]
Queen = Location(2,2)
obstacles = []
for x in range(len(obstacles)):
        Obstical = Location(obstacles[x][0],obstacles[x][1])
        if Queen.x == Obstical.x:
            if Obstical.y > Queen.y:
                if min(U,Obstical.y) == Obstical.y:
                    U = Obstical.y-1
            else:
                if max(D,Obstical.y) == Obstical.y:
                    D = Obstical.y+1
        elif Queen.y == Obstical.y:
            if Obstical.x > Queen.x:
                if min(R,Obstical.x) == Obstical.x:
                    R = Obstical.x-1
            else:
                if max(L,Obstical.x)==Obstical.x:
                    L = Obstical.x+1
        elif abs(Queen.x-Obstical.x) == abs(Queen.y-Obstical.y):
            if (Queen.x+Queen.y) == (Obstical.x+Obstical.y):
                if Obstical.x > Queen.x:
                    if min(UL,Obstical.x) == Obstical.x:
                        UL = Obstical.x-1
                else:
                    if max(DR,Obstical.x) == Obstical.x:
                        DR = Obstical.x+1
            else:
                if Obstical.x > Queen.x:
                    if min(UR,Obstical.y) == Obstical.y:
                        UR = Obstical.y-1
                else:
                    if max(DL,Obstical.y) == Obstical.y:
                        DL = Obstical.y+1
total = (U-D)+(R-L)+(UR-DL)+(UL-DR)
print(U,D)
print(R,L)
print(UR,DL)
print(UL,DR)
print(total)