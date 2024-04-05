def prime_checker(number):
  if number < 2:
    return False
  
  for i in range(2, int(number**0.5)+1):
    if number % i == 0:
      return False
  return True
    
    
print("\n Welcome to prime number checker. \n")
n = int(input("Enter a number to check if it is prime or not ")) 
if prime_checker(number=n):
  print(f"\n {n} is a prime number.")
else:
  print(f"\n {n} is not a prime number.")


# def prime_checker(number):
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")
    

# n = int(input()) # Check this number
# prime_checker(number=n)