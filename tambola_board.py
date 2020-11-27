# -*- coding: utf-8 -*-
"""
Python script for generating Tambola Number Board
BeautifulTable class is used for easily printing tabular data
in a visually appealing ASCII format to a terminal.
"""
import random as rd
from bs4 import BeautifulTable as bt

table = bt()
table.column_headers = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10']
table.column_alignments = bt.ALIGN_CENTER
table.set_style(bt.STYLE_BOX_DOUBLED)


def clear_board():
    """
    This module will display an empty board when the game will start.
    """
    table.clear()
    empty_list = []
    for _ in range(0, 9):
        for _ in range(1, 11):
            empty_list.append('-')
        table.append_row(empty_list)
        empty_list = []
    table.insert_column(0, "RowNo", ["Row1", "Row2", "Row3", "Row4", "Row5", "Row6", "Row7", "Row8", "Row9"])
    print(table)


# Function call for initialising an empty board
clear_board()


def fill_board():
    """
    This function handles the input from user, generating random number in the range and
    display in beautifultable.
    """
    entered_num_list = []
    count = 0
    while count < 90:
        try:
            inp = str(input('Enter n to pick a new number: '))
            count = count + 1
            # print("No of hits are {}".format(count))
            if inp[0] == 'n':
                rand_num = (rd.randint(1, 90))  # generate a random number from 1 to 90 , endpoints included
                while rand_num in entered_num_list:
                    rand_num = (rd.randint(1, 90))  # generate random number until a unique value is received.
                entered_num_list.append(rand_num)
                rand_num_str = list(str(rand_num))  # convert to string

                if len(rand_num_str) == 1:
                    table[0][int(rand_num_str[0])] = str(rand_num)
                elif rand_num % 10 == 0:
                    table[int(rand_num_str[0]) - 1][10] = str(rand_num)
                else:
                    table[int(rand_num_str[0])][int(rand_num_str[1])] = str(rand_num)
                print('\n' * 50)
                print(table)
                print("Current number is {} ".format(rand_num))
            elif inp == 'exit':
                count = 0
                break
            else:
                count = count - 1
        except Exception:
            count -= 1
            print("This is not a valid input, go and try again")
    else:
        print('Thank you for playing Housie!')


# Function call for filling the board
fill_board()
