from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.segment[0].setheading(0)

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_tail(pos)

    def add_tail(self, pos):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segment.append(new_seg)

    def extend(self):
        self.add_tail(self.segment[-1].position())
    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def move(self):
        for seg_id in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_id - 1].xcor()
            new_y = self.segment[seg_id - 1].ycor()
            self.segment[seg_id].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def bite_tail(self):
        for seg in self.segment[1:]:
            if self.head.distance(seg) <= 10:
                return True
        return False