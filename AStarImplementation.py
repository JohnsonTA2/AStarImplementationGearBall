import heapq
import GearBallClass
import copy

tree = []
ourHeap = []

face = 0

class treeNode:
    def __init__(self, puzzleState, puzzleVal):
        self.puzzleState = puzzleState
        self.hVal = puzzleVal
        self.gVal = 0
        self.fVal = self.hVal + self.gVal

        self.transformation = None
        self.parentPointer = None

    def assignTransformation(self, instruction):
        self.transformation = instruction

    def assignParent(self, parentState):
        self.parentPointer = parentState

    def setDepth(self):
        self.gVal = self.parentPointer.gVal + 1
        self.fVal = self.hVal + self.gVal

    def __lt__(self, other):
        if(self.fVal < other.fVal):
            return True
        else:
            return False

def retrieve_path(currentNode):
    our_moves = []
    print("Number of Turns: ", currentNode.gVal)
    while currentNode.parentPointer != None:
        our_moves.append(currentNode.transformation)
        currentNode = currentNode.parentPointer
    return our_moves


def AStar(gearball):
    rootTreeNode = treeNode(gearball, gearball.smarty_heuristic())
    heapq.heappush(ourHeap, (rootTreeNode))
    nodes_expanded = 0
    while len(ourHeap) != 0:
        currentNode = heapq.heappop(ourHeap)
        if currentNode.hVal == 0:
            return retrieve_path(currentNode), nodes_expanded
        else:
            nodes_expanded += 1
            #create children in tree
            #move 1
            newGearBallOne = copy.deepcopy(currentNode.puzzleState)
            newGearBallOne.center_third_still_left_up(face)
            newTreeNodeOne = treeNode(newGearBallOne, newGearBallOne.smarty_heuristic())
            newTreeNodeOne.assignTransformation(0)
            newTreeNodeOne.assignParent(currentNode)
            newTreeNodeOne.setDepth()
            #move 2
            newGearBallTwo = copy.deepcopy(currentNode.puzzleState)
            newGearBallTwo.center_third_still_right_up(face)
            newTreeNodeTwo = treeNode(newGearBallTwo, newGearBallTwo.smarty_heuristic())
            newTreeNodeTwo.assignTransformation(1)
            newTreeNodeTwo.assignParent(currentNode)
            newTreeNodeTwo.setDepth()
            #move 3
            newGearBallThree = copy.deepcopy(currentNode.puzzleState)
            newGearBallThree.center_third_still_top_left(face)
            newTreeNodeThree = treeNode(newGearBallThree, newGearBallThree.smarty_heuristic())
            newTreeNodeThree.assignTransformation(2)
            newTreeNodeThree.assignParent(currentNode)
            newTreeNodeThree.setDepth()
            #move 4
            newGearBallFour = copy.deepcopy(currentNode.puzzleState)
            newGearBallFour.center_third_still_top_right(face)
            newTreeNodeFour = treeNode(newGearBallFour, newGearBallFour.smarty_heuristic())
            newTreeNodeFour.assignTransformation(3)
            newTreeNodeFour.assignParent(currentNode)
            newTreeNodeFour.setDepth()
            #move 5
            newGearBallFive = copy.deepcopy(currentNode.puzzleState)
            newGearBallFive.front_move_clockwise(face)
            newTreeNodeFive = treeNode(newGearBallFive, newGearBallFive.smarty_heuristic())
            newTreeNodeFive.assignTransformation(4)
            newTreeNodeFive.assignParent(currentNode)
            newTreeNodeFive.setDepth()
            #move 6
            newGearBallSix = copy.deepcopy(currentNode.puzzleState)
            newGearBallSix.front_move_counter_clockwise(face)
            newTreeNodeSix = treeNode(newGearBallSix, newGearBallSix.smarty_heuristic())
            newTreeNodeSix.assignTransformation(5)
            newTreeNodeSix.assignParent(currentNode)
            newTreeNodeSix.setDepth()

            #enheap children

            heapq.heappush(ourHeap, (newTreeNodeOne))
            heapq.heappush(ourHeap, (newTreeNodeTwo))
            heapq.heappush(ourHeap, (newTreeNodeThree))
            heapq.heappush(ourHeap, (newTreeNodeFour))
            heapq.heappush(ourHeap, (newTreeNodeFive))
            heapq.heappush(ourHeap, (newTreeNodeSix))
