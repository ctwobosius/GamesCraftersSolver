OUTCOMES = ["win", "lose", "tie", "not primitive"]
POSSIBLE_MOVES = range(1, 3)

def DoMove(position, move):
    """Return a new position based on taking MOVE pennies from POSITION pennies"""
    return position - move

def GenerateMoves(position):
    """Return possible moves given POSITION"""
    return [move for move in POSSIBLE_MOVES if move <= position]

def PrimitiveValue(position):
    """Return whether the position is a win, lose, tie, or not primitive
    for the person whose turn it is given POSITION"""
    if not GenerateMoves(position):
        return OUTCOMES[1]
    return OUTCOMES[3]

# def AnyLoss(list_of_outcomes):
#     if any([outcome == OUTCOMES[1] for outcome in list_of_outcomes]):
#         return OUTCOMES[0]
#     return OUTCOMES[1]

# def Solve(position):
#     if PrimitiveValue(position) != OUTCOMES[3]:
#         return PrimitiveValue(position)
#     return AnyLoss([(Solve(DoMove(position, move))) for move in GenerateMoves(position)])

