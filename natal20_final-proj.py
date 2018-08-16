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
flip_counter = 0



#lists
#shape_list = ["compost.gif", "globalwarming.gif", "greenearth.gif", "airpollution.gif", "leaf.gif", "plasticwaste.gif", "poorturtle.gif", "waterpollution1.gif"]  
##pos_list[]
#variables
#pic_size = 300SIZE_X = 1000
SIZE_Y = 1000

flip = [False] * 17


cards = ["0",pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9,pic10,pic11,pic12,pic13,pic14,pic15,pic16]
# this function changes to the card when user clicks
# pic 1 = pic 13
# pic 2 = pic 9
# pic 3 = pic 10
# pic 4 = pic 12
# pic 5 = pic 8
# pic 6 = pic 15
# pic 7 = pic 14
# pic 11 = pic 16
matches = {
    (1, 13): "Consumers in North America and Europe waste about 209 to 253 pounds of food per person every year.",
    (2, 9): "40% of the lakes in America are too polluted for fishing, aquatic life, and swimming",
    (3, 10): "9% of the Arctic Sea ice is melting in every decade",
    (4, 12): "Most of this air pollution we cause results from the burning of fossil fuels, such as coal, oil, natural gas, and gasoline to produce electricity and power our vehicles. ",
    (5, 8): "Over 100 million marine animals are killed each year due to plastic",
    (6, 15): "There are many things we can do to help the environment. For example, walk or ride your bike instead of using your car",
    (7, 14): "There are many things we can do to reduce water pollution. For example: run the dishwasher or clothes washer only when full",
    (11, 16): "300 million tons of plastic is produced globally each year. Only about 10 percent of that is recycled"
}

# logic stuff aka smart stuff
def check_flips(card):  # card is the index of the card just flipped over
    global num_flipped, flip_counter
    num_flipped += 1
    if num_flipped == 2:
        card2 = flip.index(True)  # card2 is the index of the previously flipped card
        flip_counter += 1
        if (card, card2) in matches or (card2, card) in matches:
            if (card, card2) in matches:
                print(matches[(card, card2)])
            else:
                print(matches[(card2, card)])
            cards[card].hideturtle()
            cards[card2].hideturtle()
            flip[card2] = False
            num_flipped = 0
            print("So far you have used " + str(flip_counter) + " guesses")

        else:  # not a match
            print("Not a match!")
            time.sleep(1)
            flip[card2] = False
            cards[card].shape("gamecard.gif")
            cards[card2].shape("gamecard.gif")
            num_flipped = 0

    else:
        flip[card] = True
                    

        
# graphics stuf
#this sets the images as cards
def compost_flip1(x, y):
    pic1.shape("compost.gif")
    check_flips(1)
    
def compost_flip2(x,y):
    pic13.shape("compost.gif")
    check_flips(13)

def globalw_flip1(x,y):
    pic3.shape("globalwarming.gif")
    check_flips(3)
    
def globalw_flip2(x,y):
    pic10.shape("globalwarming.gif")
    check_flips(10)

def airpollution_flip1(x,y):
    pic4.shape("airpollution.gif")
    check_flips(4)

def airpollution_flip2(x,y):
    pic12.shape("airpollution.gif")
    check_flips(12)

def greenearth_flip1(x,y):
    pic6.shape("greenearth.gif")
    check_flips(6)
    
def greenearth_flip2(x,y):
    pic15.shape("greenearth.gif")
    check_flips(15)

def wp_flip1(x,y):
    pic2.shape("waterpollution1.gif")
    check_flips(2)
    
def wp_flip2(x,y):
    pic9.shape("waterpollution1.gif") 
    check_flips(9)
    
def leaf_flip1(x,y):
    pic7.shape("leaf.gif")
    check_flips(7)

def leaf_flip2(x,y):
    pic14.shape("leaf.gif")
    check_flips(14)
    
def poor_flip1(x,y):
    pic5.shape("poorturtle.gif")
    check_flips(5)
    
def poor_flip2(x,y):
    pic8.shape("poorturtle.gif")
    check_flips(8)
   
def plastic_flip1(x,y):
    pic11.shape("plasticwaste.gif")
    check_flips(11)

def plastic_flip2(x,y):
    pic16.shape("plasticwaste.gif")
    check_flips(16)

    
    
    
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

          
turtle.mainloop() 

