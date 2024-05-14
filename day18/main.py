# import colorgram
import turtle as t

tim = t.Turtle()
screen = t.Screen()
# colors = colorgram.extract('day18\colors.png', 21)
tim.color("white")
tim.turtlesize(1)

# # rgb_values = [color.rgb for color in colors]
# rgb_colors = []
# # Create a list to store RGB tuples

# for color in colors:
#     # r = color.rgb.r
#     # g = color.rgb.g
#     # b = color.rgb.b
#     # new_color = (r, g, b)
#     # rgb_colors.append(new_color)
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(rgb_colors)
# lengst = 10
# height = 10
# dot size = 20
# space apart = 50
color_list = [(245, 211, 177), (232, 132, 91), (204, 141, 148), (242, 193, 89), (84, 84, 104), (128, 178, 154), (210, 42, 40), (246, 127, 0), (42, 157, 142), (0, 48, 73), (38, 70, 83), (156, 74, 80), (56, 60, 89), (147, 154, 163), (208, 78, 76), (239, 167, 154), (25, 22, 17), (22, 27, 23), (217, 194, 199), (209, 180, 186)]
t.colormode(255)
# def rgb_to_hex(rgb_tuple):
#     """Converts an RGB tuple (R, G, B) to a hexadecimal color string."""
#     hex_code = "#{:02x}{:02x}{:02x}".format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
#     return hex_code
# first_color_hex = rgb_to_hex(color_list[0])
tim.pensize(20)
item_in_list = 0
start_point = -220
for _ in range(10):
    tim.penup()
    tim.goto(-265, start_point)
    start_point += 50
    tim.pendown()
    for _ in range(10):
        tim.pencolor(color_list[item_in_list])
        item_in_list +=1
        if item_in_list == 20:
            item_in_list = 0
        
        tim.forward(0)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.forward(0)
    # for _ in range(10):
        
    #     tim.dot(20, color_list[item_in_list])
    #     item_in_list +=1
    #     if item_in_list == 21:
    #         item_in_list = 0
    #     tim.penup()
    #     tim.forward(50)
    #     tim.pendown()
    #     tim.forward(1)
# for i, rgb in enumerate(rgb_values):
#     print(f"Color {i + 1}: RGB {rgb}")

# zero_color = colors[0]
# rgb0 = zero_color.rgb 
# first_color = colors[1]
# rgb1 = first_color.rgb 
# second_color = colors[2]
# rgb2 = second_color.rgb 
# third_color = colors[3]
# rgb3 = third_color.rgb 
# fourth_color = colors[4]
# rgb4 = fourth_color.rgb 
# fifth_color = colors[5]
# rgb5 = fifth_color.rgb 
# sixth_color = colors[6]
# rgb6 = sixth_color.rgb 
# seventh_color = colors[7]
# rgb7 = seventh_color.rgb 
# eighth_color = colors[8]
# rgb8 = eighth_color.rgb 
# ninth_color = colors[9]
# rgb9 = ninth_color.rgb 
# tenth_color = colors[10]
# rgb10 = tenth_color.rgb 
# eleventh_color = colors[11]
# rgb11 = eleventh_color.rgb 
# twelfth_color = colors[12]
# rgb12 = twelfth_color.rgb 
# thirteenth_color = colors[13]
# rgb13 = thirteenth_color.rgb 
# fourteenth_color = colors[14]
# rgb14 = fourteenth_color.rgb 
# fifteenth_color = colors[15]
# rgb15 = fifteenth_color.rgb 
# sixteenth_color = colors[16]
# rgb16 = sixteenth_color.rgb 
# print(rgb0)
screen.exitonclick()
t.mainloop()