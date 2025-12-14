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
        