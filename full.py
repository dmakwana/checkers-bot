turn ="red"
jump=0
listOfNodes = []

''' BLACK on TOP

1  - 2  - 3  - 4 (BLACK)
5  - 6  - 7  - 8 (BLACK)
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
        self.listOfMoves = []

    ############## INTERFACE FUNCTIONS ################

    def startGame(self):
        self.setup_board()

    def possible_moves(self):
        ## Returns a move (e.g 20-22 (square))
        moves=[]
        jumps_moves=[]
        
        for nodeRow in listOfNodes:
            for area in nodeRow:
                if area.colour == turn:
                    tempMoves=check_node_move(area)
                    if self.jump == 0:
                        moves.append(tempMoves)
                    else:
                        jumps_moves.append(tempMoves)

        if self.jump == 0:
            self.listOfMoves = moves
        else:
            self.listOfMoves = jumps_moves

        return self.listOfMoves

    def get_state_for_move(self):
        pass

    def move_here(self, move):
        ## make sure the move is in list_of_possible_moves
        if move in self.listOfMoves:
            newNode = get_node_for_square(move[1])
            oldNode = get_node_for_square(move[1])

            newNode.king = oldNode.king
            oldNode.king = None

            newNode.colour =  oldNode.colour
            oldNode.colour =  None

            return -1
        return 0


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

    
    