import turtle
import pandas
# with open("50_states.csv") as data:
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
screen=turtle.Screen()
screen.title("U.S.States Games")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess=[]
while len(guess)<50:
    answer_state=screen.textinput(title=f"{len(guess)}/50",prompt="What's another state name").title()
    guess.append(answer_state)
    if answer_state=="Exit":
        miss=[]
        for state in all_states:
            if state not in guess:
                miss.append(state)
        new_data=pandas.DataFrame(miss)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
