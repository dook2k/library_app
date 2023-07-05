import unittest
from classes import User, Patron, Librarian, Book, InventoryManager, Lendable, CD, LibrarySystem, Branch

class TestLibrarySystem(unittest.TestCase):
  def test_create_branch(self):
    system = LibrarySystem("United Phoenix Library System")
    main_branch = system.create_branch("Main Branch")
    self.assertIsInstance(main_branch, Branch)
    self.assertEqual(main_branch.name, "Main Branch")
    self.assertIn(main_branch, system.branches)

  def test_add_patron(self):
    system = LibrarySystem("United Phoneix Library System")
    patron1 = system.add_patron("Walter")
    self.assertIsInstance(patron1, Patron)
    self.assertEqual(patron1.name, "Walter")
    self.assertIn(patron1, system.patrons)

  def test_add_lendable(self):
    system = LibrarySystem("United Phoneix Library System")
    main_branch = system.create_branch("Main Branch")
    book1 = Book("Test Book1", "Test Author 1", main_branch)
    self.assertIs(book1.assigned_branch, main_branch)     
    self.assertIsInstance(book1, Book)
    system.add_lendable(book1)
    self.assertIsInstance(book1, Book)
    self.assertEqual(book1.title, "Test Book1")
    self.assertEqual(book1.author, "Test Author 1")
    self.assertIn(book1, system.lendables)

if __name__ == '__main__':
    unittest.main()