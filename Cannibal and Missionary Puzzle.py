"""Three missionaries and three cannibals come to a river and find a boat that holds two people.
Everyone must get across the river to continue on the journey.
However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten."""

# There are 3 cannibals and 3 missionaries on the left bank to start
# Nobody is on the right bank to start
# everyone must get to right bank before moving on

# set up of initial configuration
# c stands for cannibals and m stands for missionaries
LeftBank = {'c': 3, 'm': 3}
RightBank = {'c': 0, 'm': 0}
boat = {'c': 0, 'm': 0}


def print_state(dct1, dct2, dct3):
    # Prints each configuration after each round
    # each round consists of the boat moving back and forth between banks.
    msg = """
    Left Bank: {} cannibal(s), {} missionary(ies)
    Right Bank: {} cannibal(s), {} missionary(ies)
    On boat: {} cannibal(s), {} missionary(ies)
    """
    print(msg.format(dct1['c'], dct1['m'], dct2['c'], dct2['m'],
                     dct3['c'], dct3['m']))


def numOfCannibalsAndMissionaries(lBank=LeftBank, rBank=RightBank, boat=boat):
    if all(x == 0 for x in rBank.values()):
        # Right bank is empty, cannibal gets on boat from left bank 
        print_state(lBank, rBank, boat)
        lBank['c'] -= 1
        boat['c'] += 1

    # 1 missionary leaves left bank and gets on the boat
    lBank['m'] -= 1  
    boat['m'] += 1  
    print_state(lBank, rBank, boat)

    if all(x == 0 for x in lBank.values()):  # left bank is empty, one missionary and cannibal get on boat and get off on right bank
        boat['c'], boat['m'] = 0, 0
        rBank['c'] += 1
        rBank['m'] += 1
        print_state(lBank, rBank, boat)
        return  # everyone is off of the left bank and are on the right bank. Complete.

    boat['m'] -= 1  # 1 missionary goes out of boat and gets on the right bank
    rBank['m'] += 1 
    print_state(lBank, rBank, boat)

    lBank['c'] -= 1  # 1 cannibal leaves left bank and gets on the boat
    boat['c'] += 1 
    print_state(lBank, rBank, boat)

    boat['c'] -= 1  # 1 cannibal gets out of the boat and gets on the right bank
    rBank['c'] += 1
    print_state(lBank, rBank, boat)

    numOfCannibalsAndMissionaries(lBank, rBank, boat)

def main():
    numOfCannibalsAndMissionaries()
    

if __name__ == '__main__':
    main()
