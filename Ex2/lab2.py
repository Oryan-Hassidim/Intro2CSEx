def min_max(x, y):
    if x < y: return x,y
    return y,x

def geom_prob(x1, y1, x2, y2, a, b):
    minY, maxY = min_max(y1, y2)
    if a == 0: return minY <= b and b <= maxY
    f = lambda x: a * x + b
    minX, maxX = min_max(x1, x2)
    if 0 < a:
        return maxY >= f(minX) and minY <= f(maxX)
    return minY <= f(minX) and maxY >= f(maxX)