# test_eosaccount.py
"""
Tests for EOSAccount module.
"""

import unittest
from eosaccount import EOSAccount

class TestEOSAccount(unittest.TestCase):
    """Test cases for EOSAccount class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EOSAccount()
        self.assertIsInstance(instance, EOSAccount)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EOSAccount()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
