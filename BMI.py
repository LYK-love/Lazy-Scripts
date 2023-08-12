print( \
    '''
    偏瘦	<= 18.4
    正常	18.5 ~ 23.9
    过重	24.0 ~ 27.9
    肥胖	>= 28.0
    '''
      )
weight = float( input("Your weight is (in kg) = ") )
length = float( input("Your length is  is (in cm) = ") ) / 100

BMI = weight / (length ** 2 )
print("BMI: {0:.2f}".format(BMI))


