import copy

class Othello_Game:

    # =========== Intialization The Board And Starting Positions ===========
    def _init_(self):
        self.size = 8
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.board[3][3] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'W'

        self.current_player = "B"

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

     # =========== Switch The Current Player ===========
    def switch_player(self):
        self.current_player = "W" if self.current_player == "B" else "B"

    # =========== Check If The Move Is Valid ===========
    def is_valid_move(self, player, row, col, board):
        if board[row][col] != " ":
            return False
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

    # ===========  Return A list Of All Valid Moves For A Player Represented As A Tuple ===========
    def get_valid_moves(self, player, board):
        moves = []
        for r in range(self.size):
            for c in range(self.size):
                if self.is_valid_move(player, r, c, board):
                    moves.append((r, c))
        return moves

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
    

    # =================================================================
    """"
        == Minimax Algorithm To Find the Best Move For The AI ==
          - maximizing: True If AI turn, False If Human Turn
          - depth: How Many Moves Ahead The AI Should Simulate

    """
    # =================================================================
    def minimax(self, board, depth, maximizing):
        if depth == 0 or self.game_over(board):
            return self.evaluate(board)

        if maximizing:
            max_eval = -float("inf")
            moves = self.get_valid_moves("W", board)
            if not moves:
                return self.minimax(board, depth - 1, False)
            for move in moves:
                new_board = self.make_move(board, move, "W")
                eval = self.minimax(new_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            moves = self.get_valid_moves("B", board)
            if not moves:
                return self.minimax(board, depth - 1, True)
            for move in moves:
                new_board = self.make_move(board, move, "B")
                eval = self.minimax(new_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    # =========== Determine The Best Move For The AI Using The Minimax Algorithm. ===========
    def best_ai_move(self, board, depth):
        best_score = -float("inf")
        best_move = None
        for move in self.get_valid_moves("W", board):
            new_board = self.make_move(board, move, "W")
            score = self.minimax(new_board, depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    
# =========== Shows Board, Score, And Valid Moves Each Turn ===========
    def play_game(self, game_mode = "1"):
        board = self.board
        while not self.game_over(board):
            self.display_board(board)
            self.show_score(board)

            if self.current_player == "B" or game_mode == "1":
                valid_moves = self.get_valid_moves(self.current_player, board)
                if not valid_moves:
                    print(f"No Valid Moves For {self.current_player}. Turn Skipped.")
                    self.switch_player()
                    continue
                print(f"Player {self.current_player}'s Turn")
                print("Valid Moves:", [(r+1, c+1) for r, c in valid_moves])

                while True:
                    try:
                        r = int(input("Row (1-8): ")) - 1
                        c = int(input("Col (1-8): ")) - 1
                        if (r, c) in valid_moves:
                            break
                        else:
                            print("Invalid Move, Choose From The List Above.")
                    except:
                        print("Numbers Only")

                board = self.make_move(board, (r, c), self.current_player)

            else:
                print("White Is Thinking...")
                move = self.best_ai_move(board, depth=5)
                if move is None:
                    print("No valid moves for AI. Turn skipped.")
                else:
                    print(f"AI Chooses Move: {(move[0]+1, move[1]+1)}")
                    board = self.make_move(board, move, "W")

            self.board = board
            self.switch_player()
        self.display_board(board)
        b, w = self.score(board)
        print("\n===== GAME OVER =====")
        print(f"Final Score → Black: {b} | White: {w}")
        if w > b:
            print("White Wins!")
        elif b > w:
            print("You Win!")
        else:
            print("Draw!") 

