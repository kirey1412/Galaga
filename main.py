import pgzrun, random

TITLE="Ship Shooting"
WIDTH=700
HEIGHT=560

speed=5

bullets=[]
enemies=[]

score=0
ship=Actor("ship.png")
for i in range(7):
    enemy=Actor("bug.png")
    enemies.append(enemy)
    enemies[-1].x=100+80*i #to update recently added element
    enemies[-1].y=-100

ship.pos=(WIDTH/2, HEIGHT-50)

def draw():
    screen.clear()
    screen.fill("lightpink")
    ship.draw()
    for i in enemies:
        i.draw()
    screen.draw.text(str(score), (50,50), color="navy")
    for i in bullets:
        i.draw()
    

def update():
    global score
    if keyboard.left:
        ship.x-=speed
        if ship.x<50:
            ship.x=50
    elif keyboard.right:
        ship.x+=speed
        if ship.x>WIDTH-50:
            ship.x=WIDTH-50
    for i in enemies:
        i.y+=2
        if i.y>HEIGHT:
            i.y=-100
            i.x=random.randint(50,WIDTH-50)
        for c in bullets:
            if i.colliderect(c):
                enemies.remove(i)
                bullets.remove(c)
                score+=20
        
    for b in bullets:
        b.y-=5
        if b.y<0:
            bullets.remove(b)
    
    
def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

    

pgzrun.go()