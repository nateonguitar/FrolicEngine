class Shape():
    
    facing_direction = "up"

    def __init__(self):
        self.facing_direction = "up"

    def spin(self):
        if self.facing_direction == "up":
            return get_facing_right()

        if self.facing_direction == "right":
            return get_facing_down()

        if self.facing_direction == "down": 
            return get_facing_left()

        if self.facing_direction == "left":
            return get_facing_up()

    def get_facing_up(self):
        raise NotImplementedError

    def get_facing_down(self):
        raise NotImplementedError

    def get_facing_left(self):
        raise NotImplementedError

    def get_facing_right(self):
        raise NotImplementedError

    
class Square(Shape):
    shape_array = [
        ['▣','▣'],
        ['▣','▣']
    ]

    def get_shape(self):
        return self.shape_array
        
    def get_facing_up(self):
        return self.shape_array
    
    def get_facing_down(self):
        return self.shape_array
    
    def get_facing_left(self):
        return self.shape_array

    def get_facing_right(self):
        return self.shape_array        