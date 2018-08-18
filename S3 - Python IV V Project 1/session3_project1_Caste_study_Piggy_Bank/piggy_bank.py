# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 20:39:29 2018

@author: manoj
"""
class InvalidEntry(Exception):pass

class piggy_bank:
    def __init__(self,balance=0.0):
        self.balance=balance
    def add_amount(self,amount):
        self.balance = self.balance+amount
        print("After adding, your balanbce is {} rupees".format(self.balance))
    def withdraw_amount(self,amount):
        self.balance = self.balance-amount
        print("After withdrawing, your balanbce is {} rupees".format(self.balance))
    def check_balance(self):
        print("Your current balanbce is {} rupees".format(self.balance))
    def start(self):
        keep_running=True
        while keep_running:
            print('')
            print("Start or End : ",end="")
            start_stop=input()
            try:
                if start_stop.lower()=="start":
                    print("Add, Withdraw or Check : ",end="")
                    next_action=input()
                    if next_action.lower()=="add":
                        print("Add amount : ",end="")
                        amount=int(input())
                        self.add_amount(amount)
                    elif next_action.lower()=="withdraw":
                        print("Withdraw amount : ",end="")
                        amount=int(input())
                        self.withdraw_amount(amount)
                    elif next_action.lower()=="check":
                        self.check_balance()
                    else:
                        raise InvalidEntry()
                elif start_stop.lower()=="end":
                    keep_running=False
                else:
                    raise InvalidEntry
            except ValueError:
                print("Please enter a valid integer")
            except InvalidEntry:
                print("Please enter a valid option")
            finally:
                print("")