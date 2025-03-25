import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power_modulo(A, B, C):
    result = 1
    A %= C

    while B > 0:
        if B % 2 == 1:
            result = (result * A) % C

        B //= 2
        A = (A * A) % C

    return result

print(power_modulo(A, B, C))