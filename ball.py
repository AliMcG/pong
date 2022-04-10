from turtle import Turtle

START_POS = (0, 0)


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move(self):
        # move towards top right
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

        # bounce down left:
        # new_x = self.xcor() + 10
        # new_y = self.ycor() - 10
        # self.goto(new_x, new_y)

        # bounce down right:
        # new_x = self.xcor() - 10
        # new_y = self.ycor() - 10
        # self.goto(new_x, new_y)

        # bounce up left:
        # new_x = self.xcor() - 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)

    # def move_ball(self):
    #     heading = 45
    #     self.setheading(heading)
    #     self.forward(10)
    #     # if self.ycor() <= 280:
    #     #     heading -= 90
    #     #     self.setheading(heading)
    #     #     self.forward(10)
    #     # new_x = self.xcor() + 10
    #     # new_y = self.ycor() + 10
    #     # self.goto(new_x, new_y)
    #     print(self.heading())
    #     # else:
    #     #     new_x = self.xcor() + 10
    #     #     new_y = self.ycor() - 10
    #     #     self.goto(new_x, new_y)
