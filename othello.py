# =========== Intialization The Board And Starting Positions ===========
    def _init_(self):
        self.size = 8
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

        self.current_player = "B"

#------------------------------------------------------------------------------------------------

     # =========== Switch The Current Player ===========
    def switch_player(self):
        self.current_player = "W" if self.current_player == "B" else "B"

#-----------------------------------------------------------------------------------------------

    # =========== Check If The Move Is Valid ===========
    def is_valid_move(self, player, row, col, board):
        if board[row][col] != " ":
            return False

 # =========== Display The Current State Of The Board ===========
    def display_board(self, board):
        print("\n      == OTHELLO BOARD ==")
        print("   ", end="")
        for col in range(1, self.size + 1):
            print(f" {col}  ", end="")
        print()
        for r in range(self.size):
            print(r + 1, end=" ")
            for c in range(self.size):
                print(f" {board[r][c]} ", end="")
                if c < self.size - 1:
                    print("|", end="")
            print()
            if r < self.size - 1:
                print("  " + "---+" * (self.size - 1) + "---")
        print()

#==================================================================================================

  # =========== Execute a move for the given player on the board and flip opponent pieces ===========
    def make_move(self, board, action, player):
        new_board = [row.copy() for row in board]
        row, col = action
        new_board[row][col] = player
        opponent = "W" if player == "B" else "B"
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < self.size and 0 <= c < self.size:
                if board[r][c] == opponent:
                    found_opponent = True
                    r += dr
                    c += dc
                elif board[r][c] == player:
                    if found_opponent:
                        return True
                    break
                else:
                    break
        return False

#-------------------------------------------------------------------------------------------------

    # ===========  Return A list Of All Valid Moves For A Player Represented As A Tuple ===========
    def get_valid_moves(self, player, board):
        moves = []
        for r in range(self.size):
            for c in range(self.size):
                if self.is_valid_move(player, r, c, board):
                    moves.append((r, c))
        return moves
=======
            to_flip = []
            while 0 <= r < self.size and 0 <= c < self.size:
                if new_board[r][c] == opponent:
                    to_flip.append((r, c))
                    r += dr
                    c += dc
                elif new_board[r][c] == player:
                    for fr, fc in to_flip:
                        new_board[fr][fc] = player
                    break
                else:
                    break
        return new_board

#=======================================================================================

    def game_over(self, board):
        return not (self.get_valid_moves("B", board) or self.get_valid_moves("W", board))

