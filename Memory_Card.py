import turtle
import time

turtle.setup(1000,1000)#window size

#this inserts all pictures to the file
turtle.register_shape("gamecard.gif")
turtle.register_shape("compost.gif")
turtle.register_shape("airpollution.gif")
turtle.register_shape("plasticwaste.gif")
turtle.register_shape("globalwarming.gif")
turtle.register_shape("greenearth.gif")
turtle.register_shape("waterpollution1.gif")
turtle.register_shape("leaf.gif")
turtle.register_shape("poorturtle.gif")

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

num_flipped = 0

#lists
#shape_list = ["compost.gif", "globalwarming.gif", "greenearth.gif", "airpollution.gif", "leaf.gif", "plasticwaste.gif", "poorturtle.gif", "waterpollution1.gif"]  
##pos_list[]
#variables
##SIZE_X = 1000
##SIZE_Y = 1000

flip = [False] * 17

flip_back = [True] * 17

cards = ["0",pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9,pic10,pic11,pic12,pic13,pic14,pic15,pic16]
# this function changes to the card when user clicks

#this sets the images as cards

def FlipCard(x,y firstPic, secondPic):
    global num_flipped
    num_flipped+=1
    flip[1] = True #sets the false as true
    pic1.shape("compost.gif")
    if flip[13]: 
        print('the fact')
        pic1.hideturtle()
        pic13.hideturtle()

    elif num_flipped % 2 == 0:
        print("not match")
        time.sleep(.5)
        flip[1] = False
        card_ind = flip.index(True)
        print(card_ind)
        cards[card_ind].shape("gamecard.gif")
        flip[card_ind] = False
        pic1.shape("gamecard.gif")
        print('wrong answer')
        num_flipped = 0

    
    
    
pic1.onclick(compost_flip1)
pic13.onclick(compost_flip2)
pic3.onclick(globalw_flip1)
pic10.onclick(globalw_flip2)
pic4.onclick(airpollution_flip1)
pic12.onclick(airpollution_flip2)
pic6.onclick(greenearth_flip1)
pic15.onclick(greenearth_flip2)
pic2.onclick(wp_flip1)
pic9.onclick(wp_flip2)
pic7.onclick(leaf_flip1)
pic14.onclick(leaf_flip2)
pic5.onclick(poor_flip1)
pic8.onclick(poor_flip2)
pic11.onclick(plastic_flip1)
pic16.onclick(plastic_flip2)


##def place_pics():
##    min_x=-int(SIZE_X/2/pic_size)+1
##    max_x=int(SIZE_X/2/pic_size)-1
##    min_y=-int(SIZE_Y/2/pic_size)-1
##    max_y=int(SIZE_Y/2/pic_size)+1
##    pic_x = random.randint(min_x,max_x)*pic_size
##    pic_y = random.randint(min_y,max_y)*pic_size 
          




turtle.mainloop() 

