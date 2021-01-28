from typing import List


def solution(board)->bool:
    """
    Strategy:
     define a function which receives list as input and check whether it is valid.
     Make each section to length 9 list and check whether it is valid or not.
    """
    a=["1","2","3","4","5","6","7","8","9"]
    def check(sublist):
        # No repeat. only 1-9
        sub=[]
        for v in sublist:
            if v==".":
                continue
            else:
                if v in sub:
                    return False
                elif v not in a:
                    return False
                else:
                    sub.append(v)
        return True


    # Row check
    for row in board:
        if check(row)==False:
            return False
    #Column Check
    tboard=[[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            tboard[i][j]=board[j][i]
    print(tboard)
    for col in tboard:
        if check(col)==False:
            return False

    # Square Check
    t2board=[[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(9):
        for j in range(9):
            t2board[i//3][j//3].append(board[i][j])

    for row in t2board:
        for c in row:
            if check(c)==False:
                return False

    return True


if __name__ == '__main__':
    board =[["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    #print(solution(board))
    print(solution(board))
