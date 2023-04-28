# myEtchASketch application

from tkinter import *

#####Set variables:
canvas_height = 800
canvas_width = 1600
canvas_colour = "black"

p1_x = canvas_width/2
p1_y = canvas_height
p1_colour = "green"

p2_x = canvas_width/2
p2_y = 0
p2_colour = "pink"

line_width = 5
line_length = 5

##### Functions:
# player 1 controls
def p1_move_N (event):
    global p1_y
    canvas.create_line (p1_x, p1_y, p1_x,(p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length

def p1_move_S (event):
    global p1_y
    canvas.create_line (p1_x, p1_y, p1_x,(p1_y+line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length

def p1_move_E (event):
    global p1_x
    canvas.create_line (p1_x, p1_y, (p1_x+line_length),p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length

def p1_move_W (event):
    global p1_x
    canvas.create_line (p1_x, p1_y, (p1_x-line_length),p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length
# player 2 controls
def p2_move_N (event):
    global p2_y
    canvas.create_line (p2_x, p2_y, p2_x,(p2_y-line_length), width=line_width, fill=p2_colour)
    p2_y = p2_y - line_length

def p2_move_S (event):
    global p2_y
    canvas.create_line (p2_x, p2_y, p2_x,(p2_y+line_length), width=line_width, fill=p2_colour)
    p2_y = p2_y + line_length

def p2_move_E (event):
    global p2_x
    canvas.create_line (p2_x, p2_y, (p2_x+line_length),p2_y, width=line_width, fill=p2_colour)
    p2_x = p2_x + line_length

def p2_move_W (event):
    global p2_x
    canvas.create_line (p2_x, p2_y, (p2_x-line_length),p2_y, width=line_width, fill=p2_colour)
    p2_x = p2_x - line_length


def erase_all (event):
    canvas.delete(ALL)
    
##### main:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width , highlightthickness=0)
canvas.pack()

# bind movement to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S )
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)

window.bind("w", p2_move_N)
window.bind("s", p2_move_S )
window.bind("a", p2_move_W)
window.bind("d", p2_move_E)
window.bind("u", erase_all)

window.mainloop()

