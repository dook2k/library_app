import datetime
import uuid
from abc import ABC, abstractmethod
import pdb
from lendables import Lendable, Book, CD
from user import Patron
from branch import Branch
from library_system import LibrarySystem  
from lending_rules import LendingRules, PhysicalMediaLendingRules, BookLendingRules, CDLendingRules, DigitalMediaLendingRules
from transaction import Transaction, CheckOutTransaction, CheckInTransaction, RenewalTransaction

system = LibrarySystem("United Phoneix Library System")
main_branch = system.create_branch("Main Branch")
coronado_branch = system.create_branch("Coronado Branch")
chula_branch = system.create_branch("Chula Branch")
patron1 = system.add_patron("Walter")
print(patron1)

book1 = Book('Test Book1', 'Test Author 1', main_branch)
print("Book with no lending rules should default ot physical media rules:\n", book1)
book2 = Book('Test Book2', 'Test Author 2', main_branch, PhysicalMediaLendingRules())
print("Book2 with Physical Media rules specified at creation (rules should be same as book1 above):\n", book2)

book1.change_lending_rules(BookLendingRules)
print("Book1 changed to have Book Lending Rules:\n", book1)
book2.change_lending_rules(CDLendingRules)
print("Book2 changed to have CD Lending Rules:\n", book2)
book3 = Book('Test Book3', 'Test Author 3', main_branch, CDLendingRules())
print("Book3 created with CD Lending Rules:\n", book3)
book3.change_lending_rules(DigitalMediaLendingRules)
print("Book3 changed to have Digital Media Lending Rules:\n", book3)
# create CD with no rules specified
cd1 = CD('Test CD1', main_branch)
print("CD with no lending rules should default ot physical media rules:\n", cd1)
cd2 = CD('Test CD2', main_branch, PhysicalMediaLendingRules())
print("CD2 with Physical Media rules specified at creation (rules should be same as CD1 above):\n", cd2)
cd2.change_lending_rules(BookLendingRules)
print("CD2 changed to have Book Lending Rules:\n", cd2)
print("CD2 daily late fee: ", cd2.max_renewals)

# cd1 = CD('The Eagles Greatest Hits', main_branch)
# print(cd1)

# # cd1.checkout(patron1)
# print(cd1)
# print(patron1)

# print(patron1.checked_out_items)

# print(book1.assigned_branch)

# book1.assigned_branch = chula_branch

# print(book1.assigned_branch)

