#모듈을 모아놓은 집합
#import travel.thailand #맨뒤가 class나 함수를 import 직접 불가, module 가능
#trip_to = travel.thailand.ThailandPackage()
#trip_to.detail()

#from travel.thailand import ThailandPackage # class 설정 가능할 경우는 from, import
#trip_to = ThailandPackage()
#trip_to.detail()

#from travel import vietnam
#trip_to =vietnam.VinetnamPackage()
#trip_to.detail()

from travel import *  # 공개 범위를 개발자가 설정 해주어야함. package에서 import로 공개되길 원하는 것과 안원하는것 설정 해줘야함 // __all__
#trip_to =vietnam.VinetnamPackage() # vietnam 정의 되지 않음
#trip_to = thailand.ThailandPackage()
#trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) #해당 파일이 어디 있는지
print(inspect.getfile(thailand))