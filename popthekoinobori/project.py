#Group Members: XiangYu Hong, Shining Liu
#Company Name: 
#Game Name: Pop the koinobori
#Objects: koinobori, needle
#Instruction & goals of the game: You gain points from clicking the koinobori
#with your mouse 1(Left click), and you lose the needle's durability if you
#miss clicked the koinobori. You win by reaching the score of 300, and you lose
#if the needle's durability reached to 0.
from gamelib import*

game = Game(700,500,"Pop the koinobori",20)
koi = Image("image\\koinobori.png",game)
koi.resizeTo(koi.width / 2, koi.height / 2)
koi.setSpeed(2,60)
needle = Image("image\\needle.png",game)
bk = Image("image\\sky.png",game)
bk.resizeTo(game.width, game.height)
needle.resizeBy(-80)
bk.draw()
game.drawText("Pop the koinobori",195,130,Font(red,55,yellow))
game.drawText("Press [SPACE] to play",440,470,Font(red,35,yellow))
game.update(1)
game.wait(K_SPACE)

while not game.over:
        game.processInput()
        bk.draw()
        koi.move(True)
        needle.moveTo(mouse.x,mouse.y)

        if koi.collidedWith(mouse) and mouse.LeftButton:
                game.score += 10
                koi.speed += 1
                koi.resizeBy(-1)
        if bk.collidedWith(mouse) and mouse.LeftButton:
                needle.health-=1
        if needle.health<=0:
                game.drawText("You lose",300,250,Font(red,40,yellow))
                game.update(1)
                game.over = True
        if game.score>=300:
                game.drawText("You win",300,250,Font(red,40,yellow))
                game.update(1)
                game.over = True
        game.displayScore(0,0,Font(red,25,yellow))
        game.drawText("Needle Durability: " + str(needle.health),500,0,Font(red,25,yellow))
        game.update(60)
        
bk.draw()
game.drawText("Press [SPACE] to Exit",320,400,Font(red,50,yellow))
game.update(1)
game.wait(K_SPACE)
game.quit()
