def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())

    ccw = ax * by + bx * cy + cx * ay - (bx * ay + cx * by + ax * cy)

    if ccw == 0:
        print(0)

    elif ccw > 0:
        print(1)

    else:
        print(-1)


main()
