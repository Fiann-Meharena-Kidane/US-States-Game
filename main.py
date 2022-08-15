import turtle, pandas

screen = turtle.Screen()

screen.title("US States Game")
image = "blank_states_img.gif"   # assign image name to a variable
turtle.addshape(image)

turtle.shape(image)   # change turtle shape to image
turtle.setup(width=900, height=600)

data = pandas.read_csv('50_states.csv')   # open csv file
gameOn = True
states = 50

while gameOn:
    answer = screen.textinput(title=f"{states} states left", prompt="Enter State Name").lower()
    # user asked to type state name, f string used coz we gonna update state count with time,

    if answer=='exit':  # stops game when user types eixt
        gameOn=False
        break

    for state in data.state:  # holds states under 'state' column of our csv file
        if answer == state.lower(): # if user input is in the csv file,
            locate = turtle.Turtle()   # create a turtle
            locate.penup()
            locate.hideturtle()
            locateRow = data[data.state == state]  # holds the row with the state name
            locateX = int(locateRow.x)              # gets its x value
            locateY = int(locateRow.y)
            locate.goto(locateX, locateY)  # places the text on its respective position
            locate.write(state)  # writes the state name
            states -= 1  # update state count


# TODO uses should not guess same name twice
# TODO position of both text box and score board
# TODO


def get_mouse_click_coor(x, y):  # function to tell x and y coordinate of a mouth click
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

screen.exitonclick()
