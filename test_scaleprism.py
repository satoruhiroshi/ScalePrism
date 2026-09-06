# test_scaleprism.py
"""
Tests for ScalePrism module.
"""

import unittest
from scaleprism import ScalePrism

class TestScalePrism(unittest.TestCase):
    """Test cases for ScalePrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ScalePrism()
        self.assertIsInstance(instance, ScalePrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ScalePrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
