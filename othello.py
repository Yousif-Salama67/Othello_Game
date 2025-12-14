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
