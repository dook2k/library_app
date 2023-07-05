import datetime
from datetime import timedelta
import uuid
from abc import ABC, abstractmethod
from lending_rules import LendingRules, PhysicalMediaLendingRules
from user import Patron


class Lendable(ABC):
  def __init__(self, title, lending_rules: LendingRules):
    self.title = title
    self.is_checked_out = False
    self.lent_to = None
    self.id = uuid.uuid1().hex
    self.created_at = datetime.datetime.now()
    self.lending_rules = lending_rules
    self.lending_period_days = self.get_lending_period_days()
    self.max_renewals = self.get_max_renewals()
    self.renewal_period_days = self.get_renewal_period_days()
    self.daily_late_fee_cents = self.get_daily_late_fee_cents()
  
  def get_lending_period_days(self):
    return self.lending_rules.lending_period_days()
  
  def get_max_renewals(self):
    return self.lending_rules.max_renewals()
  
  def get_renewal_period_days(self):
    return self.lending_rules.renewal_period_days()
  
  def get_daily_late_fee_cents(self):
    return self.lending_rules.daily_late_fee_cents()

  def checkout(self, patron: Patron):
    # consider implementing this in the librarysystem class

    # lending_period_days specified by child class
    self.set_due_date(self.lending_period_days)
    # Implement rest of checkout method here in parent class child classes will specify the lending_period_days and renewal periods 
    self.is_checked_out = True
    self.lent_to = patron
    patron.checked_out_items.append(self)
    print(f"Checked out {self.title} to {patron.name} successfully.  It's due on {self._due_date}, with {self._renewals} renewal(s) of {str(self.renewal_period_days)} days available.")
    return(self)

  def set_due_date(self, lending_period_days):
    # Get current date and time
    now = datetime.datetime.now()

    # Convert lending period of days to a time delta
    lending_period_object = timedelta(days=lending_period_days)

    # Calculate due date
    due_date = now + lending_period_object

    # Set time to 23:59:00
    self._due_date = due_date.replace(hour=23, minute=59, second=59)

  def renew(self):
    if self.renewals > 0:
      self._renewals -= 1
      # Implement renewal behavior here
    else:
      raise ValueError("No more renewals are authorized for this item.  Please check it back in before it is due to avoid late fees!")

  def checkin(self):
    self._renewals = self.max_renewals
    # Implement checkin behavior here

  # Create method to change to new lending rules by passing in a new lending rules object/class
  def change_lending_rules(self, new_lending_rules: LendingRules):
    self.lending_rules = new_lending_rules()


  def __str__(self):
    str = f"Title: {self.title}\nChecked Out: {self.is_checked_out}\nLent To: {self.lent_to}\nLending Rules:\n Max Renewals: {self.get_max_renewals()}\n Renewal Period: {self.get_renewal_period_days()}\n Lending Period: {self.get_lending_period_days()}\n"
    return str
  

  
  
class DigitalMedia(Lendable):
  pass

class PhysicalMedia(Lendable):
  def __init__(self, title, assigned_branch, lending_rules: LendingRules = PhysicalMediaLendingRules()):
    super().__init__(title, lending_rules)
    self.title = title
    self.branch = assigned_branch

    def reassign_branch(new_branch):
      self.branch = new_branch

class Book(PhysicalMedia):
    def __init__(self, title, author, assigned_branch, lending_rules: LendingRules = None):
      if lending_rules is None:
        lending_rules = PhysicalMediaLendingRules()
      super().__init__(title, author, lending_rules)
      self.title = title
      self.author = author
      self.assigned_branch = assigned_branch

class CD(PhysicalMedia):
    def __init__(self, title, assigned_branch, lending_rules: LendingRules = None):
      if lending_rules is None:
        lending_rules = PhysicalMediaLendingRules()
      super().__init__(title, lending_rules)
      self.title = title
      self.assigned_branch = assigned_branch