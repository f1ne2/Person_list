import unittest
from app.view import *


class TestController(unittest.TestCase):
    def setUp(self):
        self.flag = 1
        self.new_window = ViewTkinter(self.flag)

    def test_create_record_window(self):
        self.contact_id = "1"
        self.i = 1
        self.res = ViewTkinter.create_record_window(self.new_window, self.i,
                                                    self.contact_id)
        self.assertIsInstance(Person(Entry), type(self.res))
