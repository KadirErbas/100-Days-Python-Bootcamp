import turtle # turtle modülünü içe aktar

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")

turtle_instance = turtle.Turtle() # bir kaplumbağa nesnesi oluştur
turtle_instance.color("black") # kaplumbağanın rengini siyah yap
turtle_instance.pensize(3) # kaplumbağanın kaleminin kalınlığını 5 yap


def turtle_forward():
    turtle_instance.forward(50)
def rotate_angle_right():
    turtle_instance.right(20)
def rotate_angle_left():
    turtle_instance.left(20)
def clear_screen():
    turtle_instance.clear()
def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

turtle_screen.listen()
turtle_screen.onkey(turtle_forward,"space")
turtle_screen.onkey(rotate_angle_right,"Down")
turtle_screen.onkey(rotate_angle_left,"Up")
turtle_screen.onkey(clear_screen,"c")
turtle_screen.onkey(turtle_return_home,"h")
turtle_screen.onkey(turtle_pen_down,"w")
turtle_screen.onkey(turtle_pen_up,"q")



# turtle.tracer(0) # kaplumbağanın hareketlerini izlemeyi kapat

turtle.mainloop()


