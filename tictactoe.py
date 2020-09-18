theBoard = {7: ' ' ,8: ' ' ,9: ' ' ,
            4: ' ' ,5: ' ' ,6: ' ' ,
            1: ' ' ,2: ' ' ,3: ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(' '+board[1] + ' | ' + board[2] + ' | ' + board[3]+' ')
    print('---+---+---')
    print(' '+board[4] + ' | ' + board[5] + ' | ' + board[6]+' ')
    print('---+---+---')
    print(' '+board[7] + ' | ' + board[8] + ' | ' + board[9]+' ')

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()
        try:
            mov=int(move)
        except:
            print("Enter a valid position between 1-9")
            continue
        if theBoard[mov] == ' ':
            theBoard[mov] = turn
            count =count+1
        else:
            print("This place is already filled.\nChoose another place.")
            continue
        if count >= 5:
            if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!\n")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again?\nEnter y for yes and any other char for no.\n")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '
        print("Do you want to play with computer or your friend?\nEnter 1 to play with computer\nEnter 2 to play with your friend\n")
        i=input()
        try:
            inp=int(i)
        except:
            print("Enter a valid input\n")
            quit()
        if inp==1:
            cgame()
        elif inp==2:
            game()
        else:
            print("Enter a valid choice\n")
            quit()

def poswinh(ch):
    turn='X'
    if ch=='h' or ch=='H':
        turn='X'
    elif ch=='c' or ch=='C':
        turn='O'
    if theBoard[1]==theBoard[2]==turn and theBoard[3]==' ':
        return 3
    elif theBoard[2]==theBoard[3]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[1]==theBoard[3]==turn and theBoard[2]==' ':
        return 2
    elif theBoard[4]==theBoard[5]==turn and theBoard[6]==' ':
        return 6
    elif theBoard[4]==theBoard[6]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[6]==turn and theBoard[4]==' ':
        return 4
    elif theBoard[7]==theBoard[8]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[7]==theBoard[9]==turn and theBoard[8]==' ':
        return 8
    elif theBoard[8]==theBoard[9]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[1]==theBoard[5]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[1]==theBoard[9]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[9]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[3]==theBoard[5]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[3]==theBoard[7]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[7]==turn and theBoard[3]==' ':
        return 3
    elif theBoard[1]==theBoard[4]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[1]==theBoard[7]==turn and theBoard[4]==' ':
        return 4
    elif theBoard[4]==theBoard[7]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[2]==theBoard[5]==turn and theBoard[8]==' ':
        return 8
    elif theBoard[2]==theBoard[8]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[8]==turn and theBoard[2]==' ':
        return 2
    elif theBoard[3]==theBoard[6]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[3]==theBoard[9]==turn and theBoard[6]==' ':
        return 6
    elif theBoard[6]==theBoard[9]==turn and theBoard[3]==' ':
        return 3
    else:
        return 0

def poswinc(ch):
    turn='X'
    if ch=='H' or ch=='h':
        turn='O'
    elif ch=='C' or ch=='c':
        turn='X'
    if theBoard[1]==theBoard[2]==turn and theBoard[3]==' ':
        return 3
    elif theBoard[2]==theBoard[3]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[1]==theBoard[3]==turn and theBoard[2]==' ':
        return 2
    elif theBoard[4]==theBoard[5]==turn and theBoard[6]==' ':
        return 6
    elif theBoard[4]==theBoard[6]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[6]==turn and theBoard[4]==' ':
        return 4
    elif theBoard[7]==theBoard[8]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[7]==theBoard[9]==turn and theBoard[8]==' ':
        return 8
    elif theBoard[8]==theBoard[9]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[1]==theBoard[5]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[1]==theBoard[9]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[9]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[3]==theBoard[5]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[3]==theBoard[7]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[7]==turn and theBoard[3]==' ':
        return 3
    elif theBoard[1]==theBoard[4]==turn and theBoard[7]==' ':
        return 7
    elif theBoard[1]==theBoard[7]==turn and theBoard[4]==' ':
        return 4
    elif theBoard[4]==theBoard[7]==turn and theBoard[1]==' ':
        return 1
    elif theBoard[2]==theBoard[5]==turn and theBoard[8]==' ':
        return 8
    elif theBoard[2]==theBoard[8]==turn and theBoard[5]==' ':
        return 5
    elif theBoard[5]==theBoard[8]==turn and theBoard[2]==' ':
        return 2
    elif theBoard[3]==theBoard[6]==turn and theBoard[9]==' ':
        return 9
    elif theBoard[3]==theBoard[9]==turn and theBoard[6]==' ':
        return 6
    elif theBoard[6]==theBoard[9]==turn and theBoard[3]==' ':
        return 3
    else:
        return 0

