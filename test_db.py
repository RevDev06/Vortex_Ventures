import unittest
import mysql.connector
from unittest.mock import patch, MagicMock
from conex_db import database

class TestDatabase(unittest.TestCase):
    @patch('mysql.connector.connect')
    def setUp(self, mock_connect):
        self.mock_db = MagicMock()
        mock_connect.return_value = self.mock_db
        self.mock_cursor = MagicMock()
        self.mock_db.cursor.return_value = self.mock_cursor
        self.db = database()

    def test_init(self):
        self.mock_db.is_connected.assert_called_once()
        self.mock_db.cursor.assert_called_once()

    def test_close_conex(self):
        self.db.close_conex()
        self.mock_cursor.close.assert_called_once()
        self.mock_db.close.assert_called_once()

    def test_comit(self):
        self.db.comit()
        self.mock_db.commit.assert_called_once()

    def test_select_db(self):
        self.db.select_db()
        self.mock_cursor.execute.assert_called_once_with("USE db_poo;")



if __name__ == '__main__':
    unittest.main()