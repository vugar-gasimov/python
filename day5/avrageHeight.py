print("\n Welcome to height calculator program to calculate people's average height enter their height like this 180 160 170 and etc... ")
people_heights = input("\n Enter heights of people separated by space: ").split()
for n in range(0, len(people_heights)):
  people_heights[n] = int(people_heights[n])

total_height = 0
for height in people_heights:
  total_height += height
print(f"\ntotal height = {total_height}")

num_people = 0
for person in people_heights:
  num_people +=1
print(f"number of people = {num_people}")
  
av_height = total_height / num_people
av_height_rounded = round(av_height)
print(f"average height = {av_height_rounded}\n")
