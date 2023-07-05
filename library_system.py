import datetime
import uuid
from branch import Branch
from user import Patron
from lendables import Lendable

class LibrarySystem:
  def __init__(self, name):
    self.name = name
    self.branches = []
    self.patrons = []
    self.lendables = []
    self.transactions = []
    self.created_at = datetime.datetime.now()
    self.id = uuid.uuid1().hex
    print(f"{self.name} created!")

  def create_branch(self, branch_name):
    new_branch = Branch(branch_name)
    self.branches.append(new_branch)
    print(f"{new_branch.name} created!")
    return new_branch
  
  def add_patron(self, name):
    new_patron = Patron(name)
    self.patrons.append(new_patron)
    print(f"{new_patron.name} added as a new patron!")
    return new_patron

  def add_lendable(self, item: Lendable):
    self.lendables.append(item)