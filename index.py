from tkinter import *
import random

x, y = 15, 15
direction = ''
posicion_x = 15
posicion_y = 15
posicion_food = (15, 15)
posicion_snake = [(75, 75)]
nueva_posicion = [(15, 15)]

#------- FUNCIONES -------

def coordenadas_snake():
    global direccion, posicion_snake, x, y, nueva_posicion

    if direction == 'up': # arriba
        y = y - 30
        nueva_posicion[0:] = [(x, y)]
        if y >= 495:
            y = 15
        elif y <= 0:
            y = 465
    elif direction == 'down':  # abajo
        y = y + 30
        nueva_posicion[0:] = [(x, y)]
        if y >= 495:
            y = 15
        elif y <= 0:
            y = 15    
    elif direction == 'left': # izquierda
        x = x - 30
        nueva_posicion[0:] = [(x, y)]
        if x >= 495:
            x = 0
        elif x <= 0:
            x = 465
    elif direction == 'right':  # derecha
        x = x + 30
        nueva_posicion[0:] = [(x, y)]
        if x >= 495:
            x = 15
        elif x <= 0:
            x = 15

    posicion_snake = nueva_posicion + posicion_snake[:-1]

    for parte, lugar in zip(canvas.find_withtag('snake'), posicion_snake):
        canvas.coords(parte, lugar)

def direccion(event):
    global direction

    if event == 'left':
        if direction != 'right':
            direction = event
    elif event == 'right':
        if direction != 'left':
            direction = event
    elif event == 'up':
        if direction != 'down':
            direction = event
    elif event == 'down':
        if direction != 'up':
            direction = event

def movimiento():
    global posicion_food, posicion_snake,nueva_posicion
    posiciones = [15, 45, 75, 105, 135, 165, 195, 225, 255, 285, 315, 345, 375, 405, 435, 465]

    coordenadas_snake()

    if posicion_food == posicion_snake[0]:
        n = len(posicion_snake)

        cantidad['text'] = f'Cantidad X : {n}'

        posicion_food = (random.choice(posiciones), random.choice(posiciones))
        posicion_snake.append(posicion_snake[-1])

        if posicion_food not in posicion_snake:
            canvas.coords(canvas.find_withtag("food"), posicion_food)

        canvas.create_text(*posicion_snake[-1], text= '▀', fill='green2', font = ('Arial',20), tag ='snake')

    if posicion_snake[-1] == nueva_posicion[0] and len(posicion_snake) >= 4:
        cruzar_snake()

    for i in posicion_snake:
        if len(posicion_snake) == 3:
            maximo_nivel()

    cantidad.after(500, movimiento)

def cruzar_snake():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text=f"Intentelo\n de Nuevo \n\n X", fill='red', font=('Arial', 20, 'bold'))

def maximo_nivel():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text=f"EXCELENTE\n\n °° FIN °°", fill='green2', font=('Game Over', 35 ,'bold'))

def salir ():
    root.destroy()

#--------------------------

root = Tk()
root.title('Juego Snake')
root.config(bg='black')
root.resizable(0, 0)

#--------------------------

frame_1 = Frame(root, bg='black')
frame_1.grid(row=0, column=0, padx=20, pady=10)
frame_2 = Frame(root)
frame_2.grid(row=1, column=0, padx=20, pady=10)

root.bind("<KeyPress-Up>", lambda event:direccion('up'))
root.bind("<KeyPress-Down>", lambda event:direccion('down'))
root.bind("<KeyPress-Left>", lambda event:direccion('left'))
root.bind("<KeyPress-Right>",  lambda event:direccion('right'))

canvas = Canvas(frame_2, bg='black', width=479, height=479)
canvas.pack()

for i in range(0, 460, 30):
    for j in range(0, 460, 30):
        canvas.create_rectangle(i, j, i + 30, j + 30, fill='gray10')


canvas.create_text(75, 75, text='X', fill='red2', font = ('Arial', 18), tag = 'food')

botonSalir = Button(frame_1, text='Salir', bg='orange', command = salir)
botonSalir.grid(row=0, column=0, padx=20)

botonIniciar = Button(frame_1, text='Iniciar', bg='aqua', command = movimiento)
botonIniciar.grid(row=0, column=1, padx=20)

cantidad = Label(frame_1, text='Cantidad X :', bg='black', fg = 'red', font=('Arial', 12, 'bold'))
cantidad.grid(row=0, column=2, padx=20)

root.mainloop()