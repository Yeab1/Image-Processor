#import important libraries
from graphics import *
from tkinter.filedialog import asksaveasfilename as save

#create the introductions with a function
def printintro():
    print("Hello,")
    print("This program will enable you to make simple adjustments to any picture you choose...")
    print("It enables you to change your picture into grayscale, invert it, get it's stats and save.")

#open the image and create the window with buttons  using a function.
def openImage(picFile):
    #open and display the image
    img = Image(Point(0, 0), picFile)
    width = img.getWidth()
    height = img.getHeight()+40
    img.move(width // 2, (height // 2)+40)
    win = GraphWin(picFile, width, height)
    img.draw(win)

    #create the buttons and label them
    statsbtn = Rectangle(Point(20, 11), Point(130, 51)).draw(win)
    statslbl = Text(Point(73, 32), "Stats").draw(win)

    BWbtn = Rectangle(Point(145, 11), Point(255, 51)).draw(win)
    BWlbl = Text(Point(199, 32), "B&W").draw(win)

    invertbtn = Rectangle(Point(270, 11), Point(385, 51)).draw(win)
    invertlbl = Text(Point(325, 32), "Invert").draw(win)

    savebtn = Rectangle(Point(400, 11), Point(510, 51)).draw(win)
    savelbl = Text(Point(455, 32), "Save").draw(win)

    quitbtn = Rectangle(Point(525, 11), Point(630, 51)).draw(win)
    quitbtn.setFill("red")
    quitlbl = Text(Point(576, 32), "Quit").draw(win)

    #return the open image and the window
    return img, win

#make the function to convert to negative.
def convertToNegative(img):
    print("Converting to color negative...")
    #get every pixel.
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            r, g, b = img.getPixel(row, col)
            img.setPixel(row, col, color_rgb(255 - r, 255 - g, 255 - b))

        #change the old pixels with the new ones and update
        update()
    print("   ...Done.")

#create a function to create grayscale
def grayscale(img):
    print("Converting to color grayscale...")

    #get every pixel
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            r, g, b = img.getPixel(row,col)
            #make calculations to change in to grayscale.
            l = 0.299 * r
            m = 0.587 * g
            n = 0.114 * b
            x = int(round(l, 0))
            y = int(round(m, 0))
            z = int(round(n, 0))
            brightness = x + y + z
            img.setPixel(row,col, color_rgb(brightness, brightness, brightness))

        #update the picture column by column
        update()
    print("   ...Done.")

#create a function to get the coordinates of mouse clicks
#take the window and the check mouse click as parameters.
def mouseclick(win, click, image):
    x = click.getX()
    y = click.getY()
    if 385 > x > 270 and 11 < y < 51:
        convertToNegative(image)  # Image Negative
    if 255 > x > 140 and 11 < y < 51:
        grayscale(image)
    if 130 > x > 20 and 11 < y < 51:
        stats(image)
    if 630 > x > 525 and 11 < y < 51:
        win.close()
    if 510 > x > 400 and 11 < y < 51:
        newimage = save()
        image.save(newimage + ".png")

#create the stats function
def stats(img):
    #create lists to make the histogram with
    rhist = []
    bhist = []
    ghist = []

    #make accumulators to sum and count the number of pixels
    sumred = 0
    sumgreen = 0
    sumblue = 0
    number =0

    #create an empty histogram for all 3 colors.
    for i in range(256):
        rhist.append(0)
        bhist.append(0)
        ghist.append(0)

    #get every pixel
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            r, g, b = img.getPixel(row, col)
            #add information to the histograms. and count the number of pixels
            number += 1
            rhist[r] += 1
            bhist[b] += 1
            ghist[g] += 1

    print("       red   green    blue")
    #print the information in the histogram (the count of every brightness of every color bar in the pixels)
    for i in range(256):
        print(i, "{0:7}".format(rhist[i]), "{0:7}".format(ghist[i]),"{0:7}".format(bhist[i]))

        #add the colors
        sumred = sumred + rhist[i] * i
        sumgreen = sumgreen + ghist[i] * i
        sumblue = sumblue + bhist[i] * i

    #print all the outputs of the function
    print("mean of red: {0:7}".format(sumred/number))
    print("mean of green: {0:<7}".format(sumgreen/number))
    print("mean of blue: {0:<7}".format(sumblue/number))
    print("Number of pixels: ", number)

def main():

    #print the introduction for the program
    printintro()

    #make sure errors dont occur due to clicks.
    try:
        # get the name of the file to open
        inFile = input("Enter the name of a GIF or PNG file to convert: ")

        #open the file using the function above.
        image, win = openImage(inFile)

        #use a loop to check if mouse clicks and key presses exist.
        while True:
            p = win.checkMouse()
            k = win.checkKey()

            if k:
                if k == "q":
                    win.close()#close the window
            if p:
                # go to the above function to see where the click was.
                mouseclick(win, p, image)

    except GraphicsError:
        print("")
main()