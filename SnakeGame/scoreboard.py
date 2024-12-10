from turtle import Turtle

ALIGN='center'
FONT=("Courier", 16, "normal")
FONT2=("Courier", 20, "bold")
class ScoreBoard(Turtle):

    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)  # Position at the top-center of the screen.
        self.score=0
        self.update_s()




    def update_s(self):
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,50)
        self.write(f"GAME OVER! ", align=ALIGN, font=FONT)



    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_s() #updates score


    def increase(self):
        self.clear()
        self.score+=1
        self.update_s()
