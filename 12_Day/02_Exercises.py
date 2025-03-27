import random
import string
#1.
def list_of_hexa_colors(n):
    hexa = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(n)]
    return hexa
print(list_of_hexa_colors(5))
#2.
def list_of_rgb_colors(n):
    rgb = [f'rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)}) ' for _ in range(n)]
    return rgb
print(list_of_rgb_colors(5))
#3.
def generate_colors(inp, n):
    if 'hex' in inp:
        return [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(n)]
    
    elif 'rgb' in inp:
        return [f'rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})' for _ in range(n)]
    
    else:
        return ["Invalid input! Use 'hex' or 'rgb'."]
    
print(generate_colors('rgb',5))

