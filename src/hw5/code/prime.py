from time import time
def isPrime(n):
	for i in range(2, n): #From 2 to n - 1
		if n % i == 0: #if i divides n, return false
			return False
	return True

def main():
	final_count = int(input("How many primes do you want? ")) #Get number of prime numbers
	print("The first", final_count, "primes are:", end=' ') #Print
	start = time()
	last_prime = 2 #initalize last prime to the first prime number 
	current_number = 2 #set current number to 2
	count_prime = 0 #the count of prime numbers
	count_twins = 0 #the count of twins

	while count_prime < final_count:
		if isPrime(current_number): #If the number is prime
			print(str(current_number), end = ' ') #print number
			count_prime += 1 #Increase prime count
			if current_number - last_prime == 2: #If numbers are twins
				count_twins += 1 #Increase twin count
			last_prime = current_number #Set last prime to current prime
		current_number += 1 #Increase current number by one
	print()
	print("Amongst these there are", count_twins, "twin primes.")
	print()
	end = time()
	print("Time: ", end-start)

if __name__ == "__main__":
	main()