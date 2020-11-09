#!/usr/bin/python

def instructions():
    '''how to play the game'''
    print('welcome to tictactoe on python!')
    print('this game is played between two people, one with "x" and the other with "o"')
    print('the purpose of this game is to get three in a row, colum or diagonal on the following grid')
    board1= initboard()
    prettboard(board1)
    print('both players take turns picking where they want to play')
    print('if no one scores then its a tie!')
    print('each player has to pick a specific slot, the numbering is as follows:')
    numboard=[[1,2,3],[4,5,6],[7,8,9]]
    prettboard(numboard)
    print('once a slot has been filled its value cant be changed')
    print('good luck and have fun!')

def initboard(val='_',n=3):
    ''' starts a default 3*3 board with blank spaces'''
    b=[]
    for i in range(n):
        b.append([])
    for row in b:
        for i in range(n):
            row.append(val)
    return b

def prettboard(brd):
    '''prints the grid nicely'''
    for row in brd:
        print('{} {} {}'.format(row[0],row[1],row[2]))

def win(state,turn):
    '''win checks the current state of the board and
     sees if the player won'''
    for row in state:
        if row[0]==turn and row[1]==turn and row[2]==turn:
            return True
    for col in range(3):
        if state[0][col]==turn and state[1][col]==turn and state[2][col]==turn:
            return True
    if state[0][0]==turn and state[1][1]==turn and state[2][2]==turn:
        return True
    if state[2][0]==turn and state[1][1]==turn and state[0][2]==turn:
        return True
    return False

def pickslot(sym):
    '''user must pick a slot within range'''
    a=1
    while a==1:
        try:
            slot=int(input('player {} where do yo want to play? '.format(sym)))
            while slot<1 or slot>9:
                slot=int(input('please choose a number between 1-9: '))
            a=0
        except:
            print('please input a number')
    slot=slot-1
    return slot

def move(sym):
    '''assigns pick to valid place'''
    place=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    x,y=place[pickslot(sym)]
    while board[x][y]=='o' or board[x][y]=='x':
        print("sorry, that place is taken")
        x,y=place[pickslot(sym)]
    board[x][y]=sym

def toggleplayer(num):
    '''moves btw player o and x'''
    if num%2==0:
        val='x'
    else:
        val='o'
    return val

if __name__=='__main__':
    instructions()
    board=initboard()
    for i in range(9):
         a=toggleplayer(i)
         move(a)
         prettboard(board)
         if win(board,a)==True:
             print('congrats player {} you won!'.format(a))
             break
    if win(board,'x')==False and win(board,'o')==False:
        print("sorry its a tie")
