'''
AWP | Astrodynamics with Python by Alfonso Gonzalez
https://github.com/alfonsogonzalez/AWP
https://www.youtube.com/c/AlfonsoGonzalezSpaceEngineering

Numerical Tools Library Unit Tests
'''

# 3rd party libraries
import pytest
import numpy as np

# AWP library
import numerical_tools as nt

# Treat all warnings as errors
pytestmark = pytest.mark.filterwarnings( 'error' )

def test_norm_zero_vector():
	assert nt.norm( [ 0, 0, 0 ] ) == 0.0

def test_norm_basic_usage():
	assert nt.norm( [ 1.0, 0, 0 ] ) == 1.0

def test_norm_pythagorean():
	assert nt.norm( [ 3.0, 4.0 ] ) == 5.0

def test_normed_zero_division_expect_throw():
	with pytest.raises( RuntimeWarning ):
		nt.normed( np.zeros( 3 ) )

def test_frame_transform_same_frame():
	arr = np.array( [ [ 1.0, 0.0, 0.0 ], [ 1.0, 0.0, 0.0] ] )
	arr_transformed = nt.frame_transform(
		arr, [ 0.0, 0.0 ], 'J2000', 'J2000' )
	assert np.all( arr == arr_transformed )