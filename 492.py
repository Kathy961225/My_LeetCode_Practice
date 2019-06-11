W = int(area**0.5)

    while W>=1 and area%W != 0:
        W = W-1
    return [area//W, W]