#!/usr/bin/python3

def subby(ln):
	subb = 0
	ml = max(ln)

	for n in ln:
		if ml > n:
			subb += n

	return (ml - subb)


def roman_to_int(roman_string):
	if not roman_string:
	return 0

	 if not isinstance(roman_string, str):
		return 0

	r_nume = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	k_list = list(r_nume.keys())

	m = 0
	om = 0
	l = [0]

	for ch in roman_string:
		for r in k_list:
  			if r == ch:
				if r_nume.get(ch) <= om:
					m += subby(l)
					l = [r_nume.get(ch)]
				else:
					l.append(r_nume.get(ch))

				om = r_nume.get(ch)

	m += subby(l)

	return (m)
