#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

class NimGame:
    def __init__(self):
        self.game_mode = "Misere"
        self.number_pile = random.randint(2,5)
        
        self.computer = (0,0) # Computer's move
        self.pile_comp = 0 # pile number
        self.sticks_comp = 0 # the number of sticks
        
        self.player = (0,0) # Player's move
        self.pile_player = 0 # pile number
        self.sticks_player = 0 # the number of sticks
        
        self.current_player = ''
        self.piles = [] # All piles
        
        self.execution_time = []
        
        for n in range(self.number_pile):
            pile = '| '*(2*n+1)
            self.piles.append(pile.split(' '))
            self.piles[n].pop()
#         self.piles= [['|','|'],['|','|','|','|'],['|','|','|','|','|','|','|','|']]
#         self.piles= [['|','|'],['|','|','|','|'],['|','|'],['|','|','|','|'],['|','|','|']]
#         self.piles = [['|'],['|'],['|', '|']]
    def choose_mode(self):
        done = False
        self.game_mode = input("Which kind of Nim do you want to play? (Misere/Normal) ")
        list_mode = ['normal','Normal','misere','Misere']
        while not done:
            if self.game_mode in list_mode:
                done = True
            else:
                print('Please enter Normal or Misere!!!!')
                self.game_mode = input("Which kind of Nim do you want to play ?")
                
    def who_plays_first(self):
        done = False
        list_name = ['Computer','computer','You','you']
        self.current_player = input("Do you want who would like to play first? (Computer/You) ")
        while not done:
            if self.current_player in list_name:
                done = True
            else:
                print("\nPlease enter 'Computer' or 'You'")
                self.current_player = input("Do you want who would like to play first? (Computer/You) ")   
    
    def check_and_remove_empty_sub_lists(self):
        n = 0
        while n < len(self.piles): 
            if self.piles[n] == []: 
                del self.piles[n]
            else:
                n += 1
    
    def ask_pick(self):
        print('Which pile would you like to pick and how many sticks do you want?')
        while True:
            try:
                self.check_and_remove_empty_sub_lists()
                self.number_pile = len(self.piles)
                self.print_piles()
                pile = int(input('Enter pile number (the increment of pile number is from top to bottom): '))
                while (pile < 1 or pile > self.number_pile):
                    print('Please enter number is not over', self.number_pile)
                    pile = int(input('Enter pile number (the increment of pile number is from top to bottom): '))
                
                sticks = int(input('Enter the number of sticks: '))                
                while (sticks < 1 or sticks > len(self.piles[pile-1])):
                    print('Please enter number is not over', len(self.piles[pile-1]))
                    sticks = int(input('Enter the number of sticks: ')) 
                         
                break
            except ValueError:
                print('Please enter valid positive numbers.')
        return pile, sticks     
    
    def remove_sticks(self, pile, sticks):
        self.check_and_remove_empty_sub_lists()
                
        for stick in range(sticks):
            self.piles[pile-1].pop() # remove sticks
        self.print_piles()
    
    def print_piles(self):
        for pile in self.piles:
            print(' '.join(pile))
    
    def check_end_game(self):
        piles = [item for sublist in self.piles for item in sublist]
        if not piles:
            return True
  
    def who_wins(self):
        if self.game_mode.capitalize() == 'Misere':
            if(self.current_player.capitalize() == 'You'):
                print("Computer won")
            else:
                print("You won")
        else:
            if(self.current_player.capitalize() == 'You'):
                print("You won")
            else:
                print("Computer won")
            
    def find_biggest_pile(self, piles):
        biggest_pile = 0
        number_sticks = 0
        for n in range(len(piles)):
            if number_sticks < len(piles[n]):
                biggest_pile = n
                number_sticks = len(piles[n])
        return biggest_pile+1
    
    def computer_brain(self):
        start = time.time()

        self.check_and_remove_empty_sub_lists()
