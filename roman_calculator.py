
def to_int(r_value):
	if not type(r_value) == str or not r_value:
		raise ValueError 

	roman_int_map = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

	extra_keys = [i for i in r_value if i not in roman_int_map.keys()]
	if extra_keys:

		return 0
	else:
		r_value_len = len(r_value)
		i_value = []
		for ch_index in range(r_value_len):
			ch = r_value[ch_index]
			ch_value = roman_int_map[ch]
			if ch_index < r_value_len - 1:
				next_value = roman_int_map[r_value[ch_index + 1]]
				if ch_value < next_value:
					ch_value *= -1
			i_value.append(ch_value)
		return sum(i_value)

def to_roman(int_value):

	if not type(int_value) == int or not int_value or int_value < 1:
		raise ValueError
	integers = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
	romans = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
	roman_numeric = ""
	for index,value in enumerate(integers):
		count=int(int_value/value)
		roman_numeric += romans[index] * count
		int_value -= count * value
	return roman_numeric

def roman_calculator(arg1,arg2,operator):
	if arg1.isalpha() == False or arg2.isalpha() == False:
		return "invalid input !!!!!!!!"

	arg1_int=to_int(arg1.upper())
	arg2_int=to_int(arg2.upper())
	if arg1_int == 0 or arg2_int == 0:
		return "Invalid numerics !!!!!"
	else:
		if arg1_int == 0 or arg2_int == 0:
			return "Invalid roman numeric"
		else:
			if operator == "+":
				sum_value = arg1_int + arg2_int
				roman_value = to_roman(sum_value)
				return roman_value
			
			elif operator == "-":

				sub_value = arg1_int - arg2_int
				if sub_value < 1:
					raise ValueError
				roman_value = to_roman(sub_value)
				return roman_value

			
			elif operator == "*":
				mul_value = arg1_int * arg2_int
				roman_value = to_roman(mul_value)
				return roman_value

			elif operator == "/":
				div_value = arg1_int / arg2_int
				if div_value < 1:
					raise ValueError
				roman_value = to_roman(div_value)
				return roman_value

print roman_calculator("vii","V","-")