import sys

def read(fnm,db):
  """
  read file fnm into dictionary
  each line has a nodeName followed by its adjacent nodeNames
  """
  file = open(fnm)
  graph = {} #dictionary
  for line in file:
    l = line.strip().split(" ")
    if db: print("l:",l,"len(l):",len(l))
    # remove empty lines
    if l==['']:continue
    # dict: key: nodeName  value: (color, adjList of names)
    graph[l[0]]= ('white',l[1:])
  return graph

def dump(graph):
  print("dumping graph: nodeName (color, [adj list]) ")
  for node in graph:
    print(node, graph[node])

def bfs(graph,list):
  temproot = list[0][0]
#  print("list root ", temproot)
  abc = "abcdefghifklmnopqrstuvwxyz"
  result = [character for character in abc]
  root = abc.find(temproot)
#  print("num root ", root)
  visited = [False]*(len(graph))
  queue = []
  distance = []
  for i in range(len(graph)):
    distance.append(0)
  queue.append(root)
  visited[root] = True
  abc = "abcdefghifklmnopqrstuvwxyz"
  result = [character for character in abc]
  while queue:
    s = queue.pop(0)
    graph[result[s]] = ("black", graph[result[s]][1])
#    print("char ", result[s])
#    dump(graph)
    arr1 = graph[result[s]]
   # print("arr1 ", arr1)
    arr2 = arr1[0]
  #  print("arr2 ", arr2)
    arr3 = arr1[1]
  #  print("arr3 ", arr3)
    for i in arr3:
  #    print("hmmmm ", i)
  #    print("num ", ord(i) - 97)
      con = ord(i) - 97
      if visited[con] == False:
         queue.append(con)
   #      print(distance)
         distance[con] = distance[s] + 1
         list.append((result[con],distance[con]))
         visited[con] = True

  return list

def white(graph) :
  """
   paint all graph nodes white
  """
  for node in graph :
    gr[node] = ('white',gr[node][1])

def Util(u, color):
  color[u] = "gray"
#  print("starting colors", color)
#  dump(gr)
  abc = "abcdefghifklmnopqrstuvwxyz"
  result = [character for character in abc]
  gr[result[u]] = ("gray", gr[result[u]][1])
  mylist = gr[result[u]][1]
 # print(mylist)
  for v in mylist:
     str1 = ''.join(str(e) for e in v)
    # print("should be begining ", str1)
    # print(abc.find(str1))
    # print("target color", color[abc.find(str1)])
     if color[abc.find(str1)] == "gray":
      print("cycle in", v)
     if color[abc.find(str1)] == "white" and Util(abc.find(str1), color):
      return True
  color[u] = "black"
  gr[result[u]] = ("black", gr[result[u]][1])
  return False



def dfs(root):
 #   dump(gr)
    V = len(gr)
    abc = "abcdefghifklmnopqrstuvwxyz"
    newroot = abc.find(root)
   # print(newroot)
    color = ["white"] * V
    if color[newroot] == "white":
        Util(newroot, color)
     # print(newroot)


if __name__ == "__main__":
  # db: debug flag
  db = len(sys.argv)>3
  gr = read(sys.argv[1],db)
  root = sys.argv[2]
  if db: dump(gr)


  gr[root] = ('black',gr[root][1])

 # print("second elemnt  :", gr['a'])
 # print("second elemnt  :", gr['b'])
 # print("second elemnt  :", gr['d'])
  #print("second elemnt  :", gr['e'])
 # root = 'a'
  print("root key:", root)
  # don't need grey for bfs
  q = bfs(gr,[(root,0)])
  print("BFS")
  print(q)
  if db: dump(gr)
  white(gr)
  if db: dump(gr)
  print("DFS");
  dfs(root)
  if db: dump(gr)
