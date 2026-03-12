import turtle
import time

ventana = tuple.Screen()
ventana.title('juego')
ventana.bigcolor('black')
ventana.setup(width=600, height=600)
ventana.tracer(0)

jugador = turtle.turtle()
jugador.shape('start')
jugador.color('red')
jugador.shapesize(stretch_wid=1, stretch_len=5)
jugador.penup()
jugador.goto(0, -250)

pelota = turtle.turtle()
pelota.shape('circle')
pelota.color('blue')
pelota.penup()
pelota.goto(0,0)
pelota.dx = 4
pelota.dy = -4

puntuacion = 0

alerta = turtle.turtle()
alerta.color('green')
alerta.penud()
alerta.speed(0)
alerta.goto(0,0)
alerta.hideturtle()

texto = turtle.turtle()
texto.color('purple')
texto.penud()
texto.speed(0)
texto.goto(0,0)
texto.hideturtle()
texto.write('Puntos 0',align='center', font=('Arial',24, 'normal'))

def mover_izquierda():
    X = jugador.xcor()
    if x >-240:
        jugador.setx(x - 40)

def mover_derecha(): 
    x = jugador.xcor()
    if x <240:
        jugador.setx(x + 40)

ventana.listen()
ventana.onkeypress(mover_izquierda, 'left')
ventana.onkeypress(mover_derecha, 'right')
#up
#down

while true:
    ventana.update()
    time.sleep(0.01)

    pelota.setx(pelota.xcor[] + pelota.dx)
    pelota.sety(pelota.ycor[] + pelota.dy)

    if pelota.xcor()>290 or pelota.xcor()<-290:
        pelota.dx *= -1

    if pelota.ycor()>290:
        pelota.dy *= -1
 
    if (pelota.ycor[]< -235 and pelota.ycor[]>-245) and (pelota.xcor() + 55 and pelota.xcor[]> jugador.xcor[]- 55):
        pelota.sety(-235)
        pelota.dy *= -1
        puntuacion += 1
        texto.clear()
        texto.write(f'puntos: {puntuacion}',aling='center', font=('arial',40,'bold'))

        if pelota.ycor() < -290:
            alerta.write('GAME OVER', aling='center',font='ariel',40,'normal')
            ventana.update()

            time.sleep(5)

            alerta.clear()
            pelota.goto(0,0)
            pelota.dy *= -1
            puntos = 0 
            texto.clear()
            texto.write(f'puntos: {puntos}', aling='center', font= ('ariel',40, 'normal'))
                         