

from audioop import avg


item_list = list(map( float ,input().split() ))

# def getR_A_and_R_H(MIPS_list):
    
def getR_A(item_list):
    '''
    @item_list: MIPS list
    '''
    return sum(item_list) / len(item_list)

def getR_H(item_list):
    list_len = len(item_list)
    
    divisor = 0.0
    
    for item in item_list:
        divisor += 1/item
        
    
    R_H = list_len / divisor
    return R_H

print( getR_A(item_list))
print( getR_H(item_list))



