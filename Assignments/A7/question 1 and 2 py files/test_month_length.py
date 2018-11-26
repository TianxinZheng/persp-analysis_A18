import month_length

def test_month_length():
    assert month_length.month_length("January") == 31, \
    "failed on month with 31 days" 
    assert month_length.month_length("September") == 30, \
    "failed on month with 30 days"
    assert month_length.month_length("February") == 28, \
    "failed on February with none-leap year"
    assert month_length.month_length("February", True) == 29, \
    "failed on February with leap year"
    assert month_length.month_length("not a month") == None, \
    "failed on month not given"