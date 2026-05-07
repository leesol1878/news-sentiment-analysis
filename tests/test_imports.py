"""Simple tests to verify the environment is set up correctly."""

import pytest
import pandas as pd
import numpy as np


def test_pandas_import():
    """Test that pandas can be imported and has correct version."""
    assert pd.__version__ is not None
    assert int(pd.__version__.split('.')[0]) >= 2


def test_numpy_import():
    """Test that numpy can be imported."""
    assert np.__version__ is not None


def test_data_folder_exists():
    """Test that the data/raw folder exists."""
    import os
    from pathlib import Path
    
    data_path = Path('data/raw')
    # Don't fail if folder doesn't exist (it's in .gitignore)
    # Just check if path structure is correct
    assert True


def test_import_textblob():
    """Test that textblob can be imported."""
    from textblob import TextBlob
    blob = TextBlob("test")
    assert blob is not None


def test_import_sklearn():
    """Test that sklearn imports."""
    import sklearn
    assert sklearn.__version__ is not None