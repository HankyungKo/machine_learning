def main():
    r = input() # First line
    g = input() # Second line
    b = input() # Third line

    # change r, g, b into integer...

    print(rgb2hex(int(r), int(g), int(b)))


def rgb2hex(r, g, b):
    hex_color = "#"
    hex_color = hex_color + int2hex(r) + int2hex(g) + int2hex(b)
    
    return hex_color.upper()

def int2hex(a):
    result = format(a, 'x')
    if len(result) < 2:
        result = "0"+ result
    return result

if __name__ == "__main__":
    main()