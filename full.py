import os
import time

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
class Colour():
    BLACK = 1
    RED = 2

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
        self.turn = Colour.RED
        self.jump = 0
        self.jumpNode=-0
        self.jumpColour=None
        self.jumpKing=False
        self.listOfNodes = []
        self.listOfMoves = []
        self.output_file = None

    def test_function(self):
        for row in self.listOfNodes:
            for node in row:
                print str(self.get_square_for_node(node)) + " - "
                if node:
                    if node.upRight:
                        print self.get_square_for_node(node.upRight)
                    if node.upLeft:
                        print self.get_square_for_node(node.upLeft)
                    if node.downRight:
                        print self.get_square_for_node(node.downRight)
                    if node.downLeft:
                        print self.get_square_for_node(node.downLeft)
                print "--------"
        
    ############## INTERFACE FUNCTIONS ################

    def start_game(self):
        self.setup_board()
        self.create_output_file()

    def end_game(self):
        self.output_file.close()

    def possible_moves(self):
        ## Returns a list of moves (e.g [20,22] (square))
        self.jump=0
        moves=[]
        jumps_moves=[]
        self.listOfMoves = []

        for nodeRow in self.listOfNodes:
            for piece in nodeRow:
                if piece.colour == self.turn:
                    tempMoves=self.check_node_moves(piece)
                    if self.jump == 0:
                        moves.extend(tempMoves)
                    else:
                        jumps_moves.extend(tempMoves)

        if self.jump == 0:
            self.listOfMoves = moves
        else:
            self.listOfMoves = jumps_moves

        return self.listOfMoves

    def get_states_for_list_of_moves(self, listOfMoves):
        listOfStates = []
        for move in listOfMoves:
            self.temp_move(move)
            state = {}
            state['numBlack'] = 0
            state['numRed'] = 0
            state['numBlackKings'] = 0
            state['numRedKings'] = 0
            state['numBlackThreatened'] = 0
            state['numRedThreatened'] = 0
            state['move'] = move

            for row in self.listOfNodes:
                for node in row:
                    if node.colour == Colour.BLACK:
                        if self.is_piece_threatened(node):
                            state['numBlackThreatened'] += 1
                        if node.king:
                            state['numBlackKings'] += 1
                        else:
                            state['numBlack'] += 1
                    else:
                        if self.is_piece_threatened(node):
                            state['numRedThreatened'] += 1
                        if node.king:
                            state['numRedKings'] += 1
                        else:
                            state['numRed'] += 1
            listOfStates.append(state)
            self.undo_move(move)

        return listOfStates

    def move_here(self, move):
        self.temp_move(move)
        self.jumpNode = 0
        self.jumpKing = False
        self.jumpColour = None
        self.save_move(move)

    ############## INTERNAL FUNCTIONS###############

    def temp_move(self, move):
        ## make sure the move is in list_of_possible_moves
        if move in self.listOfMoves:
            oldNode = self.get_node_for_square(move[0])
            newNode = self.get_node_for_square(move[1])
            if self.jump == 1:
                if oldNode.upLeft.upLeft == newNode:
                    self.copy_node_piece(oldNode.upLeft)
                    self.delete_node_piece(oldNone.upLeft)
                elif oldNode.upRight.upRight == newNode:
                    self.copy_node_piece(oldNode.upLeft)
                    self.delete_node_piece(oldNone.upLeft)
                elif oldNode.downLeft.downLeft == newNode:
                    self.copy_node_piece(oldNode.upLeft)
                    self.delete_node_piece(oldNone.upLeft)
                else:
                    self.copy_node_piece(oldNode.upLeft)
                    self.delete_node_piece(oldNone.upLeft)

            newNode.king = oldNode.king
            oldNode.king = False

            newNode.colour =  oldNode.colour
            oldNode.colour =  False

            return True
        return False

    def setup_board(self):
        for i in range(8):
            row = []
            for j in range(4):
                newNode = Node()
                newNode.row = i
                newNode.col = j
                if i < 3:
                    newNode.colour = Colour.BLACK
                if i > 4:
                    newNode.colour = Colour.RED
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
                if j == 0 and i % 2 == 0:
                    leftBorder = True
                if j == 3 and i % 2 == 1:
                    rightBorder = True
                if not upBorder:
                    if not leftBorder:
                        if i % 2 == 0:
                            moveIdx = j-1
                        else:
                            moveIdx = j
                        self.listOfNodes[i][j].upLeft = self.listOfNodes[i-1][moveIdx]
                    if not rightBorder:
                        if i % 2 == 1:
                            moveIdx = j+1
                        else:
                            moveIdx = j
                        self.listOfNodes[i][j].upRight = self.listOfNodes[i-1][moveIdx]
                if not downBorder:
                    if not leftBorder:
                        if i % 2 == 0:
                            moveIdx = j-1
                        else:
                            moveIdx = j
                        self.listOfNodes[i][j].downLeft = self.listOfNodes[i+1][moveIdx] 
                    if not rightBorder:
                        if i % 2 == 1:
                            moveIdx = j+1
                        else:
                            moveIdx = j
                        self.listOfNodes[i][j].downRight = self.listOfNodes[i+1][moveIdx]

    def create_output_file(self):
        directory  = os.path.join(os.getcwd(), 'gameLogs')
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, 'checkers' + time.strftime("%Y%m%d-%H%M%S"))
        self.output_file = open(file_path, 'w')

    
    def copy_node_piece(self, node):
        self.jumpNode = self.get_square_for_node();
        self.jumpColour =  node.colour
        self.jumpKing = node.king

    def delete_node_piece(self, node):
        node.colour = None
        node.king = False

    def is_piece_threatened(self, node):
        return (self.is_enemy_in_dir(node, node.upRight, Colour.BLACK, node.downLeft) or \
                self.is_enemy_in_dir(node, node.upLeft, Colour.BLACK, node.downRight) or \
                self.is_enemy_in_dir(node, node.downRight, Colour.RED, node.upLeft) or \
                self.is_enemy_in_dir(node, node.downLeft, Colour.RED, node.upRight))

    def is_enemy_in_dir(self, node, adjacentNode, enemyColour, oppAdjNode):
        if adjacentNode != None:
            if adjacentNode.colour != node.colour:
                if adjacentNode.colour == enemyColour or adjacentNode.king:
                    if oppAdjNode != None and oppAdjNode.colour != None:
                        return True

        return False

    def check_node_moves(self, piece):
        moves=[]
        jumps=[]
        if piece.king == True or piece.colour == Colour.BLACK:
            if piece.downLeft != None:
                self.check_node_dir(piece,piece.downLeft,piece.downLeft.downLeft,moves,jumps)
            if piece.downRight != None:
                self.check_node_dir(piece,piece.downRight,piece.downRight.downRight,moves,jumps)

        if piece.king == True or piece.colour == Colour.RED:
            if piece.upLeft != None:
                self.check_node_dir(piece,piece.upLeft,piece.upLeft.upLeft,moves,jumps)
            if piece.upRight != None:
                self.check_node_dir(piece,piece.upRight,piece.upRight.upRight,moves,jumps)
            
        if len(jumps)!=0:
            self.jump=1
            return jumps
        else:
            return moves

    def check_node_dir(self, piece, node, nodeDir, moves, jumps):
        if node.colour!= piece.colour:
            if node.colour == None:
                moves.append([self.get_square_for_node(piece),self.get_square_for_node(node)])
            elif nodeDir!=None and nodeDir.colour==None:
                jumps.append([self.get_square_for_node(piece),self.get_square_for_node(node)])

    def get_square_for_node(self, node):
        return (node.row*4 + node.col + 1)

    def get_node_for_square(self, square):
        return self.listOfNodes[(square-1)/4][(square-1)%4]

    def save_move(self, move):
        output = str(move[0]) + ' - ' + str(move[1])
        print output
        self.output_file.write(output)

    def undo_move(self, move):
        self.temp_move([move[1],move[0]])
        node = self.get_node_for_square(self.jumpNode)
        node.king=self.jumpKing
        node.king=self.jumpColour

    