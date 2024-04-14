# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:34:57 2024

@author: sirer
"""

from C4classes import *
import random

class ComputerPlayer(Player):
    """Intelligent opponent"""
    
    def  __init__(self, checker, tiebreak, lookahead):
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):

        prev = super().__repr__()
        return   prev + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score. """
        
        
        best = 0
        best_index = 0
        bi_list = []
        for i in range(len(scores)):
            if scores[i] > best:
                best = scores[i]
                best_index = i
        for i in range(len(scores)):
            if scores[i] == best:
                bi_list += [i]

       # print(best, best_index, bi_list)

        
        if self.tiebreak == 'LEFT':
            return bi_list[0]
        elif self.tiebreak == 'RIGHT':
            return bi_list[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(bi_list)
        
        
        
    def scores_for(self, b):
        """takes a Board object b and determines the the best option by 
        designating values of -1, 0 50, and 100 for each possible option
        Returns a list containing one score for each column."""
        
        scores  = ['k'] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
                
                
            else:
                b.add_checker(self.checker, col)
                opponent = ComputerPlayer(self.opponent_checker(), 'RANDOM', self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                else:
                    scores[col] = 0
                b.remove_checker(col)
                    
        return scores
    
    def next_move(self, b):
        """makes it so that computer player automatically choses next move based on
        set moves ahead"""
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.

          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    
    b = Board(6, 7)
    print(b)
    
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):


    print(str(p) + "'s" + ' turn')
    print()
    
    b.add_checker(p.checker, p.next_move(b)) 
    print()
    print(b)
    
   
    if b.is_win_for(p.checker) == True:
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
              
def main():
    print('Welcome to Connect Four!')
    print()
    while True:
        selection = (input('1 or 2 player(s):'))
        if selection == '1':
            print('YOU WILL NOW FACE THE COMPUTER')
            print('YOU ARE X')
            connect_four(Player('X'), ComputerPlayer('O', 'RANDOM', 3))
            
            break
            
        elif selection == '2':
            print('X GOES FIRST')
            connect_four(Player('X'), Player('O'))
       
            
            break
        elif selection == 'cancel':
            break
        else:
            print('INVALID CHOICE, TRY AGAIN')
            print('(type cancel to end)')
            
main()
    
    
