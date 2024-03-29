line1 = ["⬜️","️⬜️","⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","⬜️","️⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️","️⬜️","⬜️️"]
line4 = ["⬜️️","⬜️️","⬜️","️⬜️","⬜️️"]
line5 = ["⬜️️","⬜️️","⬜️","️⬜️","⬜️️"]
map = [line1, line2, line3, line4, line5]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ") 


row_letter = position[0].upper()
col = int(position[1]) - 1
row = ord(row_letter) - ord('A') # Get ASCII code of letter and subtract 'A' to get index

if not (row_letter in ['A', 'B', 'C', 'D', 'E'] and 1 <= col <= 3): 
    print("Invalid Position. Please enter a valid position like 'A2', 'B3', or 'C1'.")

map[col][row] = "X"


print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")

# ord(row_letter) - ord('A') calculates the numerical index for the row letter.
# ord() gets the ASCII code of the character.
# Subtracting ord('A') from the code of the row letter gives us the corresponding index (0 for 'A', 1 for 'B', and 2 for 'C').
# Example:
# ord('B') - ord('A') = 66 (code for 'B') - 65 (code for 'A') = 1 (index for 'B' in the map)
# ord('C') - ord('A') = 67 (code for 'C') - 65 (code for 'A') = 2 (index for 'C' in the map)

# Teacher's way

letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)