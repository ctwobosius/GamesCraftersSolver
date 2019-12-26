# from Main import *
# from MainTwentyFive import *
from TicTacToe import *
POSITIONS = {}
PRIMITIVE_POSITIONS = {}

def AnyLoss(list_of_outcomes):
    if OUTCOMES[1] in list_of_outcomes:
        return OUTCOMES[0]
    elif OUTCOMES[2] in list_of_outcomes:
        return OUTCOMES[2]
    return OUTCOMES[1]
    # if any([outcome for outcome in list_of_outcomes if outcome == OUTCOMES[1]]):
    #     return OUTCOMES[0]
    # elif any([outcome for outcome in list_of_outcomes if outcome == OUTCOMES[2]]):
    #     return OUTCOMES[2]
    # return OUTCOMES[1]

def Solve(position):
    if position in POSITIONS.keys():
        return POSITIONS[position]
    elif PrimitiveValue(position) != OUTCOMES[3]:
        POSITIONS[position] = PrimitiveValue(position)
        PRIMITIVE_POSITIONS[position] = PrimitiveValue(position)
        return PrimitiveValue(position)
    POSITIONS[position] = AnyLoss([(Solve(DoMove(position, move))) for move in GenerateMoves(position)])
    return POSITIONS[position], POSITIONS, PRIMITIVE_POSITIONS






    # elif [move for move in POSSIBLE_MOVES if not GenerateMoves(DoMove(position, move))]:
    #     return OUTCOMES[0]
    # elif position > min(POSSIBLE_MOVES):