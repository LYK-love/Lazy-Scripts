# 用于扩展欧几里得算法的 Python 程序



def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
    gcd, x, y = extended_gcd(119, 120)
    print('The GCD is', gcd)
    print(f'x = {x}, y = {y}')