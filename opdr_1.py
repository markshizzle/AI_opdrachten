
# Defines when the desired goal is reached
def isGoal(state):
    left=state[0]
    return left==set()

def getChildren(state):
    children=[]
    for item in takeovers:
        child=shipOver(state,item)
        if not child: continue
        children.append(child)
    return children

# Function to ship over the farmer with an item of choice or nothing
def shipOver(state, item):
    left,right=[set(x) for x in state[0]]
    if farmer in left:
        src,dst=left,right
    else:
        src,dst=right,left
    if item and not item in src:
        return None
    solution="The farmer travels to the right" if farmer in left else "The farmer travels to the left"
    src.remove(farmer)
    dst.add(farmer)
    if item:
        src.remove(item)
        dst.add(item)
        solution+=" with the "+item
    else:
        solution+=" alone"
    return ((left,right),solution)

# Check if the current state is possible
def checkState(state):
    for shore in state[0]:
        if farmer not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False
def printState(state,level):
    left,right=state[0]
    print (state[1], "\n",level,", ".join(left)," | ",", ".join(right), "\n")

def generateSolutions(state,level=0):
    printState(state,level)
    childs=getChildren(state)
    for child in childs:
        if checkState(child):
            continue
        if child[0] in previousstates:
            continue
        previousstates.append(child[0])
        generateSolutions(child,level+1)

# Defines the variables
farmer,goat,cabbage,wolf=("farmer","goat","cabbage","wolf")
takeovers = (cabbage,goat,wolf,None)
forbiddens=(set((goat,cabbage)), set((wolf,goat)))
# Begin state
state=((set((farmer,goat,cabbage,wolf)), set()),"")
previousstates=[state[0]]
generateSolutions(state)
