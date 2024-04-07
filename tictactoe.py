import math

global boxes
boxes = 0

one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9" 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


global list1
global list2
global list3
global list4
global list5
list1 = [" ", one , " " , '|', " ", two , " " , '|'," " , three]
list2 = ['---------------------']
list3 = [" " , four , " " , '|'," ", five , " " , '|', " ", six]
list4 = ['---------------------']
list5 = [" " , seven , " " , '|'," ", eight , " " , '|' , " ", nine]





def printBoard():
   print(*list1)
   print(*list2)
   print(*list3)
   print(*list4)
   print(*list5)




def check():

    if (

        (list1[1] == list1[5] == list1[9] == bcolors.WARNING + "X" + bcolors.ENDC) or
        (list3[1] == list3[5] == list3[9] == bcolors.WARNING + "X" + bcolors.ENDC) or
        (list5[1] == list5[5] == list5[9] == bcolors.WARNING + "X" + bcolors.ENDC) or

        (list1[1] == list3[1] == list5[1] == bcolors.WARNING + "X" + bcolors.ENDC) or
        (list1[5] == list3[5] == list5[5] == bcolors.WARNING + "X" + bcolors.ENDC) or
        (list1[9] == list3[9] == list5[9] == bcolors.WARNING + "X" + bcolors.ENDC) or

        (list1[1] == list3[5] == list5[9] == bcolors.WARNING + "X" + bcolors.ENDC) or
        (list1[9] == list3[5] == list5[1] == bcolors.WARNING + "X" + bcolors.ENDC)
    ):
        print("Player One (X) wins!")
        return True

    elif (
        (list1[1] == list1[5] == list1[9] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or
        (list3[1] == list3[5] == list3[9] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or
        (list5[1] == list5[5] == list5[9] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or

        (list1[1] == list3[1] == list5[1] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or
        (list1[5] == list3[5] == list5[5] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or
        (list1[9] == list3[9] == list5[9] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or

        (list1[1] == list3[5] == list5[9] == bcolors.OKBLUE+ "O" + bcolors.ENDC) or
        (list1[9] == list3[5] == list5[1] == bcolors.OKBLUE+ "O" + bcolors.ENDC)
    ):
        print("Player Two (O) wins!")
        return True

    else:
        return False


def placeX_1():
    turns = 9
    while turns >0:
            placex = input("\nWhat number slot would you like to place your X? ")
            if placex.lower() not in ["1","2","3","4","5","6","7","8","9"]:
                print("\nPlease enter a number 1-9 ")
                break
            elif placex.lower() == "1":
                if list1[1] == bcolors.WARNING + "X" + bcolors.ENDC or list1[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[1] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "2":
                if list1[5] == bcolors.WARNING + "X" + bcolors.ENDC or list1[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[5] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "3":
                if list1[9] == bcolors.WARNING + "X" + bcolors.ENDC or list1[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[9] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "4":
                if list3[1] == bcolors.WARNING + "X" + bcolors.ENDC or list3[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[1] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "5":
                if list3[5] == bcolors.WARNING + "X" + bcolors.ENDC or list3[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[5] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "6":
                if list3[9] == bcolors.WARNING + "X" + bcolors.ENDC or list3[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[9] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "7":
                if list5[1] == bcolors.WARNING + "X" + bcolors.ENDC or list5[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[1] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "8":
                if list5[5] == bcolors.WARNING + "X" + bcolors.ENDC or list5[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[5] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placex.lower() == "9":
                if list5[9] == bcolors.WARNING + "X" + bcolors.ENDC or list5[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[9] = bcolors.WARNING + "X" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break



def placeO_1():
    turns = 9
    while turns >0:
            placeO = input("\nWhat number slot would you like to place your O? ")
            if placeO.lower() not in ["1","2","3","4","5","6","7","8","9"]:
                print("\nPlease enter a number 1-9 ")
                break
            elif placeO.lower() == "1":
                if list1[1] == bcolors.WARNING + "X" + bcolors.ENDC or list1[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[1] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "2":
                if list1[5] == bcolors.WARNING + "X" + bcolors.ENDC or list1[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[5] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "3":
                if list1[9] == bcolors.WARNING + "X" + bcolors.ENDC or list1[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list1[9] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "4":
                if list3[1] == bcolors.WARNING + "X" + bcolors.ENDC or list3[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[1] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "5":
                if list3[5] == bcolors.WARNING + "X" + bcolors.ENDC or list3[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[5] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "6":
                if list3[9] == bcolors.WARNING + "X" + bcolors.ENDC or list3[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list3[9] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "7":
                if list5[1] == bcolors.WARNING + "X" + bcolors.ENDC or list5[1] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[1] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "8":
                if list5[5] == bcolors.WARNING + "X" + bcolors.ENDC or list5[5] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[5] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break

            elif placeO.lower() == "9":
                if list5[9] == bcolors.WARNING + "X" + bcolors.ENDC or list5[9] == bcolors.OKBLUE + "O" + bcolors.ENDC:
                    print("\nNot available")
                    continue
                else:
                    list5[9] = bcolors.OKBLUE + "O" + bcolors.ENDC
                    printBoard()
                    turns -=1
                    if check():
                        exit() 
                    break




def One_Player():
    printBoard()
    input("")

def Two_Player():
    printBoard()
    print("\nPlayer One (X) is going first and Player Two (O) is going second. ")
    turns = 9
    
    placeX_1()
    placeO_1()
    placeX_1()
    placeO_1()
    placeX_1()
    placeO_1()
    placeX_1()
    placeO_1()
    placeX_1()
    
    print("Out of turns Tie")
    exit()
        


while True:
    initial = input("how many players? ")
    if initial.lower() not in ["1", "2"]:
        print("Please enter 1 or 2.")
        continue
    elif initial.lower() == "1":
        One_Player()
    elif initial.lower() == "2":
        Two_Player()
        
        
