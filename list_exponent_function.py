Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def list_exponents(my_num):
	"This function will raise a number to the power of numbers 1 - 10 and list each result in succession."
	one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for numbers in one_to_ten:
		if my_num == 0 :
			print("Please use number greater than zero. Thanks!")
			break
		else :
			print('Raising', my_num, 'to the power of', numbers, 'results in')
			print('\t', my_num ** numbers)
			print()

>>> list_exponents(2)
Raising 2 to the power of 1 results in
	 2

Raising 2 to the power of 2 results in
	 4

Raising 2 to the power of 3 results in
	 8

Raising 2 to the power of 4 results in
	 16

Raising 2 to the power of 5 results in
	 32

Raising 2 to the power of 6 results in
	 64

Raising 2 to the power of 7 results in
	 128

Raising 2 to the power of 8 results in
	 256

Raising 2 to the power of 9 results in
	 512

Raising 2 to the power of 10 results in
	 1024

>>> list_exponents(5)
Raising 5 to the power of 1 results in
	 5

Raising 5 to the power of 2 results in
	 25

Raising 5 to the power of 3 results in
	 125

Raising 5 to the power of 4 results in
	 625

Raising 5 to the power of 5 results in
	 3125

Raising 5 to the power of 6 results in
	 15625

Raising 5 to the power of 7 results in
	 78125

Raising 5 to the power of 8 results in
	 390625

Raising 5 to the power of 9 results in
	 1953125

Raising 5 to the power of 10 results in
	 9765625

>>> list_exponents(1000)
Raising 1000 to the power of 1 results in
	 1000

Raising 1000 to the power of 2 results in
	 1000000

Raising 1000 to the power of 3 results in
	 1000000000

Raising 1000 to the power of 4 results in
	 1000000000000

Raising 1000 to the power of 5 results in
	 1000000000000000

Raising 1000 to the power of 6 results in
	 1000000000000000000

Raising 1000 to the power of 7 results in
	 1000000000000000000000

Raising 1000 to the power of 8 results in
	 1000000000000000000000000

Raising 1000 to the power of 9 results in
	 1000000000000000000000000000

Raising 1000 to the power of 10 results in
	 1000000000000000000000000000000

>>> 