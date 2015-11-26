# MissedQuiz2015
Missed Quiz for Software Engineer Class 
__author__ = 'Zheng Zhang'
from card import Card
from poker_hand import PokerHand
import sys

#Global variables
WHITE, TIE, BLACK = range(-1, 2)
#Result message
RESULT = {
    BLACK: "Black wins.",
    TIE: "Tie.",
    WHITE: "White wins."
}

#######################################################################
###################1) Alt + F12 open Terminal##########################
####################2) key in - python main.py "inputfile.txt"#########

def main(inputfile_str):
    #main function
    file = open(inputfile_str, 'r')            #read file
    #read line by line
    for line in file:
        x = PokerHand()
        y = PokerHand()
        x = PokerHand.parse_hand(x, line[0:14])
        y = PokerHand.parse_hand(y, line[15:29])
        print RESULT[x.__cmp__(y)]

if __name__ == '__main__':
	main(sys.argv[1])
