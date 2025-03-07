import pytest
from unittest.mock import patch, MagicMock
import random
from io import StringIO
import sys

from src.runner import run
from src.grid_generation import make_grid
from src.step import step

def test_run_with_seed():
    """Test that setting a seed produces consistent results"""
    with patch('sys.stdout', new=StringIO()) as fake_output:
        with patch('time.sleep') as mock_sleep:  # Don't actually sleep in tests
            # Run twice with same seed
            run(rows=3, cols=3, steps=1, seed=42)
            output1 = fake_output.getvalue()
            fake_output.seek(0)
            fake_output.truncate()
            
            run(rows=3, cols=3, steps=1, seed=42)
            output2 = fake_output.getvalue()
            
            assert output1 == output2  # Same seed should produce same grid

def test_run_interval():
    """Test that sleep is called with correct interval"""
    with patch('sys.stdout', new=StringIO()):
        with patch('time.sleep') as mock_sleep:
            mock_grid = [[0, 0], [0, 0]]
            with patch('src.grid_generation.make_grid', return_value=mock_grid):
                with patch('src.step.step', return_value=mock_grid):
                    test_interval = 0.5
                    run(rows=2, cols=2, steps=2, interval=test_interval)
                    assert mock_sleep.call_count == 2
                    mock_sleep.assert_called_with(test_interval)

def test_run_keyboard_interrupt():
    """Test that KeyboardInterrupt is handled gracefully"""
    with patch('sys.stdout', new=StringIO()) as fake_output:
        with patch('time.sleep', side_effect=KeyboardInterrupt):
            run(rows=2, cols=2)
            assert "Stopped by user." in fake_output.getvalue()

def test_run_default_parameters():
    """Test that function works with default parameters"""
    with patch('sys.stdout', new=StringIO()):
        with patch('time.sleep') as mock_sleep:
            # Should run without raising any exceptions
            run(rows=3, cols=3, steps=1)  # Only specify minimum required params

def test_run_zero_steps():
    """Test behavior with zero steps"""
    with patch('sys.stdout', new=StringIO()) as fake_output:
        with patch('time.sleep'):
            run(rows=2, cols=2, steps=0)
            # Should print initial grid but not step
            assert fake_output.getvalue().count('Generation') == 1

def test_run_small_interval():
    """Test with very small interval"""
    with patch('sys.stdout', new=StringIO()):
        with patch('time.sleep') as mock_sleep:
            run(rows=2, cols=2, steps=1, interval=0.001)
            mock_sleep.assert_called_with(0.001)

def test_run_invalid_probability():
    """Test with invalid probability values"""
    with patch('sys.stdout', new=StringIO()):
        with patch('time.sleep'):
            with pytest.raises(ValueError):
                run(rows=2, cols=2, alive_prob=1.5, steps=1)
            with pytest.raises(ValueError):
                run(rows=2, cols=2, alive_prob=-0.5, steps=1)

def test_run_deterministic_with_same_seed():
    """Test that the same seed produces the same grid multiple times"""
    with patch('sys.stdout', new=StringIO()):
        with patch('time.sleep'):
            final_grids = []
            for _ in range(3):
                with patch('src.step.step', return_value=[[0, 0], [0, 0]]):  # Mock step to return constant grid
                    result = run(rows=4, cols=4, steps=1, seed=42)
                    final_grids.append([row[:] for row in result])
            
            # All final grids should be identical when using the same seed
            assert all(grid == final_grids[0] for grid in final_grids[1:])