def posany():
    for i in range(1,10):
        if theBoard[i]==' ':
            return i
    return 0

def posmov():
    if theBoard[5]==" ":
        return 5
    elif theBoard[2]==" ":
        return 2
    elif theBoard[4]==" ":
        return 4
    elif theBoard[6]==" ":
        return 6
    elif theBoard[8]==" ":
        return 8
    else:
        return 0

def findposwin(player):
    if theBoard[7] == theBoard[8] == theBoard[9] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " +player+ " won. ****")
        return 0
    else:
        printBoard(theBoard)
        return 1

def cgameh(ch):
    count=0
    flag=1
    turn='X'
    for i in range(10):
        if count%2==0 and flag==1:
            turn='X'
            player='You'
            print("It's your turn.\tWhich place do you want to move to ?")
            move=input()
            try:
                mov=int(move)
            except:
                print("Enter a valid position between 1-9")
                continue
            if mov>9 or mov<1:
                print("Enter a valid position between 1-9")
                continue
            if(theBoard[mov]==' '):
                theBoard[mov]=turn
                count=count+1
            else:
                print("This place is already filled.\nChoose another position")
                continue

        elif count%2!=0 and flag==1:
            turn='O'
            player='Computer'
            if count==1:
                if theBoard[5]==' ':
                    theBoard[5]=turn
                    print(player+" has chosen 5")
                else:
                    theBoard[2]=turn
                    print(player+" has chosen 2")
                count=count+1
            elif count==3:
                pwh=poswinh(ch)
                if pwh!=0:
                    theBoard[pwh]=turn
                    print(player+" has chosen "+str(pwh))
                else:
                    pm=posmov()
                    theBoard[pm]=turn
                    print(player+" has chosen "+str(pm))
                count=count+1
            elif count==5:
                pwc=poswinc(ch)
                pwh=poswinh(ch)
                if pwc!=0:
                    theBoard[pwc]=turn
                    print(player+" has chosen "+str(pwc))
                    flag=0
                    printBoard(theBoard)
                    print("Computer Won")
                    break
                elif pwh!=0:
                    theBoard[pwh]=turn
                    print(player+" has chosen "+str(pwh))
                else:
                    pm=posmov()
                    theBoard[pm]=turn
                    print(player+" has chosen "+str(pm))
                count=count+1
            elif count==7:
                pwc=poswinc(ch)
                pwh=poswinh(ch)
                if pwc!=0:
                    theBoard[pwc]=turn
                    print(player+" has chosen "+str(pwc))
                    flag=0
                    printBoard(theBoard)
                    print("Computer Won")
                elif pwh!=0:
                    theBoard[pwh]=turn
                    print(player+" has chosen "+str(pwh))
                else:
                    pa=posmov()
                    theBoard[pa]=turn
                    print(player+" has chosen "+str(pa))
                count=count+1
        if(count<5):
            printBoard(theBoard)
        elif count >= 5 and flag==1:
            flag=findposwin(player)

        if count == 9 and flag==1:
            print("\nGame Over.\n")
            print("It's a Tie!!\n")
            break

