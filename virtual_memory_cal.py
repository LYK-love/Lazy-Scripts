

import math

def twopower(n):
    power = 0
    target = 1
    
    while target < n:
        target = target << 1
        power = power + 1
        
    return power

    
prompt = '''
virtual memory address = VPN( virtual page number ) + offset
physical memory address = PFN( page frame number ) + offset
'''
print(prompt)

virtual_memory_address_len = int( input("the length of virtual memory address: ") )
physical_memory_address_len = int( input("the length of physical memory address: ") )

page_size = int( input("pase size is (in Byte): ") )
offset_len = twopower(page_size)

print()

print("{0} is 2^{1}, so offset_len is {1}".format(page_size, offset_len))

VPN_len = virtual_memory_address_len - offset_len

PFN_len = physical_memory_address_len - offset_len


print( "the length of VPN( virtual page number ): {0}".format(VPN_len))
print( "the length of PFN( page frame number ): {0}".format(PFN_len))
print( "the length of offset: {0}".format(offset_len))
