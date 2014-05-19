current_fibo_number = 0
fibo_one = 1
fibo_two = 1

sum_of_even_fibo_numbers = 0
while current_fibo_number < 4000000:
	
	current_fibo_number = fibo_one + fibo_two
	fibo_one = fibo_two
	fibo_two = current_fibo_number
	
	if current_fibo_number % 2 == 0:
		sum_of_even_fibo_numbers += current_fibo_number


print sum_of_even_fibo_numbers
