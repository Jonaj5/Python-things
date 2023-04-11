from turtle import *

speed(5)

for _ in range(6):
    for _ in range(6):
        forward(50)
        right(60)
    forward(50)
    left(60)

mainloop()