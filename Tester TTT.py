from Solver import *

WINS = 0
WINS_PRIM = 0
LOSSES = 0
LOSSES_PRIM = 0
TIES = 0
TIES_PRIM = 0

BLANK_BOARD = "---------"
SolutionTTT = Solve(BLANK_BOARD)

for position in SolutionTTT[1]:
    if SolutionTTT[1][position] == OUTCOMES[0]:
        WINS += 1
    elif SolutionTTT[1][position] == OUTCOMES[1]:
        LOSSES += 1
    elif SolutionTTT[1][position] == OUTCOMES[2]:
        TIES += 1
for prim in SolutionTTT[2]:
    if SolutionTTT[1][prim] == OUTCOMES[0]:
        WINS_PRIM += 1
    elif SolutionTTT[1][prim] == OUTCOMES[1]:
        LOSSES_PRIM += 1
    elif SolutionTTT[1][prim] == OUTCOMES[2]:
        TIES_PRIM += 1

TOTAL = len(SolutionTTT[1])
TOTAL_PRIM = len(SolutionTTT[2])
print("LOSE: " + str(LOSSES) + "(" + str(LOSSES_PRIM) + " primitive)")
print("WIN: " + str(WINS) + "(" + str(WINS_PRIM) + " primitive)")
print("TIES: " + str(TIES) + "(" + str(TIES_PRIM) + " primitive)")
print("TOTAL: " + str(TOTAL) + "(" + str(TOTAL_PRIM) + " primitive)")


from math import factorial
# BOARDS = [BLANK_BOARD]

def R(x, o, s):
    return int(factorial(s) / (factorial(x) * factorial(o)* factorial(s - x - o)))

def TotalR(x, o, s, sum=0):
    if x == 0 and o == 0:
        return R(x, o, s) + sum
    elif x > o:
        return TotalR(x - 1, o, s, sum + R(x, o, s))
    else:
        return TotalR(x, o - 1, s, sum + R(x, o, s))

def GenerateBoards(x, o, s, player):
    global BOARDS
    x_old = x
    o_old = o
    if x > o:
        x_old = x - 1
    else:
        o_old = o - 1
    print(TotalR(x_old, o_old, s), TotalR(x, o, s))
    for i in range(TotalR(x_old, o_old, s), TotalR(x, o, s)):
        for index in range(9):
            if BOARDS[i][index] == "-":
                BOARDS += [BOARDS[i][:index] + player + BOARDS[i][index + 1:]]

def GenerateAllBoards():
    global BOARDS
    for index in range(9):
        BOARDS += [BLANK_BOARD[:index] + "x" + BLANK_BOARD[index + 1:]]
    # for x in range(1, 6):
    #     for n in range(2):
    #         o = x - n
    #         if o >= 5:
    #             break
    #         elif x > o:
    #             team = "o"
    #         else:
    #             team = "x"
    #         GenerateBoards(x, o, 9, team)
    GenerateBoards(1, 0, 9, "o")
    GenerateBoards(1, 1, 9, "x")
    GenerateBoards(2, 1, 9, "o")
    GenerateBoards(2, 2, 9, "x")
    GenerateBoards(3, 2, 9, "o")
    GenerateBoards(3, 3, 9, "x")
    GenerateBoards(4, 3, 9, "o")
    GenerateBoards(4, 4, 9, "x")
    # GenerateBoards(5, 4, 9, "o")

# GenerateAllBoards()
# print(BOARDS)
# print(len(BOARDS))
# print(R(2, 1, 9))

# for moves in range(TotalR(0, 0, 9), TotalR(1, 0, 9)):
#     for index in range(9):
#         if BOARDS[moves][index] == "-":
#             BOARDS += [BOARDS[moves][:index] + player + BOARDS[moves][index + 1:]]

# def NewSolve(position):
#     return [(Solve(DoMove(position, move))) for move in GenerateMoves(position)]
#
# print(NewSolve("---------"))








# def MakeAMoveGlobal(player):
#     global BOARDS
#     if player % 2 == 0:
#         player = "x"
#     else:
#         player = "o"
#     for moves in range(9):
#         for index in range(9):
#             if BOARDS[moves][index] == "-":
#                 BOARDS += [BOARDS[moves][:index] + player + BOARDS[moves][index + 1:]]



# for alternating in range(1, 1):
#     MakeAMoveGlobal(alternating)









def Hash(pos_str):
    """Converts "xo-" strings to base 10 decimal numbers (treating the string as a ternary number
    with - being 0, x being 1, o being 2)
    >>> Hash("xo-------")
    10935
    >>> Hash("ooooxxxxx") # max hash number for tic tac toe 3x3
    19561

    """
    hash = 0
    for power in range(len(pos_str)):
        if pos_str[power] == "x":
            hash += 1 * 3 ** (len(pos_str) - 1 - power)
        elif pos_str[power] == "o":
            hash += 2 * 3 ** (len(pos_str) - 1 - power)
    return hash

def DecimalString(num):
    power = 0
    while 3 ** (power + 1) <= num:
        power += 1
        # to be finished

def Unhash(hash):
    """Converts ternary numbers to "xo-" strings
    >>> Unhash(120000000)
    "xo-------"
    """
    pos_str = ""
    while hash != 0:
        ones = hash % 10
        if ones == 0:
            pos_str = "-" + pos_str
        elif ones == 1:
            pos_str = "x" + pos_str
        else:
            pos_str = "o" + pos_str
        hash = hash // 10
    return pos_str



# for char in ("---------"):
# Solve("x--------")
# Solve("-x-------")

# print(str(5) + ": " + Solve("xoxxoxo--"))
# "oxxxxoo-"
# print(21111220)
# print(Hash("ooooxxxxx"))
# print(Unhash(120000000))
# print(Solve("xoxxoxoo-"))
# print(Solve("xoxxoxo--"))
# print(Solve("---------"))
# print(PrimitiveValue("xoooxxoxx"))
# position = "xoooxxoxx"
# print(ThreeInARow(position, Turn(position, reverse=True)))