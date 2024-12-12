from turtle import Turtle

ST_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(3):
            self.add_segments(ST_POSITIONS[i])
        self.head=self.segments[0]

    def add_segments(self,pos):
        segments = Turtle('square')
        segments.color('white')
        segments.penup()
        segments.setposition(pos)
        self.segments.append(segments)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move old segments off-screen
        self.segments.clear()
        self.create_snake()  # Recreate snake
        self.head = self.segments[0]
