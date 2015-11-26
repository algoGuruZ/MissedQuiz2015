# MissedQuiz2015
Missed Quiz for Software Engineer Class 
__author__ = 'Zheng Zhang'
from card import Card       #import the Card class

#Main purpose: receive a pair of 5 cards and compare the RANK of the two pairs to determine which one is of higher score
#if two pair are of the SAME RANK, we then follow the subrules to compare them
#Heuristically, we assign scores from 0 - 8 to each of the nine ranks here
#Global variables
HIGHCARD, PAIR, TWOPAIRS, THREEOFAKIND, STRAIGHT, FLUSH, FULLHOUSE, FOUROFAKIND, STRAIGHTFLUSH = range(9)

class PokerHand(object):
    #we define a serious of _find_ functions to determine if there is a specific rank in our hand
    #   and we take the maximum as our final Rank
    def __init__(self):
        self.members = []           #5 cards
        self.rank = HIGHCARD        #rank of the pokerhand
        self.values = []            #values of cards
        self.suits = []             #suits of cards

    #compare function
    def __cmp__(self, other):
        myRank = self._get_rank()
        yourRank = other._get_rank()
        if myRank < yourRank: return -1
        elif myRank > yourRank: return 1
        else:
            rank = myRank
            myvals = self.values
            yourvals = other.values
            #1) if both are strightflush
            if rank == STRAIGHTFLUSH:       #rank by the highest value
                myvals.sort(reverse=True)
                yourvals.sort(reverse=True)
                if myvals[0] > yourvals[0]: return 1
                elif myvals[0] < yourvals[0]: return -1
                else: return 0
            #2) if both are four of a kind
            elif rank == FOUROFAKIND:         #rank by the value of the four cards
                my_value_hash = {}
                your_value_hash = {}
                for val in myvals:
                    if val not in my_value_hash.keys():
                        my_value_hash[val] = 1
                    else: my_value_hash[val] += 1
                for val in yourvals:
                    if val not in your_value_hash.keys():
                        your_value_hash[val] = 1
                    else: your_value_hash[val] += 1
                #find the key with value of 4 and compare
                myKey = 0
                yourKey = 0
                for key in my_value_hash:
                    if my_value_hash[key] == 4: myKey = key
                for key in your_value_hash:
                    if your_value_hash[key] == 4: yourKey = key
                if myKey > yourKey: return 1
                elif myKey < yourKey: return -1
                else: return 0
            #3) Fullhouse
            elif rank == FULLHOUSE:         #rank by the value of the three cards
                my_value_hash = {}
                your_value_hash = {}
                for val in myvals:
                    if val not in my_value_hash.keys():
                        my_value_hash[val] = 1
                    else: my_value_hash[val] += 1
                for val in yourvals:
                    if val not in your_value_hash.keys():
                        your_value_hash[val] = 1
                    else: your_value_hash[val] += 1
                #find the key with value of 3 and compare
                myKey = 0
                yourKey = 0
                for key in my_value_hash:
                    if my_value_hash[key] == 3: myKey = key
                for key in your_value_hash:
                    if your_value_hash[key] == 3: yourKey = key
                if myKey > yourKey: return 1
                elif myKey < yourKey: return -1
                else: return 0
            #4) Flush
            elif rank == FLUSH:         #rank by the rule of HighCard
                myvals.sort(reverse=True)
                yourvals.sort(reverse=True)
                for num in range(0,5):
                    if myvals[num] > yourvals[num]: return 1
                    elif myvals[num] < yourvals[num]: return -1
                return 0
            #5) Stright
            elif rank == STRAIGHT:      #rank by their highest card
                myvals.sort(reverse=True)
                yourvals.sort(reverse=True)
                #SPECIAL CASE: A, 2, 3, 4, 5 < T, J, Q, K, A
                if myvals[0] == 12 and myvals[1] == 3:
                    if yourvals[0] == 12 and yourvals[1] == 3:
                        return 0
                    else: return -1
                elif myvals[0] > yourvals[0]: return 1
                elif myvals[0] < yourvals[1]: return -1
                else: return 0
            #6) Three-of-a-kind
            elif rank == THREEOFAKIND:  #rank by the value of the three cards
                my_value_hash = {}
                your_value_hash = {}
                for val in myvals:
                    if val not in my_value_hash.keys():
                        my_value_hash[val] = 1
                    else: my_value_hash[val] += 1
                for val in yourvals:
                    if val not in your_value_hash.keys():
                        your_value_hash[val] = 1
                    else: your_value_hash[val] += 1
                #find the key with value of 3 and compare
                myKey = 0
                yourKey = 0
                for key in my_value_hash:
                    if my_value_hash[key] == 3: myKey = key
                for key in your_value_hash:
                    if your_value_hash[key] == 3: yourKey = key
                if myKey > yourKey: return 1
                elif myKey < yourKey: return -1
                else: return 0
            #7) Two pairs
            elif rank == TWOPAIRS:      #rank by higher of the two pairs and then the remaining
                my_value_hash = {}
                your_value_hash = {}
                for val in myvals:
                    if val not in my_value_hash.keys():
                        my_value_hash[val] = 1
                    else: my_value_hash[val] += 1
                for val in yourvals:
                    if val not in your_value_hash.keys():
                        your_value_hash[val] = 1
                    else: your_value_hash[val] += 1
                #find the two keys with value of 2 and compare
                myKey1 = 0
                myKey2 = 0
                myremaining = 0
                sum1 = 0
                yourKey1 = 0
                yourKey2 = 0
                yourremaining = 0
                sum2 = 0
                for key in my_value_hash:
                    if my_value_hash[key] == 2:
                        myKey1 = max(key,myKey1)
                        sum1 += key
                    else: myremaining = key
                for key in your_value_hash:
                    if your_value_hash[key] == 3:
                        yourKey1 = max(key, yourKey1)
                        sum2 += key
                    else: yourremaining = key
                myKey2 = sum1 - myKey1
                yourKey2 = sum2 - yourKey1
                if myKey1 > yourKey1: return 1
                elif myKey1 < yourKey1: return -1
                else:
                    if myKey2 > yourKey2: return 1
                    elif myKey2 < yourKey2: return -1
                    else:
                        if myremaining > yourremaining: return 1
                        elif myremaining < yourremaining: return -1
                        else: return 0
            #8) Pair
            elif rank == PAIR:          #rank by the value forming the pairs and then the remaining in descending order
                my_value_hash = {}
                your_value_hash = {}
                for val in myvals:
                    if val not in my_value_hash.keys():
                        my_value_hash[val] = 1
                    else: my_value_hash[val] += 1
                for val in yourvals:
                    if val not in your_value_hash.keys():
                        your_value_hash[val] = 1
                    else: your_value_hash[val] += 1
                #find the key with value of 2 and compare
                myKey = 0
                yourKey = 0
                for key in my_value_hash:
                    if my_value_hash[key] == 2:
                        myKey = key
                        myvals.remove(key)
                        myvals.remove(key)
                for key in your_value_hash:
                    if your_value_hash[key] == 2:
                        yourKey = key
                        yourvals.remove(key)
                        yourvals.remove(key)
                if myKey > yourKey: return 1
                elif myKey < yourKey: return -1
                else:
                    myvals.sort(reverse=True)
                    yourvals.sort(reverse=True)
                    for num in range(0,3):
                        if myvals[num] > yourvals[num]: return 1
                        elif myvals[num] < yourvals[num]: return -1
                    return 0
            #9) High Card:
            else:
                myvals.sort(reverse=True)
                yourvals.sort(reverse=True)
                for num in range(0,5):
                    if myvals[num] > yourvals[num]: return 1
                    elif myvals[num] < yourvals[num]: return -1
                return 0

    #add cards to pokerhand
    def add(self, card):
        #insert cards into members
        self.members.append(card)
        self.values.append(card.value)
        self.suits.append(card.suit)


    #read string
    def parse_hand(cls, str):
        #parse string and build PokerHand Class: 2H, 3D, 5S, 9C, KD
        x = Card(1)
        myHand = PokerHand()   #build an object
        for element in str.split():
            x = Card.parse_str(x, element)
            myHand.add(x)
        return myHand

    #_find_ functions
    #1. Straight flush
    def _find_straight_flush(self):
        #sort from highest to lowest
        self.values.sort(reverse=True)
        self.suits.sort(reverse=True)
        theSuit = self.suits[0]
        for i in range(1,5):
            if self.suits[i] != theSuit:
                return False
        #consider values
        #special case: A, 2, 3, 4, 5
        if self.values[0] != 12:        #largest is NOT A
            for i in range(1,5):
                if self.values[i-1] - self.values[i] != 1:
                    return False
        else:   #largest is A
            if self.values[1] != 3:
                for i in range(1,5):
                    if self.values[i-1] - self.values[i] != 1:
                        return False
            else:
                for i in range(1,5):
                    if self.values[i] != 4 - i:
                        return False

        return True

    #2. Four of a kind
    def _find_four_of_a_kind(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        for num in value_hash:
            if value_hash[num] == 4:
                return True

        return False

    #3. Full-house
    def _find_full_house(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        theKeys = list(value_hash.keys())
        if len(theKeys) != 2:
            return False
        else:
            for key in value_hash:
                if value_hash[key] == 2 or value_hash[key] == 3:
                    return True
        return False

    #4. Flush
    def _find_flush(self):
        #sort from highest to lowest
        self.suits.sort(reverse=True)
        theSuit = self.suits[0]
        for i in range(1,5):
            if self.suits[i] != theSuit:
                return False
        if self._find_straight_flush():
            return False
        else:
            return True

    #5. Straight
    def _find_straight(self):
        #sort from highest to lowest
        self.values.sort(reverse=True)
        #consider values
        #special case: A, 2, 3, 4, 5
        if self.values[0] != 12:        #largest is NOT A
            for i in range(1,5):
                if self.values[i-1] - self.values[i] != 1:
                    return False
        else:   #largest is A
            if self.values[1] != 3:
                for i in range(1,5):
                    if self.values[i-1] - self.values[i] != 1:
                        return False
            else:
                for i in range(1,5):
                    if self.values[i] != 4 - i:
                        return False
        self.suits.sort(reverse=True)
        theSuit = self.suits[0]
        for i in range(1,5):
            if self.suits[i] != theSuit:
                return True
            else:
                return False

    #6. Three of a kind
    def _find_three_of_a_kind(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        theKeys = list(value_hash.keys())
        if len(theKeys) != 3:
            return False
        else:
            for key in value_hash:
                if value_hash[key] == 3:
                    return True
        return False

    #7. Two Pairs
    def _find_two_pairs(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        theKeys = list(value_hash.keys())
        if len(theKeys) != 3:
            return False
        else:
            for key in value_hash:
                if value_hash[key] == 2:
                    return True
        return False

    #8. Pairs
    def _find_pair(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        theKeys = list(value_hash.keys())
        if len(theKeys) != 4:
            return False
        else:
            for key in value_hash:
                if value_hash[key] == 2:
                    return True
        return False

    #9. High Card
    def _find_high_hard(self):
        value_hash = {}
        for val in self.values:
            if val not in value_hash.keys():
                value_hash[val] = 1
            else:
                value_hash[val] += 1
        theKeys = list(value_hash.keys())
        if len(theKeys) != 5:
            return False
        else:
            return True

    #Get the rank of the cards
    def _get_rank(self):
        if self._find_straight_flush():
            return STRAIGHTFLUSH
        elif self._find_four_of_a_kind():
            return FOUROFAKIND
        elif self._find_full_house():
            return FULLHOUSE
        elif self._find_flush():
            return FLUSH
        elif self._find_straight():
            return STRAIGHT
        elif self._find_three_of_a_kind():
            return THREEOFAKIND
        elif self._find_two_pairs():
            return TWOPAIRS
        elif self._find_pair():
            return PAIR
        else:
            return HIGHCARD
