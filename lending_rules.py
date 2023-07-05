# Description: This file contains the lending rules for the library
from abc import ABC, abstractmethod

# Define a Strategy Interface for lending rules
class LendingRules(ABC):
    @abstractmethod
    def lending_period_days(self):
        pass
    
    @abstractmethod
    def renewal_period_days(self):
        pass
    
    @abstractmethod
    def max_renewals(self):
        pass
    @abstractmethod
    def daily_late_fee_cents(self):
      pass
          
# Define a concrete strategy for Physical Media
class PhysicalMediaLendingRules(LendingRules):
  def lending_period_days(self):
    return 1
  
  def renewal_period_days(self):
    return 2
  
  def max_renewals(self):
    return 3
  
  @property
  def daily_late_fee_cents(self):
    return 100
  
  def get_daily_late_fee(self):
    return self.daily_late_fee_cents
  
  def change_daily_late_fee(self, new_fee):
    self.daily_late_fee_cents = new_fee


# Define a concrete strategy for Books
class BookLendingRules(LendingRules):
  def lending_period_days(self):
    return 4
  
  def renewal_period_days(self):
    return 5
  
  def max_renewals(self):
    return 6
  
  @property
  def daily_late_fee_cents(self):
    return 300

# Define a concrete strategy for CDs
class CDLendingRules(LendingRules):
  def lending_period_days(self):
    return 7
  
  def renewal_period_days(self):
    return 8
  
  def max_renewals(self):
    return 9
  
  @property
  def daily_late_fee_cents(self):
    return 200

# Define a concrete strategy for Digital Media
class DigitalMediaLendingRules(LendingRules):
  def lending_period_days(self):
    return 10
  
  def renewal_period_days(self):
    return 11
  
  def max_renewals(self):
    return 12
  
  @property
  def daily_late_fee_cents(self):
    return 400