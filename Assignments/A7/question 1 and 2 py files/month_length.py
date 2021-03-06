def month_length(month, leap_year=False):
	if month in {"September", "April", "June", "November"}:
		return 30
	elif month in {"January", "March", "May", "July", \
	               "August", "October", "December"}:
	    return 31
	if month == "February":
		if not leap_year:
			return 28
		else:
			return 29
	else:
		return None
