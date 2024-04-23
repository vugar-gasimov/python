# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse3")
# timmy.forward(100)
# my_screen = Screen()

# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon Name", "Pokemon Type"]
# table.add_row(["Pickachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# table.add_row(["Hobart", "Wind"])
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander", "Hobart"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire", "Wind"])
table.align["Pokemon Name"] = "l"
table.align["Pokemon Type"] = "r"
print(table)