"""
4-byte checksum for message

------------------------------------------------------------
It shows how weak checksum is thus it's incapable of being \\
    a cryptographic hash function

e.g.
"IOU100.99BOB"
and
"IOU900.19BOB"

both have the checksum: ['0xb2', '0xc1', '0xd2', '0xac']
Here we get a Hash Collision!
------------------------------------------------------------
"""

__author__ = "LYK-love"

COL_NUM = 4


def list2matrix(input_list, col_num):
    """
    convert list to a matrix with given col_num,
    NBL this means the length of the input_list is just multiples of col_num
    """
    mat = []
    while input_list != []:
        mat.append(input_list[:col_num])
        input_list = input_list[col_num:]
    return mat


def checksum(mat, row_num, col_num):
    """
    calculate the check sum of the given row_num * col_num matrix

    """
    res = []

    # 从最后一列开始加
    for col in range(col_num - 1, -1, -1):
        sum = 0
        for row in range(0, row_num):
            sum += mat[row][col]
        res.append(sum)

    # 结果反转
    res.reverse()
    return res


text = input("input = ") or "IOU100.99BOB"

if len(text) % COL_NUM is not 0:
    raise Exception(
        "the length of input text must be multiples of col_num, which is {}".format(
            COL_NUM
        )
    )
ascii_list = list(map(ord, list(text)))

mat = list2matrix(ascii_list, COL_NUM)
check_sum_list = checksum(mat, row_num=len(mat), col_num=COL_NUM)
hex_check_sum_list = list(map(hex, check_sum_list))
print(hex_check_sum_list)
