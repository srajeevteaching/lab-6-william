from graphicsCS151 import *
def input_check(minimum,maximum):
    x=input("please input a starting x coordinate from " +str(minimum) + " to " + str(maximum))
    if not x.isdigit():
        print("please input only digits")
        input_check(minimum,maximum)
    x=float(x)
    if x >= minimum and x<= maximum:
        return x
    else:
        print("please choose a value in the given range")
        input_check(minimum,maximum)
def main():
    radius=15
    minimum=radius
    maximum=500-radius
    x_coord=input_check(minimum,maximum)
    window = make_window("Lab 6", 500, 500)
    circle = make_circle(x_coord, 20, radius)
    color_circle(circle, "Red")
    circle.draw(window)
    while circle.getCenter().getX() < 500 - radius:
        circle.move(5, 5)
        sleep(50)
    while circle.getCenter().getY() < 500 - radius:
        circle.move(-5, 5)
        sleep(50)
    while circle.getCenter().getX() > radius:
        circle.move(-5, -5)
        sleep(50)
    while circle.getCenter().getY() > radius:
        circle.move(5, -5)
        sleep(50)
    window.getMouse()
    window.close()

main()

