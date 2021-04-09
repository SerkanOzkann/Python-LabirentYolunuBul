import sys
def readFile(fileName):
  currentFile = open(fileName,"r")
  maze=[]
  while True:
    line = currentFile.readline().rstrip('\n')
    if line=='':
      break
    maze.append(line)
  return maze

#Serkan özkan
def is_reinForcement(maze,row,col):
  for i in range(row):
    for j in range(col):
      if maze[i][j]=='H':
        return True
  return False


def findBeginning(maze,row,col):
  for i in range(row):
    for j in range(col):
      if maze[i][j]=='S':
        return i,j
  return 0,0


def create2dArray(row,col):
  visitedPath = []
  for i in range(row):
    tempArray = []
    for j in range(col):
      tempArray.append(0)
    visitedPath.append(tempArray)
  return visitedPath





#Solution One (Güçlendirmeli Yolu Bulma)

def find_theReinForcementWay(maze,row,col,x,y,visitedPath,reinforced):
  visitedPath[x][y]=1

  if (reinforced==True and maze[x][y]=='F'):
      visitedPath[x][y]='F'
      return 1

  if (maze[x][y]=='H'):
    reinforced=True
    visitedPath[x][y]='H'

  if(x-1>=0 and  (maze[x-1][y]=='P' or maze[x-1][y]=='F' or maze[x-1][y]=='H') 
   and visitedPath[x-1][y] == 0 and  find_theReinForcementWay(maze,row,col,x-1,y,visitedPath,reinforced)):
    return True
  if(y-1>=0 and  (maze[x][y-1]=='P' or maze[x][y-1]=='F' or maze[x][y-1]=='H') 
  and  visitedPath[x][y-1] == 0 and find_theReinForcementWay(maze,row,col,x,y-1,visitedPath,reinforced)):
    return True
  if (x + 1 < row and (maze[x + 1][y] == 'P' or maze[x + 1][y] == 'F' or maze[x + 1][y] == 'H') 
  and visitedPath[x + 1][y] == 0 and find_theReinForcementWay(maze, row, col, x + 1, y, visitedPath, reinforced)):
    return True
  if (y + 1 < col and (maze[x][y + 1] == 'P' or maze[x][y + 1] == 'F' or maze[x][y + 1] == 'H')
   and visitedPath[x][y + 1] == 0 and find_theReinForcementWay(maze, row, col, x, y + 1, visitedPath, reinforced)):
    return True

  visitedPath[x][y]=0
  reinforced=False
  return 0




#Solution Two (Normal Yolu Bulma)

def find_theWay(maze,row,col,x,y,visitedPath):
  visitedPath[x][y]=1

  if (maze[x][y]=='F'):
      visitedPath[x][y]='F'
      return 1

  if(x-1>=0 and  (maze[x-1][y]=='P' or maze[x-1][y]=='F')  and visitedPath[x-1][y] == 0 and  find_theWay(maze,row,col,x-1,y,visitedPath)):
    return True
  if(y-1>=0 and  (maze[x][y-1]=='P' or maze[x][y-1]=='F') and  visitedPath[x][y-1] == 0 and find_theWay(maze,row,col,x,y-1,visitedPath)):
    return True
  if (x + 1 < row and (maze[x + 1][y] == 'P' or maze[x + 1][y] == 'F') and visitedPath[x + 1][y] == 0 and find_theWay(maze, row, col, x + 1, y, visitedPath)):
    return True
  if (y + 1 < col and (maze[x][y + 1] == 'P' or maze[x][y + 1] == 'F') and visitedPath[x][y + 1] == 0 and find_theWay(maze, row, col, x, y + 1, visitedPath)):
    return True

  visitedPath[x][y]=0
  return 0








if not len(sys.argv)==3:
  print("Hatalı veya eksik argüman girişi, çalıştırmak için 3 argüman lazım. Örnek Kullanım: yolbul.py guclu_girdi.txt cikti.txt")
else:
  maze = readFile(sys.argv[1])
  col = len(maze[0])
  row = len(maze)
  x,y=findBeginning(maze,row,col)
  visitedPath = create2dArray(row,col)

  if is_reinForcement(maze,row,col):
    reinforced=False
    result=find_theReinForcementWay(maze,row,col,x,y,visitedPath,reinforced)
  else:
    result=find_theWay(maze,row,col,x,y,visitedPath)

  visitedPath[x][y]='S'
  output = open(sys.argv[2],"w")

  if result==1:
    for i in range(len(visitedPath)):
      for j in range(len(visitedPath[i])):
        output.write(str(visitedPath[i][j])+", ")
      output.write("\n")
  else:
    output.write("Maalesef böyle bir yol yok...")
  output.close()