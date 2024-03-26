#1. Create a greeting for your program.
print(
    "Welcome to Vugar's first app, which generates a band name, and also unfortunately looks stupid =) "
)
#2. Ask the user for the city that they grew up in.
user_name = input("What is your name dear user? ")
print("Nice to meet you dear " + user_name)
users_city = input(
    "If it is not secret could you tell me what is the name of the city you grew up in? "
)
#3. Ask the user for the name of a pet.
users_pet = input(
    "If you have or had pet What is or was it is name ? (if you never had a pet what would you name it if you had it ?) "
)

#4. Combine the name of their city and pet and show them their band name.
prefered_band_name = users_city + users_pet
prefered_second_band_name = users_city + user_name
#5. Make sure the input cursor shows on a new line:
print("My first suggestion for your band name is " + prefered_band_name)
print("My second suggestion for your band name is " +
      prefered_second_band_name)