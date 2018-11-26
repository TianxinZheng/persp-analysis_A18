import smallest_factor

def test_sf():
    assert smallest_factor.smallest_factor(1) == 1, "failed on 1"   
    assert smallest_factor.smallest_factor(4) == 2, "failed on square number"
    assert smallest_factor.smallest_factor(15) == 3, "failed on non-square number" 
    assert smallest_factor.smallest_factor(7) == 7, "failed on prime number"
