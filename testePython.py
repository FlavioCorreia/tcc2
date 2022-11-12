#pytest testePython.py

import pytest

def inc( a ):
    return a+1

def test_function():
    assert inc(1) == 2
    assert inc(1) == 1
    assert inc(2) == 3
    
def test_function3():
    assert inc(2) == 3
    
def test_function2():
    assert inc(2) == 1
