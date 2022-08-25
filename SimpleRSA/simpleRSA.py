#! python
# -*- coding: utf-8 -*-

import argparse


'''
RSA工具, 使用扩展欧几里得算法来计算d
'''

__author__ = "LYK-love"

def letter2numeric(letter):
    '''
    get numeric representation of a lower case letter, 
    a == 97, b == 98, ..., etc
    '''
    return ord(letter)

def numeric2letter(num):
    return chr(num)

def string2numeric(text):
    '''
    get numeric representation of a lower case text
    '''
    ascii_values = []
    for character in text:
        ascii_values.append(letter2numeric)
    return ascii_values
        
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True



def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def get_all_coprime(n):
    """Find all numbers that is co-prime to n in range n"""
    k=[]
    for i in range(n):
        if gcd(i,n)==1:
            k.append(i)
            i+=1
        else:
            i+=1
    return k

def get_one_coprime(n):
    """Find a number that is co-prime to a in range n"""
    co_primes = get_all_coprime(n)
    return co_primes[-1]

def compute_phi_pq(p,q):
    """compute Euler functuion, note this function only takes 2 parameters"""
    return (p-1) * (q-1)

def compute_phi_n(n):
    """compute Euler functuion, \phi(n)"""
    co_primes = get_all_coprime(n)
    
    return len(co_primes)


def extended_gcd(a, b):
    '''
    扩展欧几里得算法
    '''
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def get_one_mod_reverse_num(a,n):
    '''
    计算a相对于n的模反元素, 这里用了扩展欧几里得算法
    $ab \equiv 1 \mod n$
    '''
    
    gcd, x, y = extended_gcd(a,n)
    d = x
    while d <= 1:
        d += n
    return d
    


def make_positive(x, mode_num):
    '''
    模运算的结果x可能<=0, 该函数将x + n * mode_num, 直到x为正数 '''
    while x <= 0:
        x += mode_num
    return x

class Public_Key(object):
    def __init__(self, n, e):
        self.__n = n
        self.__e = e
    def get_public_key(self):
        return (self.__n,self.__e)
    
    def __str__(self):
        return ("n = {0}, e = {1}".format(self.__n, self.__e))
        
    
class Private_Key(object):
    def __init__(self, n, d):
        self.__n = n
        self.__d = d 
    def get_private_key(self):
            return (self.__n,self.__d)
        
    def __str__(self):
            return ("n = {0}, d = {1}".format(self.__n, self.__d))
            

def choose_prime(prime_name, default_value):
    '''
    @Deprecated
    let user choose q and p.
    NB: n = p*q should larger than any character which user inputs. \\
        So you had better make p and q may  as larger as possible.
    '''
    p = int(input("{0} = ".format(prime_name)) or default_value )
    if not is_prime(p) or p <= 17:
        raise Exception("{0} must be a large prime, your input is {1}".format(prime_name, p)  )
    return p
    
def generate_key(p,q):
    
    msg = "{} = {}"
    # # Choose two large prime numbers, $p$ and $q$
    # p = choose_prime("p", 5)
    # q = choose_prime("q", 7)
    
    # then compute $n = pq$
    n = p*q

    # Compute  $z = \phi(n) = (p - 1)(q - 1)$
    z = compute_phi_pq( p, q )
    print(msg.format("z", z))

    # 选择一个与 z 互质的数 e
    e = get_one_coprime(z)
    print(msg.format("e", e))

    # 计算 e 相对 z 的模反元素 d, 
    d = get_one_mod_reverse_num(e, z )
    print(msg.format("d", d))

    # 现在[n,e]就是public key, [n,d]就是private key
    public_key = Public_Key(n,e)
    private_key = Private_Key(n,d)  
    return public_key, private_key
  
        
def __encryption(m, public_key):
    '''
    接受数字m, 加密为数字c返回
    @m: int
    
    @return: c: int
    加密过程使用 $e$ , 计算密文 $c$ : 
    
    $c \equiv m^e \pmod n$
    '''
    # print("message in numeric: {}".format(m))
    

    
    n,e = public_key.get_public_key()
    
    # m < n
    if m >= n:
        raise Exception("p and q are too small to encrypte the character!")
    
    c = int( pow(m,e) % n )
    if c <= 0:
        c = make_positive(c,n)
        
    return c
        

     
    
