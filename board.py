#board template apo eclass me ilopiisi parser text arxeiou
class Board:

    def __init__(self):
        self._game_board = []
        #diastaseis
        self.rows = 0
        self.cols = 0
        #sinola theseon
        self.walls = set()
        self.goals = set()
        self.player_start = None
        self.boxes_start = set()


    #tiponei board stin othoni
    def print_board(self):
        for row in self._game_board:
            line = ""
            for ch in row:
                line +=ch
            print(line)

    #property getter tou game board
    @property
    def game_board(self):
        return self._game_board
    
    #Fortonei sokoban apo arxeio
    def load(self,name):
        raw_lines = []

        f = open(name, "r")
        for line in f:
            line = line.strip("\n")
            raw_lines.append(line)
        f.close()
        #poses grammes kai stiles exei to level
        self.rows = len(raw_lines)

        #vriskw to megalitero mikos grammhs
        max_cols = 0
        for line in raw_lines:
            if len(line) > max_cols:
                max_cols = len(line)
        self.cols = max_cols

        #reset
        self._game_board = []
        self.walls.clear()
        self.goals.clear()
        self.boxes_start.clear()
        self.player_start = None
        
        #parser arxeion
        r= 0
        for line in raw_lines:
            row = []
            c=0
            while c< self.cols:
                if c< len(line):
                    ch = line[c]
                else:
                    ch = ' '
                row.append(ch)
                pos = (r,c)

                if ch == '#':
                    self.walls.add(pos)
                if ch == '.' or ch == '*' or ch == '+':
                    self.goals.add(pos)
                if ch == '$' or ch == '*':
                    self.boxes_start.add(pos)
                if ch == '@' or ch == '+':
                    self.player_start = pos
                c = c + 1
            self._game_board.append(row)
            r = r+1
        return raw_lines