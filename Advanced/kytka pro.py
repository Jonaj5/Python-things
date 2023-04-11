from turtle import *

speed(5)

for _ in range(6):
    for _ in range(6):
        forward(50)
        right(60)
    forward(50)
    left(60)

right(120)
forward(50)
left(60)


for _ in range(6):
    for _ in range(3):
        for _ in range(6):
            forward(50)
            right(60)
        forward(50)
        left(60)
    right(120)
    
mainloop()