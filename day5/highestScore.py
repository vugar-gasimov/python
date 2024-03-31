person_scores = input("\n Enter a list of people's scores with space: ").split()
for n in range(0, len(person_scores)):
  person_scores[n] = int(person_scores[n])

highest = 0 
for score in person_scores:
   if score > highest:
     highest = score 
print(f"\n The highest score in the class is: {highest}")
  