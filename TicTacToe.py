OUTCOMES = ["win", "lose", "tie", "not primitive"]
BOARD_WIDTH = 3
BOARD_LENGTH = 3
BOARD_SIZE = BOARD_LENGTH * BOARD_WIDTH
WIN_SIZE = 3


def DoMove(position, move):
    """Place a piece in board POSITION for MOVE (index, player) and return the resulting board

    >>> DoMove("xxooox---", (6, "x"))
    "xxoooxx--"

    >>> DoMove("xxooox---", (0, "o"))
    'oxooox---'
    """
    position = position[:move[0]] + move[1] + position[move[0] + 1:]
    return position

def GenerateMoves(position):
    """Given player X is 1 and player O is 2, return possible moves for board POSITION
    >>> GenerateMoves("xxooox---")
    [(6, "x"), (7, "x"), (8, "x")]
    """
    turn = Turn(position)
    return [(index, turn) for index in range(BOARD_SIZE) if position[index] == "-"]

def PrimitiveValue(position):
    """Return whether the position is a win, lose, tie, or not primitive
    for the person whose turn it is given POSITION
    >>> PrimitiveValue("xoooxxoxx")
    "lose"

    """
    if ThreeInARow(position, Turn(position, reverse=True)):
        return OUTCOMES[1]
    elif not GenerateMoves(position): # no moves left, can only lose or tie (PRIMITIVE)
        if ThreeInARow(position, Turn(position, reverse=True)): # 3 in a row
            return OUTCOMES[1]  # lose
        return OUTCOMES[2] # tie
    return OUTCOMES[3] # not primitive

def Turn(position, reverse=False):
    """Returns player x or o depending on how many x's and o's are on the board POSITION
    >>> Turn("xoxoxo---")
    "x"
    >>> Turn("xoxoxox--")
    "o"
    """
    turn = "x"
    if len([char for char in position if char == "x"]) > len([char for char in position if char == "o"]):
        # if number of x's > o's it is o's turn
        turn = "o"
    if reverse and turn == "x":
        turn = "o"
    elif reverse and turn == "o":
        turn = "x"
    return turn

def ThreeInARow(position, team):
    """Return True if there is 3 in a row for TEAM, else False
    >>> ThreeInARow("xoxxo----", "x")
    False
    >>> ThreeInARow("xxxo-o---", "x")
    True
    >>> ThreeInARow("xoxoxxoxo", "x")
    False
    >>> ThreeInARow("xoxxoxoo-", "o")
    True
    """
    horizontal = []
    vertical = []
    # Solve rows
    for pos in range(0, BOARD_SIZE - 1, BOARD_WIDTH): # 0, 3, 6
        for row in range(BOARD_LENGTH): # 0, 1, 2
            horizontal += [position[pos + row]]
        if WIN_SIZE == len([piece for piece in horizontal if team == piece]):  # if 3 in a row on any horizontals
            return True
        horizontal = []

    # Solve columns
    for column in range(BOARD_WIDTH):
        for pos in range(0, BOARD_SIZE - 1, BOARD_WIDTH):
            vertical += [position[pos + column]]
        if WIN_SIZE == len([piece for piece in vertical if team == piece]):  # if 3 in a row on any horizontals
            return True
        vertical = []

    # Solve diagonals
    diagonal = [(0, 4, 8), (2, 4, 6)]
    for diag in diagonal:
        if WIN_SIZE == len([index for index in diag if team == position[index]]):
            return True
    return False






# def ThreeInARow(position):
#     horizontal = []
#     vertical = []
#     diagonal = []
#     opposition = (Turn(position) % 2) + 1 # alternate to other player
#     for pos in range(0, BOARD_SIZE - 1, BOARD_WIDTH): # 0, 3, 6
#         for row in range(BOARD_LENGTH): # 0, 1, 2
#             horizontal += [position[pos + row]]
#         if WIN_SIZE == len([opposition == piece for piece in horizontal]):  # if 3 in a row on any horizontals
#             return OUTCOMES[1]  # current player loses
#         for column in range(BOARD_WIDTH):
#             vertical += [position[pos + column]]
#         if WIN_SIZE == len([opposition == piece for piece in vertical]):  # if 3 in a row on any horizontals
#             return OUTCOMES[1]  # current player loses
#     diagonal = [(0, 4, 8), (2, 4, 6)]
#     for diag in diagonal:
#         if WIN_SIZE == len([opposition == piece for piece in diag]):
#             return OUTCOMES[1]
#     return False

# def PositionUnhash(pos_str):
#     pos_list = []
#     for char in pos_str:
#         if char == "-":
#             pos_list += [0]
#         elif char == "x":
#             pos_list += [1]
#         elif char == "o":
#             pos_list += [2]
#     return pos_list
#
# def PositionHash(pos_list):
#
#     pos_str = []
#     for num in pos_list:
#         if num == 0:
#             pos_str += "-"
#         elif num == 1:
#             pos_str += "x"
#         elif num == 2:
#             pos_str += "o"
#     return pos_str