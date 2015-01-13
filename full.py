turn ="red"
jump=0
listOfNodes = []

''' BLACK on TOP

1  - 2  - 3  - 4  (BLACK)
5  - 6  - 7  - 8  (BLACK)
9  - 10 - 11 - 12 (BLACK)
13 - 14 - 15 - 16
17 - 18 - 19 - 20
21 - 22 - 23 - 24 (RED)
25 - 26 - 27 - 28 (RED)
29 - 30 - 31 - 32 (RED)
(MAP OF BOARD)

'''

class Node():
    row = None
    col = None
    upLeft = None
    upRight = None
    downRight = None
    downLeft = None
    colour = None
    king = False

class CheckersGame():
    def __init__(self):
        self.turn ="red"
        self.jump=0
        self.listOfNodes = []
        
    ############## INTERFACE FUNCTIONS ################

    def startGame(self):
        self.setup_board()

    def possible_moves(self):
        ## Returns a move (e.g [20,22] (square))
        self.jump=0
        moves=[]
        jumps_moves=[]
        listOfMoves = []

        for nodeRow in listOfNodes:
            for area in nodeRow:
                if area.colour == turn:
                    tempMoves=check_node_move(area)
                    if self.jump == 0:
                        moves.append(tempMoves)
                    else:
                        jumps_moves.append(tempMoves)

        if self.jump == 0:
            listOfMoves = moves
        else:
            listOfMoves = jumps_moves

        return self.listOfMoves

    def get_states_for_list_of_moves(self, listOfMoves):
        for move in listOfMoves:
            self.move_here(move)
            ## do calculations
            # 1. num black pieces
            # 2. num black kings
            # 3. num red pieces
            # 4. num red kings
            # 5. num black pieces threatened
            # 6. num red pieces threatened

            

            self.undo_move(move)

    def move_here(self, move):
        ## make sure the move is in list_of_possible_moves
        if move in self.listOfMoves:
            oldNode = get_node_for_square(move[0])
            newNode = get_node_for_square(move[1])

            if self.jump == 1:
                if oldNode.upLeft.upLeft == newNode:
                    oldNode.upLeft.colour = None
                    oldNode.upLeft.king = None
                elif oldNode.upRight.upRight == newNode:
                    oldNode.upRight.colour = None
                    oldNode.upRight.king = None
                elif oldNode.downLeft.downLeft == newNode:
                    oldNode.downLeft.colour = None
                    oldNode.downLeft.king = None
                else:
                    oldNode.downRight.colour = None
                    oldNode.downRight.king = None

            newNode.king = oldNode.king
            oldNode.king = None

            newNode.colour =  oldNode.colour
            oldNode.colour =  None

            return True
        return False


    ############## INTERNAL FUNCTIONS###############

    def setup_board(self):
        for i in range(8):
            row = []
            for j in range(4):
                newNode = Node()
                newNode.row = i
                newNode.col = j
                if i < 3:
                    newNode.colour = "black"
                if i > 4:
                    newNode.colour = "red"
                row.append(newNode)
            self.listOfNodes.append(row)
                
        for i in range(8):
            for j in range(4): 
                upBorder = False
                downBorder = False
                leftBorder = False
                rightBorder = False
                if i == 0:
                    upBorder = True
                if i == 7:
                    downBorder = True
                if j == 0:
                    leftBorder = True
                if j == 3:
                    rightBorder = True
                if not upBorder:
                    if not leftBorder:
                        upLeft = self.listOfNodes[i-1][j-1]
                    if not rightBorder:
                        upRight = self.listOfNodes[i-1][j+1]
                if not downBorder:
                    if not leftBorder:
                        downLeft = self.listOfNodes[i+1][j-1] 
                    if not rightBorder:
                        downRight = self.listOfNodes[i+1][j+1]

    def create_output_file(self):
        pass
    
    def is_piece_threatened(self):
        pass


    def check_node_move(self, area):
        if area.king == True:
            pass   
    # This checks if the move you're about to make is valid

    def get_square_for_node(self, node):
        return (node.row*4 + node.col + 1)

    def get_node_for_square(self, square):
        return self.listOfNodes((square-1)/4,(square-1)%4)

    def save_move(self):
        pass

    def undo_move(self, move):
        self.move_here([move[1],move[0]])

    