import math

def find_next_square(sq):
        return (math.sqrt(sq) + 1) ** 2 if sq % math.sqrt(sq) == 0 else -1