def cgamec(ch):
    count=0
    flag=1
    turn='X'
    for i in range(10):
        if count%2==0 and flag==1:
            turn='X'
            player='Computer'
            if count==0:
                theBoard[5]=turn
                print(player+" chose 5")
                count=count+1
            elif count==2:
                if theBoard[9]==' ':
                    theBoard[9]=turn
                    print(player+" has chosen 9")
                else:
                    theBoard[3]=turn
                    print(player+" has chosen 3")
                count=count+1
            elif count==4:
                pwc=poswinc(ch)
                pwh=poswinh(ch)
                if pwc!=0:
                    theBoard[pwc]=turn
                    #d={'pwc':turn}
                    #theBoard.update(d)
                    print(player+" has chosen "+str(pwc))
                    flag=0
                    printBoard(theBoard)
                    print("Computer Won")
                    break
                elif pwh!=0:
                    theBoard[pwh]=turn
                    print(player+" has chosen "+str(pwh))
                elif theBoard[7]==' ':
                    theBoard[7]=turn
                    print(player+" has chosen 7")
                else:
                    theBoard[3]=turn
                    print(player+" has chosen 3")
                count=count+1
            elif count==6 or count==8:
                pwc=poswinc(ch)
                pwh=poswinh(ch)
                if pwc!=0:
                    theBoard[pwc]=turn
                    print(player+" has chosen "+str(pwc))
                    flag=0
                    printBoard(theBoard)
                    print("Computer Won")
                    break
                elif pwh!=0:
                    theBoard[pwh]=turn
                    print(player+" has chosen "+str(pwh))
                else:
                    pa=posany()
                    theBoard[pa]=turn
                    print(player+" has chosen "+str(pa))
                count=count+1

        elif count%2!=0 and flag==1:
            turn='O'
            player="You"
            print("It's your turn.\tWhich place do you want to move to ?")
            move=input()
            try:
                mov=int(move)
            except:
                print("Enter a valid position between 1-9")
                continue
            if mov>9 or mov<1:
                print("Enter a valid position between 1-9")
                continue
            if(theBoard[mov]==' '):
                theBoard[mov]=turn
                count=count+1
            else:
                print("This place is already filled.\nChoose another position")
                continue
        if count<5:
            printBoard(theBoard)
        elif count >= 5 and flag==1:
            findposwin(player)

        if count == 9 and flag==1:
            print("\nGame Over.\n")
            print("It's a Tie!!\n")
            break

def cgame():
    print("\nDo you want to play first or computer to play first?\nEnter C for Computer to play first\nEnter H for you to play first")
    ch=input()
    try:
        cho=str(ch)
    except:
        print("Enter a valid input\n")
        quit()
    turn='X'
    player='You'
    printBoard(theBoard)
    if (cho=='h' or cho=='H'):
        print("You will play first")
        cgameh(ch)
    elif (cho=='c' or cho=='C'):
        print("Computer plays first")
        cgamec(ch)
    else:
        print("Enter a valid Choice\n")
        quit()

    restart = input("\nDo want to play Again?\nEnter y for yes and any other char for no.\n")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        print("Do you want to play with computer or your friend?\nEnter 1 to play with computer\nEnter 2 to play with your friend")
        i=input()
        try:
            inp=int(i)
        except:
            print("You didn't enter a valid input\n")
            quit()
        if inp==1:
            cgame()
        elif inp==2:
            game()
        else:
            print("You didn't enter a valid choice")
            quit()

if __name__ == "__main__":
    print("Do you want to play with computer or your friend?\nEnter 1 to play with computer\nEnter 2 to play with your friend")
    i=input()
    try:
        inp=int(i)
    except:
        print("Enter a valid input")
        quit()
    if inp==1:
        cgame()
    elif inp==2:
        game()
    else:
        print("Enter a valid choice")
        quit()
