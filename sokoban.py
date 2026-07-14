#ilopiisi sokoban
from state import State

class Sokoban(State):

    def __init__(self, player_pos, boxes):
        super().__init__()
        #thesi pexti os row,column
        self.player_pos = player_pos
        #thesi koution
        self.boxes = set(boxes)

    #check an vrikame lisi
    def is_final(self, goals):

        for box in self.boxes:
            if box not in goals:
                return False
        return True
    
    #an den einai goal kai vriskete se gonia tote einai axristo to monopati
    def is_deadend(self, pos, board):
        (r, c) = pos
        if pos in board.goals:
            return False
        #elenxei an einai toixos h ektos orion
        def wall_or_out(rr, cc):
            if rr < 0 or rr >= board.rows or cc < 0 or cc >= board.cols:
                return True
            return (rr, cc) in board.walls

        up = wall_or_out(r - 1, c)
        down = wall_or_out(r + 1, c)
        left = wall_or_out(r, c - 1)
        right = wall_or_out(r, c + 1)

        #gonia: panw+aristera, panw+deksia, katw+aristera, katw+deksia
        if (up and left) or (up and right) or (down and left) or (down and right):
            return True
        return False


    #epomeno state(panw, katw, deksia, aristera)
    def get_children(self, board):
        children = []
        directions = [
            #panw
            (-1, 0),
            #katw
            (1, 0),
            #aristera
            (0, -1),
            #deksia
            (0, 1)
        ]

        for dr, dc in directions:
            #torini thesi
            pr, pc = self.player_pos
            #nea thesi an kanei to vima
            nr, nc = pr + dr, pc + dc
            new_player_pos = (nr, nc)

            #elenxos orion kai toixou
            if nr < 0 or nr >= board.rows or nc < 0 or nc >= board.cols:
                continue
            if new_player_pos in board.walls:
                continue

            new_boxes = set(self.boxes)

            #an paei se keli xoris kouti:
            if new_player_pos not in new_boxes:
                child = Sokoban(new_player_pos, new_boxes)
                child.g = self.g + 1
                child.father = self
                children.append(child)
                continue

            #an paei se keli me kouti
            br, bc = nr + dr, nc + dc
            beyond_pos = (br, bc)

            #an paei na to sproksi se akiro keli h den bori logo toixou h koutiou h einai dead end,akironete
            if br < 0 or br >= board.rows or bc < 0 or bc >= board.cols:
                continue
            if beyond_pos in board.walls or beyond_pos in new_boxes:
                continue
            if self.is_deadend(beyond_pos, board):
                continue

            #kanei push
            new_boxes.remove(new_player_pos)
            new_boxes.add(beyond_pos)
            child = Sokoban(new_player_pos, new_boxes)
            child.g = self.g + 1
            child.father = self
            children.append(child)

        return children
    #sigkrinoume states
    def __eq__(self, other):
        if isinstance(other, Sokoban):
            return self.player_pos == other.player_pos and self.boxes == other.boxes
        return False
    #apothikeuoume states
    def __hash__(self):
        return hash((self.player_pos, tuple(sorted(self.boxes))))