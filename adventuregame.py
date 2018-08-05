from tkinter import *
import time
import random

root = Tk()
c = Canvas(root, width=1200, height=700, bg='black')
c.pack()

def run():

    intro_text = c.create_text(600,350, font=('arial', '50'), text="Press 'space' To Begin", fill='white')

    def start(event):
        nonlocal intro_text

        root.unbind('<space>')
        c.delete(intro_text)
        welcome = c.create_text(600,350, font=('arial', '18'), text="Welcome to the room, find your way out", fill='white')
        player = c.create_rectangle(590, 600, 610, 620, fill='white', outline='blue')
        c.update()
        time.sleep(1)
        c.delete(welcome)
        selection = c.create_text(600,350, font=('arial', '18'), text="Press '1', '2', or '3' for a room", fill='white')


        alive, right, left, up, down = True, False, False, False, False
        
       
        def right(event):
            nonlocal right
            right = True
            
        def right_s(event):
            nonlocal right
            right = False
            
        def left(event):
            nonlocal left
            left = True
            
        def left_s(event):
            nonlocal left
            left = False
            
        def up(event):
            nonlocal up
            up = True
            
        def up_s(event):
            nonlocal up
            up = False
            
        def down(event):
            nonlocal down
            down= True
            
        def down_s(event):
            nonlocal down
            down= False

        def room_1_a:
            print('go')
            c.delete(selection)
            door = c.create_rectangle(1150, 400, 1190, 440, fill='green', outline='blue')
            incorrect = c.create_rectangle(290, 620, 330, 660, fill='red', outline='blue')
            if right and c.coords(player)[2] <=1200 :
                c.move(player, 3, 0)
            if left and c.coords(player)[0] >=0 :
                c.move(player, -3, 0)
            if up and c.coords(player)[1] >=0 :
                c.move(player, 0, -3)
            if down and c.coords(player)[3] <=700 :
                c.move(player, 0, 3)
                c.update() 
            
        while room_2_a:
            door = c.create_rectangle(1150, 400, 1190, 440, fill='green', outline='blue')
            for i in range(5):
                incorrect = c.create_rectangle(290, i*20, 330, i*50, fill='red', outline='blue')
            
        while room_3_a:
            door = c.create_rectangle(1150, 400, 1190, 440, fill='green', outline='blue')
            incorrect = c.create_rectangle(290, 620, 330, 660, fill='red', outline='blue') 


        root.bind('<KeyPress-Right>', right)
        root.bind('<KeyRelease-Right>', right_s)
        root.bind('<KeyPress-Left>', left)
        root.bind('<KeyRelease-Left>', left_s)
        root.bind('<KeyPress-Up>', up)
        root.bind('<KeyRelease->', up_s)
        root.bind('<KeyPress-Down>', down)
        root.bind('<KeyRelease-Down>', down_s)
        root.bind('<1>', room_1)
        root.bind('<2>', room_2)
        root.bind('<3>', room_3)

        right(event)
        right_s(event)
        left(event)
        left_s(event)
        up(event)
        up_s(event)
        down(event)
        down_s(event)
        
        
    root.bind('<space>', start)



run()
root.mainloop()
