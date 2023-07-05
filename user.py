import uuid
import datetime


class User:
  def __init__(self, name):
    self.name = name
    self.id = uuid.uuid1().hex
    self.created_at = datetime.datetime.now()

class Librarian(User):
  def __init__(self, name, branch):
    super().__init__(name, branch)
    
class Patron(User):
  def __init__(self, name):
    super().__init__(name)
    self.name = name
    self.checked_out_items = []
    self.history = []
 
  def __str__(self):
    if len(self.checked_out_items) == 0:
      return "\nPatron has no items checked out!"
    else:
      checked_out_items_str = ''
      for item in self.checked_out_items:
        checked_out_items_str += str(item.title) 
      return f"Patron: {self.name}\nChecked Out Items:\n{checked_out_items_str}"