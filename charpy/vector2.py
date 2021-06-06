from __future__ import annotations
import math
class Vector2():

    def __init__(self, x: int|float, y: int|float):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def clone(self) -> Vector2:
        """Returns a new copy of the Vector2"""
        return Vector2(self.x, self.y)

    
    def add(self, other: Vector2) -> Vector2:
        """Returns a new Vector2 of this + other"""
        return Vector2(x=self.x + other.x, y=self.y + other.y)


    def subtract(self, other: Vector2) -> Vector2:
        """Returns a new Vector2 of this - other"""
        return Vector2(x=self.x - other.x, y=self.y - other.y)

    
    def scale(self, scale: int|float) -> Vector2:
        """Returns a new Vector2 with each axis * scale"""
        return Vector2(x=self.x * scale, y=self.y * scale)


    def dot(self, other: Vector2) -> int|float:
        return (self.x * other.x) + (self.y * other.y)


    def magnitude(self) -> float:
        return math.sqrt(self.x*self.x + self.y*self.y)


    @staticmethod
    def zero() -> Vector2:
        return Vector2(x=0, y=0)


    def __str__(self):
        return f'({self.x},{self.y})'
