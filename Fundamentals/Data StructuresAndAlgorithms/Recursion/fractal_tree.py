import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)


if __name__ == "__main__":
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.pensize(2)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("red")
    tree(45,  t)
    myWin.exitonclick()