#         piles = [pile for pile in self.piles]
        piles = self.piles.copy()
        nim_sum = 0
        pile = 0
        sticks = 0
        for pile_item in piles:
            nim_sum ^= len(pile_item)

        if nim_sum == 0:
            pile = random.randint(1,len(piles))
            sticks = random.randint(1, len(piles[pile-1]))
            
            end = time.time()
            self.execution_time.append(end-start)
            print(pile,sticks)
            return pile, sticks
        else:
            if self.game_mode.capitalize() == 'Misere':
                biggest_pile = self.find_biggest_pile(piles)
                biggest_size = len(piles[biggest_pile-1])

                if (nim_sum < biggest_size):
                    temp_piles = piles.copy()
                    while True: 
                        biggest_pile = self.find_biggest_pile(temp_piles)
                        biggest_size = len(temp_piles[biggest_pile-1])
                        number_biggest_pile = 0
                        for pile in temp_piles:
                            if(len(pile) == biggest_size):
                                number_biggest_pile += 1
                        if (number_biggest_pile % 2 == 0):
                            n = 0
                            while n < len(temp_piles): 
                                if (len(temp_piles[n]) == biggest_size): 
                                    del temp_piles[n]
                                else:
                                    n += 1
                        else:
                            sticks = biggest_size
                            for i in range(len(piles)):
                                if(len(piles[i]) == biggest_size):
                                    pile = i+1

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                else:
                    size_1_count = 0
                    for pile in piles:
                        if (len(pile) == 1):
                            size_1_count += 1

                    if size_1_count + 1 == len(piles):
                        if size_1_count % 2 == 0:
                            pile = biggest_pile
                            sticks = biggest_size - 1

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                        else: 
                            pile = biggest_pile
                            sticks = biggest_size

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                    else:
    #                     print(self.piles)
                        while (nim_sum != 0):
                            sticks += 1
                            piles[biggest_pile-1].pop()
                            nim_sum = 0
                            for pile_item in piles:
                                nim_sum ^= len(pile_item)
                        pile = biggest_pile
    #                     print(self.piles)

                        print(pile, sticks)
                        end = time.time()
                        print(end-start)
                        self.execution_time.append(end-start)
                        return pile, 0
            else:
                biggest_pile = self.find_biggest_pile(piles)
                biggest_size = len(piles[biggest_pile-1])
                
                if (nim_sum < biggest_size):
                    temp_piles = piles.copy()
                    while True: 
                        biggest_pile = self.find_biggest_pile(temp_piles)
                        biggest_size = len(temp_piles[biggest_pile-1])
                        number_biggest_pile = 0
                        for pile in temp_piles:
                            if(len(pile) == biggest_size):
                                number_biggest_pile += 1
                        if (number_biggest_pile % 2 == 0):
                            n = 0
                            while n < len(temp_piles): 
                                if (len(temp_piles[n]) == biggest_size): 
                                    del temp_piles[n]
                                else:
                                    n += 1
                        else:
                            sticks = biggest_size
                            for i in range(len(piles)):
                                if(len(piles[i]) == biggest_size):
                                    pile = i+1

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                else:
                    size_1_count = 0
                    for pile in piles:
                        if (len(pile) == 1):
                            size_1_count += 1

                    if size_1_count + 1 == len(piles):
                        if size_1_count % 2 == 0:
                            pile = biggest_pile
                            sticks = biggest_size

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                        else: 
                            pile = biggest_pile
                            sticks = biggest_size - 1

                            print(pile, sticks)
                            end = time.time()
                            print(end-start)
                            self.execution_time.append(end-start)
                            return pile, sticks
                    else:
                        pile = random.randint(1,len(piles))
                        sticks = random.randint(1, len(piles[pile-1]))

                        end = time.time()
                        self.execution_time.append(end-start)
                        print(pile,sticks)
                        return pile, sticks
                
    def avg_exec_time(self):
        return sum(self.execution_time)/len(self.execution_time)
    
    def main(self):
        self.choose_mode()
        self.print_piles()
        end_game = False
        self.who_plays_first()
        
        if self.current_player.capitalize() == 'You':
            while not end_game:
                print("***Your turn: ")
                self.current_player = "You"
                self.pile_player, self.sticks_player = self.ask_pick()
                self.remove_sticks(self.pile_player, self.sticks_player)
                if self.check_end_game():
                    self.who_wins()
                    end_game = self.check_end_game()
                    break
                
                print("\n***Computer's turn: ")
                self.current_player = "Computer"
                self.pile_computer, self.sticks_computer = self.computer_brain()
                self.remove_sticks(self.pile_computer, self.sticks_computer)
                if self.check_end_game():
                    self.who_wins()
                    end_game = self.check_end_game()
                    break
        else: 
            while not end_game:
                print("***Computer's turn: ")
                self.current_player = "Computer"
                self.pile_computer, self.sticks_computer = self.computer_brain()
                self.remove_sticks(self.pile_computer, self.sticks_computer)
                if self.check_end_game():
                    self.who_wins()
                    end_game = self.check_end_game()
                    break

                print("\n***Your turn: ")
                self.current_player = "You"
                self.pile_player, self.sticks_player = self.ask_pick()
                self.remove_sticks(self.pile_player, self.sticks_player)
                if self.check_end_game():
                    self.who_wins()
                    end_game = self.check_end_game()
                    break
                    

nim = NimGame()
nim.main()

