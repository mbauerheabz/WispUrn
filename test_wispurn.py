# test_wispurn.py
"""
Tests for WispUrn module.
"""

import unittest
from wispurn import WispUrn

class TestWispUrn(unittest.TestCase):
    """Test cases for WispUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WispUrn()
        self.assertIsInstance(instance, WispUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WispUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
