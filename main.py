import os
import datetime

path = '.\\files'
data_now = datetime.datetime.now()

age = [11, 20, 18, 33, 14, 12]
print(list(filter(lambda age: age>=18, age)))
