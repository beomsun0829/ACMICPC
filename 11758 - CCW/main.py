def main():
    p1x, p1y = map(float, input().split())
    p2x, p2y = map(float, input().split())
    p3x, p3y = map(float, input().split())

    r1 = [p2x - p1x, p2y - p1y]
    r2 = [p3x - p2x, p3y - p2y]

    dir = (r1[0] * r2[1] - r1[1] * r2[0])

    if dir > 0:
        print(1)

    elif dir == 0:
        print(0)

    else:
        print(-1)


main()
