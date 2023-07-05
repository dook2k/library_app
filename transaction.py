import datetime
import uuid
from abc import ABC, abstractmethod
from lendables import Lendable

# Create a transaction class that will be the parent class for all transactions. Subclasses will specify a transaction type.
# Transaction class will have a branch, patron, transaction_id, date, and transaction_type.
class Transaction(ABC):
  def __init__(self, branch, patron):
    self.branch = branch
    self.patron = patron
    self.transaction_id = uuid.uuid1().hex
    self.date = datetime.datetime.now()
       
  @property
  @abstractmethod
  def transaction_type(self):
    pass
  

  # CheckOut is a child of Transaction. It will have a due date, and a transaction type of 'Checkout'. Checkout will have due_date specified at creation based on the applicable
  #  lendable object's lending rules. Checkout will specify max_renewals from the lendable object, and track the number of renewals remaining.  Finally, CheckOut will have a method to determine the total fines incurred as of a datetime passed to that method.
  #  The default datetime should be the date of running that method.  The daily_late_fee default for all lendables needs to be specified in the Lendable class and can be overridden in its child classes.
  #   A Renewal(Transaction) class will effectuate the renewal of a lendable object. CheckIn(Transaction) will effectuate the checkin of a lendable object. CheckIn will should return total late fees incurred as of date of checkin.  

class CheckOutTransaction(Transaction):
  def __init__(self, branch, patron, item: Lendable):
    super().__init__(branch, patron)
    self.type = 'Checkout'
    self.item = item
    self.due_date = self.set_due_date(item)
    self.max_renewals = item.get_max_renewals()
    self.remaining_renewals = self.max_renewals
    self.daily_late_fee = item.get_daily_late_fee()
    self.total_fines = 0

class CheckInTransaction(Transaction):
  pass

class RenewalTransaction(Transaction):
  pass


# def __init__(self, branch, patron):
#     super().__init__(branch, patron)

#   @property
#   def transaction_type(self):
#     return 'Checkout'
  
#   @property
#   def set_due_date(self):
#     now = datetime.datetime(now)

# # class Loan(CheckOut):
# #   def __init__(self):
# #     self.transaction = Transaction
# #     self.due_date = 


# # class Loan (tracks due date, daily fees perhaps, library, item, patron; created by a checkout transaction; checkin
# # transaction )

# class CheckOut(Transaction):
#   def __init__(self, branch, patron, item: Lendable):
#     super().__init__(branch, patron)
#     self.type = 'Checkout'

#   def get_type(self):
#     return self.type





