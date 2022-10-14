from game import addScore 

def test_addScore():
    assert(addScore("rock", "rock") == 0)
    assert(addScore("rock", "paper") == 0)
    assert(addScore("rock", "scissor") == 1)
    
    assert(addScore("paper", "rock") == 1)
    assert(addScore("paper", "paper") == 0)
    assert(addScore("paper", "scissor") == 0)
    
    assert(addScore("scissor", "rock") == 0)
    assert(addScore("scissor", "paper") == 1)
    assert(addScore("scissor", "scissor") == 0)