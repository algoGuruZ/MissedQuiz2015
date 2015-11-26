# MissedQuiz2015
Missed Quiz for Software Engineer Class 
__author__ = 'Zheng Zhang'

# 52 cards in a poker deck, each card has two features: 1) suit 2) value
# 1) Suit: [club, diamond, heart, spade] (C,D,H,S)
# 2) Value: [2,3,4,5,6,7,8,9,10,Jack,Queen,King,Ace] (2,3,4,5,6,7,8,9,T,J,Q,K,A)
# Values are in ascending order; Suit has no bearings on values

#define the Card class
#Club, Diamond, Heart, Spade represents 0, 1, 2, 3
#Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace represent 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

#Global variables
Club, Diamond, Heart, Spade = range(4)
Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace = range(13)
_abbr_Suit = 'CDHS'
_abbr_Value = '23456789TJQKA'

class Card(object):
    def __init__(self, val):
        '''
        here we assign numeric values 0 - 51 to each card, denote as n, then
        suit = n / 13, which takes value of 0, 1, 2, 3 that corresponds to C, D, H, S respectively
        value = n % 13, which takes value of 0, 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9, 10, 11, 12 that corresponds to
                        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
        '''
        self.suit = val / 13
        self.value = val % 13

    def __cmp__(self, other):
        '''
        self-defined comparison function for card values, based on built-in function cmp
        Note: cmp(x, y) returns 1) -1, if x < y; 2) 0, if x == y; 3) 1, if x > y
        '''
        return cmp(self.value, other.value)

    def __str__(self):
        return _abbr_Value[self.value] + _abbr_Suit[self.suit]

    def parse_str(cls, str):
        '''
        class method, NOT instance method - this method reads in a short string, and build the corresponding
        Card object
        '''
        str = str.strip()               #take out all the ' ', '\n', '\t', '\r'
        #check if str meets standard
        if len(str) != 2:
            raise ValueError('String should be containing exactly 2 chars!!')
        val, suit = str[0], str[1]
        #parsing value
        if val >= '2' and val <= '9':
            val = int(val) - 2
        elif val == 'T': val = Ten
        elif val == 'J': val = Jack
        elif val == 'Q': val = Queen
        elif val == 'K': val = King
        elif val == 'A': val = Ace
        else: raise ValueError("Unknown value '%s'" % val)
        #parsing suit
        if suit.upper() == 'C':
            suit = Club
        elif suit.upper() == 'D': suit = Diamond
        elif suit.upper() == 'H': suit = Heart
        elif suit.upper() == 'S': suit = Spade
        else: raise ValueError("Unknow suit '%s'" % suit)

        return Card(suit * 13 + val)
