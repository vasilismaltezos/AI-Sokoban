# ilopoiisi A*
import time
from sokoban import Sokoban


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#kotninotero goal me manhattan kai athrisma apostaseon
def heuristic(state, goals):
    # An den exoume koutia i goals, den exei noima i euretiki
    if goals is None or len(goals) == 0 or len(state.boxes) == 0:
        return 0
    total = 0

    # gia KATHE kouti tou state
    for box in state.boxes:
        min_dist = None

        # briskoume tin mikroteri apostasi se KAPOIO goal
        for g in goals:
            d = manhattan(box, g)
            if min_dist is None or d < min_dist:
                min_dist = d

        # prosthetoume tin apostasi tou koutiou pros to kontinotero goal
        total += min_dist

    return total

#goal_state an vrei lisi / none an den vrei
def a_star(start_state, board):
    # Arxikopoioume to arxiko state
    start_state.g = 0
    start_state.h = heuristic(start_state, board.goals)
    start_state.f = start_state.g + start_state.h
    start_state.father = None

    #lista kai visited set
    open_list = [start_state]
    closed_set = set()
    #xronos
    start_time = time.time()
    #plithos katastaseon
    states = 0

    while len(open_list) > 0:
        # Vriskoume to state me to mikrotero f sti lista
        best_index = 0
        best_state = open_list[0]
        i = 1
        while i < len(open_list):
            candidate = open_list[i]
            if candidate.f < best_state.f:
                best_state = candidate
                best_index = i
            i = i + 1

        #to pernw
        current = open_list.pop(best_index)

        #an toxw hdh dei skip
        if current in closed_set:
            continue
        states+=1
        #an einai teliko return
        if current.is_final(board.goals):
            end_time = time.time()
            current.total_time = end_time - start_time
            return current,states

        #Alliws add sto visited
        closed_set.add(current)

        #Ftiaxnw ta paidia
        children = current.get_children(board)

        for child in children:
            #an exei episkefthei hdh skip
            if child in closed_set:
                continue

            #f,g,h paidiou
            child.g = current.g + 1
            child.h = heuristic(child, board.goals)
            child.f = child.g + child.h

            child.father = current
            open_list.append(child)
    return None,states


def reconstruct_path(goal_state):
    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = current.father

    path.reverse()
    return path