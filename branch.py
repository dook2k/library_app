import datetime
import uuid 
from user import Librarian

class Branch:
  def __init__(self, name):
    self.name = name
    self.librarians = []
    self.created_at = datetime.datetime.now()
    self.id = uuid.uuid1().hex

  def add_librarian(self):
    new_librarian = Librarian(self)
    if new_librarian not in self.librarians:
      self.librarians.append(new_librarian)
      print("New librarian registered!")
    return new_librarian
        
  def __str__(self):
    return self.name
