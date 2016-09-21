x = 0


# This holds everything that can happen in Phase 1
def phase_1():
    global x
    print("This is Phase 1")
    phase1 = raw_input("Will you be turning? ")
    if phase1 in ['yes', 'Yes', 'y', 'Y']:
        print ("You turned!")
    else:
        print ("End of turn.")

    # This code is for ending the game
    # It changes the value of x depending on the answer
    # It only stops the loop, meaning the game will continue until phase 5 is complete
    #
    # It is in every phase method and the plan is to have the data saved when the game is ended

    #                                ^
    # Figure this out in the future / \
    #                                |
    #                                |
    #                                |

    x = raw_input("Will you end the game? ")
    if x in ['yes', 'Yes', 'y', 'Y', '', ' ']:
        x == 1
        return x
    else:
        print ("you continued!")


# This holds everything that can happen in Phase 2
def phase_2():
    global x
    print ("This is Phase 2")
    phase2 = raw_input("Can you move? ")
    if phase2 in ['yes', 'Yes', 'y', 'Y']:
        print ("You moved!")
    else:
        print ("You didn't move.")
    x = raw_input("Will you end the game? ")
    if x in ['yes', 'Yes', 'y', 'Y', '', ' ']:
        x == 1
        return x
    else:
        print ("you continued!")


# This holds everything that can happen in Phase 3
def phase_3():
    global x
    print ("This is Phase 3")
    phase3 = raw_input("Will you be turning? ")
    if phase3 in ['yes', 'Yes', 'y', 'Y']:
        print ("You turned!")
    else:
        print ("You didn't turn.")
    x = raw_input("Will you end the game? ")
    if x in ['yes', 'Yes', 'y', 'Y', '', ' ']:
        x == 1
        return x
    else:
        print ("you continued!")


# This holds everything that can happen in Phase 4
def phase_4():
    global x
    print ("This is Phase 4")
    phase4 = raw_input("Can you move? ")
    if phase4 in ['yes', 'Yes', 'y', 'Y']:
        print ("You moved!")
    else:
        print ("You didn't move.")
    x = raw_input("Will you end the game? ")
    if x in ['yes', 'Yes', 'y', 'Y', '', ' ']:
        x == 1
        return x
    else:
        print ("you continued!")


# This holds everything that can happen in Phase 5
def phase_5():
    global x
    print ("This is Phase 5")
    phase5 = raw_input("Will you be turning? ")
    if phase5 in ['yes', 'Yes', 'y', 'Y', '', ' ']:
        print ("You turned!")
    else:
        print ("You didn't turn.")
    x = raw_input("Will you end the game? ")
    if x in ['yes', 'Yes', 'y', 'Y']:
        x == 1
        return x
    else:
        print ("you continued!")
