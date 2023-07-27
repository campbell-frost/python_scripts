import turtle
import math
import random

# Global variables
width = 800
height = 600
round_counter = 1
enemies = []
bullets = []
kills = 0
round_ended = True

# Game functions
# Move character acording to mouse movement
def motion(event):
    global x
    global y
    x, y = event.x, event.y

    print('{}, {}'.format(x, y))

# Creates projectile from player going to the direction the player is facing
def fire(x, y):
    bullet = turtle.Turtle()
    bullet.hideturtle()
    bullet.shape('circle')
    bullet.color('yellow')
    bullet.penup()

    angle = math.atan2(y - falcon.ycor(), x - falcon.xcor())
    angle_degrees = math.degrees(angle)
    
    bullet.goto(falcon.xcor(), falcon.ycor())
    bullet.setheading(angle_degrees)
    bullet.showturtle()
    
    bullet.forward(10)
    bullets.append(bullet)
    
# Spawns enemy     
def spawn_enemy():
    enemy = turtle.Turtle()
    enemy.shape('turtle')
    enemy.color('blue')
    enemy.penup()

    enemy.goto(width / 2, random.randint(-height // 2, height // 2))
    enemies.append(enemy)

# Handels enemy death
def kill_enemy(enemy):
    global enemy_deaths
    enemy_deaths += 1
    enemy.hideturtle()
    enemy.killed = True    
    
# Moves bullet    
def move_bullet(bullet):
    bullet.forward(20)  

# Moves enemy 
def move_enemy(enemy):
    enemy.setx(enemy.xcor() - 5)  

# Checks if bullet collides with enemy
def is_collision(t1, t2):
    distance = t1.distance(t2)
    return distance < 20  

# Setup screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width, height)

# Create player
falcon = turtle.Turtle()
falcon.shape('turtle')
falcon.color('red')
falcon.shapesize(2)
falcon.penup()
x = 0
y = 0

# Call fire function on click
wn.listen()
wn.onscreenclick(fire)

# Setup kill counter
kill_counter = turtle.Turtle()
kill_counter.color('white')
kill_counter.penup()
kill_counter.hideturtle()
kill_counter.goto(-width / 2 + 50, height / 2 - 50)  # Adjust the position of the counter

# Setup round counter
round_counter_display = turtle.Turtle()
round_counter_display.color('white')
round_counter_display.penup()
round_counter_display.hideturtle()
round_counter_display.goto(-width / 2 + 50, height / 2 - 80)  # Adjust the position of the round counter

# Draw center boundary 
boundary = turtle.Turtle()
boundary.hideturtle()
boundary.color('red')
boundary.width(2)
boundary.penup()
boundary.goto(0, -height / 2)
boundary.pendown()
boundary.goto(0, height / 2)

# Main game loop
while True:
    falcon.goto(x - 1 / 2 * width, - (y - 1 / 2 * height))
    turtle.update()
    canvas = turtle.getcanvas()
    canvas.bind('<Motion>', motion)
    turtle.onscreenclick(fire)

    # Spawn enemies at the start of each round
    if len(enemies) == 0 and round_ended:
        for i in range(round_counter * 2):  
            spawn_enemy()

    round_ended = True  # Mark new round

    # Shoot bullet
    for bullet in bullets.copy():
        move_bullet(bullet)
        
        # Un-renderes bullet if it goes off the screen
        if abs(bullet.xcor()) > width / 2 or abs(bullet.ycor()) > height / 2:
            bullets.remove(bullet)
            bullet.hideturtle()

    # Move enemy
    for enemy in enemies.copy():
        move_enemy(enemy)

        # Check if bullet hits the enemy
        for bullet in bullets.copy():
            if is_collision(bullet, enemy):
                kills += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                enemy.hideturtle()
                bullet.hideturtle()

        # Loss check
        if enemy.xcor() < 0:
            print("You Loose!")
            turtle.bye()
            break

        # Reset round state to false
        if len(enemies) > 0:
            round_ended = False

    # Check if all enemies are killed in a round
    if round_ended:
        round_counter += 1
        for enemy in enemies.copy():
            enemy.hideturtle()
        enemies.clear()
        
    # Win Check    
    if round_counter >= 4:
        print("You Win!")
        turtle.bye()
        break

    # List current kills
    kill_counter.clear()
    kill_counter.write(f"Kills: {kills}", align='left', font=('Arial', 20, 'normal'))
    
    # List current round
    round_counter_display.clear()
    round_counter_display.write(f"Round: {round_counter}", align='left', font=('Arial', 20, 'normal'))

    # Updates window
    wn.update()