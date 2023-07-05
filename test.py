import unittest
import pdb
import datetime
import uuid
from abc import ABC, abstractmethod
from classes import Library, User, Patron, Librarian, Book, InventoryManager, Lendable

class TestInventoryManager(unittest.TestCase):
  
  def test_check_out(self):
    library = Library("Test Library")
    book = Book("Test Book", "Test Author")
    librarian = library.register_librarian()
    patron = library.register_patron()
    inventory_manager = InventoryManager(library)
    inventory_manager.add_to_inventory(book, librarian)

    inventory_manager.check_out(book, librarian, patron)
    self.assertTrue(book.is_checked_out)
    self.assertIn(book, inventory_manager.inventory)
    self.assertIn(book, patron.checked_out_items)
    self.assertEqual(book.lent_to, patron.id)

  def test_check_in(self):
    library = Library("Test Library")
    book = Book("Test Book", "Test Author")
    librarian = library.register_librarian()
    patron = library.register_patron()
    inventory_manager = InventoryManager(library)
    
    # Invalid item
    with self.assertRaises(ValueError):
      inventory_manager.check_in(librarian, librarian, patron)

    # Invalid librarian
    with self.assertRaises(PermissionError):
      inventory_manager.check_in(book, patron, patron)
    
    # Invalid patron
    with self.assertRaises(PermissionError):
      inventory_manager.check_in(book, librarian, librarian)
   
    # All arguments valid but item not in inventory 
    self.assertNotIn(book, inventory_manager.inventory)
    with self.assertRaises(ValueError):
      inventory_manager.check_in(book, librarian, patron)

    # Item in inventory but isn't checked out
    inventory_manager.add_to_inventory(book, librarian)
    self.assertIn(book, inventory_manager.inventory)
    with self.assertRaises(ValueError):
      inventory_manager.check_in(book, librarian, patron)

    # Item in inventory and is checked out but not to patron
      # Create new patron that doesn't check out the item
    new_patron = library.register_patron()
    self.assertEqual(len(new_patron.checked_out_items), 0)
      # Check out item to patron and run test of checking it back in using new_patron
    inventory_manager.check_out(book, librarian, patron)
    with self.assertRaises(PermissionError):
      inventory_manager.check_in(book, librarian, new_patron)

    # With valid item in inventory properly checked out and test check-in using proper arguments 
      # Confirm book checked out to patron
    self.assertFalse(book.lent_to == new_patron.id)
    self.assertEqual(book.lent_to, patron.id)
    self.assertTrue(book.is_checked_out)
    inventory_manager.check_in(book, librarian, patron)
    self.assertFalse(book.is_checked_out)
    self.assertIsNone(book.lent_to)
    self.assertNotIn(book, patron.checked_out_items)


  def test_add_to_inventory(self):
    library = Library("Test Library")
    book = Book("Test Book", "Test Author")
    librarian = library.register_librarian()
    patron = library.register_patron()
    inventory_manager = InventoryManager(library)
    
    # Invalid item
    with self.assertRaises(PermissionError):
      inventory_manager.add_to_inventory(patron, librarian)

    # Invalid librarian
    with self.assertRaises(PermissionError):
      inventory_manager.add_to_inventory(book, patron)

    # Item already in inventory
    inventory_manager.add_to_inventory(book, librarian)
    self.assertIn(book, inventory_manager.inventory)
    with self.assertRaises(ValueError):
      inventory_manager.add_to_inventory(book, librarian)

    
  
  def test_remove_from_inventory(self):
    library = Library("Test Library")
    book = Book("Test Book", "Test Author")
    librarian = library.register_librarian()
    patron = library.register_patron()
    inventory_manager = InventoryManager(library)
    # inventory_manager.add_to_inventory(book, librarian)
    
    # Invalid item
    with self.assertRaises(ValueError):
      inventory_manager.remove_from_inventory(book, librarian)

    # Invalid librarian
    with self.assertRaises(PermissionError):
      inventory_manager.remove_from_inventory(book, patron)

    # Item not in inventory
    self.assertNotIn(book, inventory_manager.inventory)
    with self.assertRaises(ValueError):
      inventory_manager.remove_from_inventory(book, librarian)

    # Item in inventory but currently checked out
    inventory_manager.add_to_inventory(book, librarian)
    self.assertIn(book, inventory_manager.inventory)
    inventory_manager.check_out(book, librarian, patron)
    self.assertTrue(book.is_checked_out)
    with self.assertRaises(PermissionError):
      inventory_manager.remove_from_inventory(book, librarian)


if __name__ == '__main__':
    unittest.main()
