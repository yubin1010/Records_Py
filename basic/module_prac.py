#import theater_module
#theater_module.price(3)
#theater_module.price_morning(4)
#theater_module.prince_soldier(5)

#import theater_module as mv #모듈 이름을 축약
#mv.price(3)
#mv.price_morning(4)
#mv.prince_soldier(5)

#from theater_module import *
#price(3)
#price_morning(4)
#prince_soldier(5)

#from theater_module import price, price_morning, prince_soldier
# 특정 함수만
#price(5)
#price_morning(6)

#from theater_module import price, prince_soldier
#prince_soldier(5)
#price(4)

from theater_module import prince_soldier as price
price(5) #soldier의 내용을 price로 쓰는 것