import sys


def main():
    n, m = map(int, sys.stdin.readline().split())

    data = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp.insert(0, 0)
        data[i] = tmp

    for i in range(1, n+1):
        for j in range(1, m+1):
            sum[i][j] = data[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            for ii in range(i, min(i + 10, n + 1)):
                for jj in range(j, min(j + 10, m + 1)):
                    if sum[ii][jj] - sum[i-1][jj] - sum[ii][j-1] + sum[i - 1][j - 1] == 10:
                        ans += 1

    print(ans)


main()
