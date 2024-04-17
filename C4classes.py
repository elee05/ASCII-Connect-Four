# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 23:11:28 2024

@author: sirer
"""

    

class Board:

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.slots = [[' '] * width for x in range(height)] 


    def __repr__(self):
        s = ''         

        for row in range(self.height):
            s += '|'   

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n' 

  
        s += ('-'  + '-' * self.width * 2)
        s += '\n'
        cols = []
        for i in range(self.width):
            cols += [i]
        for i in range(len(cols)):
            while cols[i] >= 10:
                cols[i] = cols[i] % 10
           
            s += (' ' + str(cols[i])) 
        
            
        
        return s

    def add_checker(self, checker, col):
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        while True:
            for i in range(self.height):
                if self.slots[i][col] != ' ':
                    if i == 0:
                        return
                    else:
                        self.slots[i - 1][col] = checker
                        return
                elif (i + 1) == (self.height):
                    self.slots[i][col] = checker
                    return
    
    def reset(self):
        self.slots = [[' '] * self.width for x in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        if self.slots[0][col] != ' ':
            return False
        return True
    
    def is_full(self):
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False
        return True
    
    def remove_checker(self, col):
        for i in range(self.height):
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                return
            
    
    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False   

    def is_vertical_win(self,checker):
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False   
    
    def is_diagonal_positive_win(self,checker):
        for row in range(3, self.height):
            for col in range(self.width -3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
                
    def is_diagonal_negative_win(self,checker):
        for row in range(self.height - 3):
            for col in range(self.width -3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
                
    def is_win_for(self, checker):
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) == True or self.is_horizontal_win(checker) == True or self.is_diagonal_negative_win(checker) == True or self.is_diagonal_positive_win(checker) == True:
            return True
        return False
    
class Player:
    
    
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the 
        Player object’s opponent."""
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
        
    
    def next_move(self, b):
        while True:
            attempted_placement = int(input('Enter a column: '))
            if attempted_placement >= 0 and attempted_placement < b.width:
                if b.can_add_to(attempted_placement) == True:
                    self.num_moves += 1
                    return attempted_placement
            print('Try Again!')
