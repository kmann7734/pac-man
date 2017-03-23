from gamelib import* 

game = Game(800,600,"Hoops Up!")

   
court = Image("images\\court.jpg",game)
court.resizeTo(800,600)

player1 = Image("images\\player1.png",game)
player1.setSpeed(4,60)
player1.resizeBy(-60)

while not game.over:
    game.processInput()

    
    court.draw()
    player1.move(True)

    game.update(60)
game.quit()

 
   
    


   




    