def __decryption(c, private_key):
    '''
    @return: int
    
    
    解密过程使用$d$, 计算 $m$ :
    
    $m \equiv c^d \pmod n$
    '''

    n,d = private_key.get_private_key()
    m = int( pow(c,d) % n)
    if m <= 0:
        m = make_positive(m, n )
    return m

def encryption( plain_text, public_key):
    '''
    plain_text: str
    @return list(str)
    
    接受字符串, 将每个字符按ascii编码为数字, 然后加密为数字形式, 然后返回加密后的数字列表, 并转成同样的字符列表
    例如: “love”被ascii编码为['108', '111', '118', '101'], 加密为['49', '67', '40', '17']
    '''
    c_list = []
    for character in plain_text:
        m = letter2numeric(character)
        c = __encryption(m, public_key)
        c_list.append( c )
        
    cypher_text_list =  list(map(str, c_list))
    return cypher_text_list

def decryption( cypher_text_list, private_key):
    '''
    cypher_text_list: list(str)
    @return str
    
    接受加密后的字符列表,将每个字符转成数字, 解密成数字, 再解ascii编码成字符, 拼接起来形成明文字符串
    
    比如, ['12', '84', '27', '107']被转为[12,84,27, 107], 解密为[108,111,118,101], \\
    解ascii编码为['l','o','v','e'], 最后返回"love"
    '''
    
    m_list = []
    def numstr2num(numstr):
        return int(numstr)
    
    for cypher_text in cypher_text_list:
        c = numstr2num(cypher_text) # "49"变成49
        
        m = __decryption(c,private_key)# 49(密文) ->‘l’的ascii编码(也就是明文) == 108
        m_list.append( m )
    plain_text_list = list(map(numeric2letter, m_list)) # ['l', 'o', 'v', 'e']的数字形式 -> ['l', 'o', 'v', 'e']
    
    return ''.join(plain_text_list) # ['l', 'o', 'v', 'e'] -> 'love'
        

def parse_args():
    parser = argparse.ArgumentParser(description="a simple implementation of RSA ")
    group = parser.add_mutually_exclusive_group()  # 在参数对象中添加互斥组
    
    group.add_argument("-G","--generate", action="store_true", help="Generate RSA public and private keys" )
    group.add_argument("-E", "--encrypt", action="store_true", help="encrypt message using generated public key" )
    group.add_argument("-D", "--decrypt", action="store_true", help="decrypt message using generated private key" )
    
    parser.add_argument("--p", help="p", type=int)
    parser.add_argument("--q", help="q", type=int)
    parser.add_argument("--n", help="n", type=int)
    parser.add_argument("--e", help="e", type=int)
    parser.add_argument("--d", help="d", type=int)
    parser.add_argument("--plain_text", help="plain_text", type=str)
    parser.add_argument("--cypher_text", help="cypher_text", type=str, nargs='+' )
    
    args = parser.parse_args()
    return args

def main():
    # public_key, private_key = generate_key()
 
    args = parse_args()
    
    done_msg = "{0}: {1}"
    if args.generate:
        print("Generating keys...")
        # Choose two large prime numbers, $p$ and $q$
        p = args.p
        q = args.q
        
        def check_prime(prime_name, p):
            '''
            let user choose q and p.
            NB: n = p*q should larger than any character which user inputs. \\
            So you had better make p and q may  as larger as possible.
            '''
            print("{} = {}".format(prime_name, p))     
            if not is_prime(p) or p <= 17:
                raise Exception("{0} must be a large prime, your input is {1}".format(prime_name, p)  )
        
        check_prime("p",p)
        check_prime("q",q)
        
        public_key, private_key = generate_key(p,q)
        print(done_msg.format("public_key",public_key))
        print(done_msg.format("private_key",private_key))

    if args.encrypt:
        print("Encrypting...")
        

        public_key = Public_Key( args.n, args.e )
        plain_text = args.plain_text
        cypher_text = encryption(plain_text,public_key)      
        print( done_msg.format("cypher_text", cypher_text))
    
    if args.decrypt:
        print("Decrypting...")
        
        private_key = Private_Key( args.n, args.d )
        cypher_text = args.cypher_text
        print( done_msg.format("input cypher_text", cypher_text))
        
        plain_text = decryption( cypher_text, private_key )
        
        print( done_msg.format("plain_text", plain_text))
        
        
        
    
if __name__ == "__main__":
    main()










    
    


