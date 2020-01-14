from direction import *

class Action():
    def execute(o, collidables):
        pass

class Action_move():
    def execute(o, collidables):
        o.move(collidables)

class Action_turn_right():
    def execute(o, collidables):
        o.turn(Direction.RIGHT)

class Action_turn_left():
    def execute(o, collidables):
        o.turn(Direction.LEFT)
