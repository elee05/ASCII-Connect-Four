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
        """ Returns a string that represents a Board object.
        """
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
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        
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
        

    
    ### add your reset method here ###
    
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

    ### add your remaining methods here
    
    def can_add_to(self, col):
        """that returns True if it is valid to place a checker in the column col 
        on the calling Board object. Otherwise, it should return False."""
        if self.slots[0][col] != ' ':
            return False
        return True
    
    def is_full(self):
        """that returns True if the called Board object is completely full of checkers, 
        and returns False otherwise."""
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board object. 
        If the column is empty, then the method should do nothing."""
        for i in range(self.height):
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                return
            
    
    def is_horizontal_win(self, checker):
        
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False   

    def is_vertical_win(self,checker):
        """Checks for a vertical win for the specified checker."""
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False   
    
    def is_diagonal_positive_win(self,checker):
        """Checks for a diagonal positive slope win for the specified checker."""
        for row in range(3, self.height):
            for col in range(self.width -3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
                
    def is_diagonal_negative_win(self,checker):
        """Checks for a diagonal negative slope win for the specified checker."""
        for row in range(self.height - 3):
            for col in range(self.width -3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
                
    def is_win_for(self, checker):
        """accepts a parameter checker that is either 'X' or 'O', 
        and returns True if there are four consecutive slots containing checker on the board. 
        Otherwise, it should return False."""
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) == True or self.is_horizontal_win(checker) == True or self.is_diagonal_negative_win(checker) == True or self.is_diagonal_positive_win(checker) == True:
            return True
        return False
    
class Player:
    
    
    def __init__(self, checker):
        """constructs a new Player object by initializing the following two attributes:

an attribute checker – a one-character string that represents the gamepiece for the player, 
as specified by the parameter checker

an attribute num_moves – an integer that stores how many moves the player has made so far. 
This attribute should be initialized to zero to signify that the Player object
 has not yet made any Connect Four moves."""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """that returns a string representing a Player object. 
        The string returned should indicate which checker the Player object is using."""
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """that returns a one-character string representing the checker of the 
        Player object’s opponent. The method may assume that the calling Player object 
        has a checker attribute that is either 'X' or 'O'."""
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O':
            return 'X'
        
    
    def next_move(self, b):
        """that accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move. To do this,
        the method should ask the user to enter a column number that represents 
        where the user wants to place a checker on the board. 
        The method should repeatedly ask for a column number until 
        a valid column number is given."""
        while True:
            attempted_placement = int(input('Enter a column: '))
            if attempted_placement >= 0 and attempted_placement < b.width:
                if b.can_add_to(attempted_placement) == True:
                    self.num_moves += 1
                    return attempted_placement
            print('Try Again!')