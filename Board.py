#from Piece import Piece;
import Piece;


#comments are done in the java code. I basically took my java code and converted it into python 
class Board :

  #  array = int[8][8];
    score1 = 0
    score2 = 0

    def __init__(self):
        # White goes first (0 is white and player,1 is black and computer)
        self.player = 0
        self.passed = False

        #  Initializing an empty board
        self.array = []
        for x in range(8):
            self.array.append([])
            for y in range(8):
                self.array[x].append(None)

    def start(self):

        # Initializing center values

        p1 = Piece.Piece(1,False, True, True, False)
        p2 = Piece.Piece(0,False, True, False, True)
        p3 = Piece.Piece(1,True, False, False, True)
        p4 = Piece.Piece(0,True, False, True, False)

        self.array[3][3] = p1
        self.array[3][4] = p4
        self.array[4][3] = p2
        self.array[4][4] = p3



    def beginGame(self):

        print("Welcome to the game! Lets play Othello")


        turn = 1
        player =1
        print("Player 1 starts. GO!")
        self.start()

        while turn < 65 :
            self.printGrid()

            column =input("Enter the letter: ")
            column = column[0]
            row = int(input("Enter the row: "))


            pieceMade = board.createPiece(column, row-1, player)
            if pieceMade :
                self.calculateScores();
                turn+=1;
            print();

            if turn % 2 == 0 :
                print("Player 2's turn.")
                player = 0;
            else :
                print("Player 1's turn.")
                player = 1;




    def printGrid(self):
        print("  A B C D E F G H    ")
        print(" _______________ ")

        for i in range(8):
            print(i+1,end=' ')
            for j in range(8):
                if self.array[i][j] == None :
                    print('.',end=' ')

                elif self.array[i][j].color == 1 :
                    print("*", end=' ')
                else :
                    print ('O',end=' ')
            print()


    def createPiece(self, col, row, player) :
        col = col.lower()


        #row = row-1



        if(col == 'a') :
            column = 0
        elif (col == 'b') :
            column = 1
        elif (col == 'c') :
            column = 2
        elif (col == 'd'):
            column = 3
        elif (col == 'e'):
            column = 4
        elif (col == 'f') :
            column = 5
        elif (col == 'g'):
            column = 6
        elif (col == 'h') :
            column = 7
        else :
            col = input("Enter a valid letter")

        if row < 0 or row > 8:
            row = input("Enter a valid number")


        ready = self.checkValid(row, column)

        newPiece = Piece.Piece(player,False, False, False, False)

        if ready and self.array[row][column] == None and self.isPlacable(newPiece, row, column) :

            self.array[row][column] = newPiece
            self.changePieces(newPiece, row, column)
            return True
        else :
            print("Position not valid. Try again.")
            return False

    def isPlacable(self, a, row, column):

         top = False
         bottom = False
         left = False
         right = False

         if self.checkValid(row-1,column):
            if self.array[row-1][column] != None and self.array[row-1][column].color != a.color :
                top = True
         if self.checkValid(row+1,column):
            if self.array[row+1][column] != None and self.array[row+1][column].color != a.color :
                bottom = True
         if self.checkValid(row,column-1):
            if self.array[row][column-1] != None and self.array[row][column-1].color != a.color :
                left = True
         if self.checkValid(row,column+1):
            if self.array[row][column+1] != None and self.array[row][column+1].color != a.color :
                right = True


         if top or bottom or left or right :
            return True
         else :
             return False

    def checkValid(self,r, c):
        if r >= 0 and r < 8 and c >= 0 and c < 8 :
            return True
        else :
            return False


    def changePieces(self, a, row,  column) :


        if self.checkValid(row-2,column) :
            if self.array[row-2][column] != None:
                if self.array[row-2][column].color == a.color :
                    if self.array[row-1][column] != None:
                       self.array[row-1][column].color = a.color

        if self.checkValid(row + 2, column):
            if self.array[row + 2][column] != None:
                if self.array[row + 2][column].color == a.color:
                    if self.array[row+1][column] != None:
                       self.array[row + 1][column].color = a.color
        if self.checkValid(row,column-2) :
            if self.array[row][column-2] != None:
                if self.array[row][column-2].color == a.color :
                    if self.array[row][column - 1] != None:
                       self.array[row][column-1].color = a.color
        if self.checkValid(row,column+2) :
            if self.array[row][column+2] != None:
                if self.array[row][column+2].color == a.color :
                    if self.array[row][column + 1] != None:
                       self.array[row][column+1].color = a.color


    def calculateScores(self) :

        playerOneScore =0;
        playerTwoScore =0;

        for i in range(8):
            for j in range(8):
                if self.array[i][j] != None :
                    if self.array[i][j].color == 1 :
                        playerOneScore+=1
                    if self.array[i][j].color == 0 :
                        playerTwoScore+=1

        score1 = playerOneScore
        score2 = playerTwoScore

        if playerOneScore > playerTwoScore :
            print("Player One is currently winning")
        elif playerOneScore < playerTwoScore :
            print("Player Two is winning")


board = Board()
board.beginGame()


