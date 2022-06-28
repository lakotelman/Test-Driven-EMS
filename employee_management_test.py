from employee_management import Role, Employee, Manager, Supervisor, Post
import unittest
from unittest.mock import patch


class TestEms(unittest.TestCase):
    def test_employee_init(self):
        e = Employee("Bilbo", "Baggins")
        self.assertIn(e, e.all_)
        self.assertFalse(e.posts)
        self.assertEquals("bilbob@codingtemple.com", e.email)
        self.assertTrue(e.role)  #!Had to add employee Roles to make this test pass

    def test_create_manager(self):
        e = Employee("Gandalf", "Thegray")
        m = Manager("Treebeard", "Ent")
        self.assertFalse(m.employees)

    def test_add_employee(self):
        e = Employee("Saruman", "Thewhite")
        m = Manager("Sauron", "Maia")
        m.add_employee(e)
        self.assertIn(e, m.employees)
        
    def test_remove_employee(self):
        e = Employee("Saruman", "Thewhite")
        m = Manager("Sauron", "Maia")
        m.add_employee(e)
        m.remove_employee(e.email)
        self.assertFalse(m.employees)

    @patch('builtins.print')
    def test_supervisor(self, mock_print):
        s = Supervisor("Galadriel", "Lothlórien")
        s.create_post()
        mock_print.assert_called_with("Sorry, Administrator do not have Post priveleges")

    def test_employee_post(self):
        e = Employee("Samwise", "Gamgee")
        e.create_post("Hello?") #! added argument body = "" to the function
        self.assertTrue(e.posts)

    def test_get_emp_by_email(self):
        e = Employee("Gimli", "Gloinson")
        self.assertEquals(e.get_employee_by_email(e.email), e)



if __name__ == "__main__":
    unittest.main()
