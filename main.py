from ursina import*

app = Ursina()

def reset():
    ball.x = 0
    ball.z = -.2

def update():
    global dx, dz, scoreA, scoreB
    paddle_a.x = paddle_a.x + held_keys['right arrow']*time.dt
    paddle_a.x = paddle_a.x - held_keys['left arrow']*time.dt
    paddle_b.x = paddle_b.x + held_keys['d']*time.dt
    paddle_b.x = paddle_b.x - held_keys['a']*time.dt
    ball.x = ball.x + 0.02*dx
    ball.z = ball.z + 0.02*dz

    if abs(ball.x)>.4:
        dx= -dx

    if ball.z>.25:
        scoreB = scoreB+1
        print_on_screen(f'Player A: Player B = {scoreA}: {scoreB}', position=(-.85, .45), scale=2, duration= 2)
        reset()

    if ball.z<-.65:
        scoreA = scoreA+1
        print_on_screen(f'Player A: Player B = {scoreA}: {scoreB}', position=(-.85, .45), scale=2, duration=2)
        reset()

    #collitions
    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == paddle_a or hit_info.entity == paddle_b:
            dz =-dz

window.color = color.light_gray


#entities are below
table = Entity(model="cube", color = color.green,scale=(10, .5, 14), position= (0,0,0), texture="white_cube")
#paddles
paddle_a = Entity(parent=table, color= color.dark_gray, model="cube", scale=(.2,.03,.05), position=(0, 3.7, .22), collider="box")
paddle_b = duplicate(paddle_a, z=-.62)

Text(text= "Player A", scale=2, position=(-.1, .32) )
Text(text= "Player B", scale=2, position=(-.1, -.4) )

line = Entity(parent=table, model="quad", scale=(.88, .2, .1), position=(0, 3.5, -.2))
ball = Entity(parent=table, model= "sphere", color= color.azure, scale=.05, position=(0, 3.71, -.2), collider="box")

dx= .3
dz= .4
scoreA = 0
scoreB = 0

camera.position=(0, 15, -26)
camera.rotation_x= 30

app.run()
