rn = random(1,1300)
rm = random(1,700)
score = 0
points = 1
timer = 20000
s = second()
def setup():
    size(1500,750)
    noCursor()
    background(0,0,0)
def draw():
    global rn,rm,score,points,timer,s
    background(0,0,0)
    fill(0,200,200)
    circle(rn,rm,50)
    textSize(32)
    fill(255,255,255)
    text(score,100,100)
    text (timer,1400,100)
    text ("time left", 1250,100)
    timer -= s
    rect(mouseX, mouseY, -20,3)
    rect(mouseX, mouseY, -3,20)
    rect(mouseX, mouseY, 20,3)
    rect(mouseX, mouseY, -3,-20)
    if rn - 20 <= mouseX and rn + 20 >= mouseX and rm - 20 <= mouseY and rm + 20 >= mouseY and mousePressed and (mouseButton == LEFT):
        rn = random(100,1300)
        rm = random(100,700)
        fill(0,200,200)
        circle(rn,rm,50)
        score += points
    if score == 10 and timer > 0:
        points = 0
        textSize(100)
        text ("GOOD JOB YOU WIN",300,375)
    if timer <= 0 and score <= 10:
        points = 0
        s = 0
        textSize (100)
        text("you lose",300,375)
