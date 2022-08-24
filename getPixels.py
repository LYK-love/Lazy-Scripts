#! python
# -*- coding: utf-8 -*-

'''
 a  pixel caculator
'''

__author__ = "LYK-love"
# if __name__ == "main":

print('''
      This is a pixel caculator, you should input your intended parameters, including:\
      \n
      DPI: default is 400 \n\
      image width: default is 8.268 in inch, which is the width of A4 \n\
      image height: default is the same value of width \n\
      '''
      )


DPI = int(input("DPI = ") or 400 )
print(DPI)

width = float( input("width = ")  or 8.268 )
print(width)

height = float( input("height = ") or width )
print(height)


pixels_in_X = ( DPI * width )
pixels_in_Y = ( DPI * height )

MPs = pixels_in_X* pixels_in_Y / 1000000
print( "Result Resolution is {0:.1f} MP".format(MPs)  )
