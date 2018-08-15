import turtle

#this inserts all pictures to the file

turtle.shape("square")
#this sets pictures as turtles.
pic1 = turtle.clone()
pic1.shape("gamecard.gif") 
pic2 = pic1.clone()
pic3 = pic1.clone()
pic4 = pic1.clone()
pic5 = pic1.clone()
pic6 = pic1.clone()
pic7 = pic1.clone()
pic8 = pic1.clone()
pic9 = pic1.clone()
pic10 = pic1.clone()
pic11 = pic1.clone()
pic12 = pic1.clone()
pic13 = pic1.clone()
pic14 = pic1.clone()
pic15 = pic1.clone()
pic16 = pic1.clone()

##placing the turtles in the right positions 
turtle.hideturtle()
pic1.penup()
pic1.goto(-365,365)
pic1.pendown()
pic2.penup()
pic2.goto(-123,365)
pic2.pendown()
pic3.penup()
pic3.goto(120,365)
pic3.pendown()
pic4.penup()
pic4.goto(365,365)
pic4.pendown()
pic5.penup()
pic5.goto(-365,123)
pic5.pendown()
pic6.penup()
pic6.goto(-123,123)
pic6.pendown()
pic7.penup()
pic7.goto(120,123)
pic7.pendown()
pic8.penup()
pic8.goto(365,123)
pic8.pendown()
pic9.penup()
pic9.goto(-365,-120)
pic9.pendown()
pic10.penup()
pic10.goto(-123,-120)
pic10.pendown()
pic11.penup()
pic11.goto(120,-120)
pic11.pendown()
pic12.penup()
pic12.goto(365,-120)
pic12.pendown()
pic13.penup()
pic13.goto(-365,-365)
pic13.pendown()
pic14.penup()
pic14.goto(-123,-365)
pic14.pendown()
pic15.penup()
pic15.goto(120,-365)
pic15.pendown()
pic16.penup()
pic16.goto(365,-365)
pic16.pendown()

#lists 
##pos_list[]
#variables
pic_size = 300
SIZE_X = 1000
SIZE_Y = 1000

# this function changes to the card when user clicks
turtle.register_shape("gamecard.gif")
turtle.setup(1000,1000)
turtle.register_shape("compost.gif")
turtle.register_shape("airpollution.gif")
turtele.register_shape()
turtle.register_shape("globalwarming.gif")
turtle.register_shape("greenearth.gif")
turtle.register_shape("waterpollution1.gif")
turtle.register_shape("leaf.gif")
turtle.register_shape("poorturtle.gif")

def compost_flip1(x, y):
    pic1.shape("compost.gif")
def compost_flip2(x,y):
    pic13.shape("compost.gif")
def globalw_flip1(x,y):
    pic3.shape("glabalwarming.gif")
def globalw_flip2(x,y):
    pic10.shape("glabalwarming.gif")
def airpollution_flip1(x,y):
    pic4.shape("airpollution.gif")
def airpolution_flip2(x,y):
    pic12.shape("airpollution.gif")
def greenearth_flip1(x,y):
    pic6.shape("greenearth.gif")
def greenearth_flip2(x,y):
    pic15.shape("greenearth.gif")
def wp_flip1(x,y):
    pic2.shape("waterpollution1.gif")
def wp_flip2(x,y):
    pic9.shape("waterpollution1.gif")
def leaf_flip1(x,y):
    pic7.shape("leaf.gif")
def leaf_flip2(x,y):
    pic14.shape("leaf.gif")
def poor_flip1(x,y):
    pic5.shape("poorturtle.gif")
def poor_flip2(x,y):
    pic8.shape("poorturtle.gif")
    
pic1.onclick(compost_flip1)
pic13.onclick(compost_flip2)
pic3.onclick(globalw_flip1)
pic10.onclick(globalw_flip2)

##def place_pics():
##    min_x=-int(SIZE_X/2/pic_size)+1
##    max_x=int(SIZE_X/2/pic_size)-1
##    min_y=-int(SIZE_Y/2/pic_size)-1
##    max_y=int(SIZE_Y/2/pic_size)+1
##    pic_x = random.randint(min_x,max_x)*pic_size
##    pic_y = random.randint(min_y,max_y)*pic_size 
    
    
    

if pic1.onclick + pic13.onclick == True:
    write("the fact")
    pic1.hidetrutle()
    pic13.hideturtle()











turtle.mainloop() 

