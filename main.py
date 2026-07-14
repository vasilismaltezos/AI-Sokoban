from board import Board
from sokoban import Sokoban
from aStar import a_star

#print arxiko map
def print_state(board, state):
    rows = board.rows
    cols = board.cols

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            pos = (r, c)
            if pos in board.walls:
                row.append('#')
            elif pos in board.goals:
                row.append('.')
            else:
                row.append(' ')
        grid.append(row)

    # koutia
    for (br, bc) in state.boxes:
        if (br, bc) in board.goals:
            grid[br][bc] = '*'
        else:
            grid[br][bc] = '$'

    # paikths
    pr, pc = state.player_pos
    if (pr, pc) in board.goals:
        grid[pr][pc] = '+'
    else:
        grid[pr][pc] = '@'

    for row in grid:
        print("".join(row))


def main():
    board = Board()
    board.load("lvl1.txt")

    start = Sokoban(board.player_start, board.boxes_start)

    print("----Arxiki Katastasi----")
    print_state(board, start)

    print("\nYpologismos me A*...\n")
    goal_state, states = a_star(start, board)

    if goal_state is None:
        print("Den vrethike lysi")
        return

    print("----Vrethike Lisi----")
    print("Pragmatopoihike se ", goal_state.g,"vimata")
    print(f"O sinolikos xronos htan: {goal_state.total_time:.2f} sec")
    print("Sinolo katastasewn pou epexergastike o A*:",states)

if __name__ == "__main__":
    main()