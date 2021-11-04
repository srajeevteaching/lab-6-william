from graphicsCS151 import *
def input_check(minimum,maximum,x):
    if not x.isdigit():
        print("please input only digits")
        return False
    x=float(x)
    if x >= minimum and x<= maximum:
        return True
    else:
        print("please choose a value in the given range")
        return False
def main():
    radius=15
    minimum=radius
    maximum=500-radius
    check=False
    while not check:
        x = input("please input a starting x coordinate from " + str(minimum) + " to " + str(maximum))
        check=input_check(minimum,maximum,x)
    x_coord=float(x)
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

