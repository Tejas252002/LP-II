#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_solution(board):
    for i in range(N):
        for j in range (N):
            print(board[i][j], end=" ")

        print()

def is_safe(row, col, nd,rd, rowlookup, ndlookup, rdlookup):
    if(ndlookup[nd[row][col]] or rdlookup[rd[row][col]] or rowlookup[row]):
        return False
    
    return True

def solve_nqueens_u(board, col, nd, rd, rowlookup, ndlookup, rdlookup):
    if (col>=N):
        return True
    
    for i in range (N):
        if(is_safe(i,col,nd,rd,rowlookup,ndlookup,rdlookup)):
            board[i][col]=1
            rowlookup[i] = True
            ndlookup[nd[i][col]] = True
            rdlookup[rd[i][col]] = True


            if(solve_nqueens_u(board, col+1, nd, rd, rowlookup, ndlookup, rdlookup)):
                return True
        
        board[i][col]=0
        rowlookup[i] = False
        ndlookup[nd[i][col]] = False
        rdlookup[rd[i][col]] = False

    return False
    
def solve_nqueens(N):
    board = [[0 for i in range(N)] for j in range(N)]
    nd = [[0 for i in range(N)] for j in range(N)]
    rd = [[0 for i in range(N)] for j in range(N)]
    
    x=2*N-1

    rowlookup = [False] * x
    
    ndlookup =  [False]*x
    rdlookup =  [False]*x

    for r in range(N):
        for c in range(N):
            nd[r][c]= r + c
            rd[r][c]= r - c + N-1

        if(solve_nqueens_u(board, 0, nd, rd, rowlookup, ndlookup, rdlookup)==False):
            print("Solution does not exists")
            return False
    
        print_solution(board)

        return True
    

while True:
    N=int(input("Enter the number of Queens:"))
    print("Solved by Branch and Bound:")
    solve_nqueens(N)


# In[ ]:




