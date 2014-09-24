Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
#2.18a
>>> flowers = 'rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley'
>>> flowers
('rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley')

#2.18b
>>> 'potato' in flowers
False

#2.18c
>>> thorny = flowers [0], flowers [1], flowers [2]
>>> thorny
('rose', 'bougainvillea', 'yucca')


#2.18d
>>> poisonous = [flowers[-1]]
>>> poisonous
['lilly of the valley']

#2.18e
>>> dangerous = [thorny + poisonous]
>>> dangerous
[['rose', 'bougainvillea', 'yucca', 'lilly of the valley']]


#2.19a
x = 0
y = 0
import math
math.sqrt(x**2 + y**2) <= 10
True

#2.19b
x = 10
y = 10
import math
math.sqrt (x**2 + y**2) <=10
False

#2.19c
x = 6
y = -6
import math
math.sqrt (x**2 + y**2) <=10
True

#2.19d
x = 7
y = -8
import math
math.sqrt (x**2 + y**2) <=10
False

#2.20a
degrees = 75
>>> radians = (math.pi*degrees)/180
>>> 16*math.sin(radians)
15.454813220625093

#2.20b
degrees = 0
>>> radians = (math.pi*degrees)/180
>>> 20*math.sin(radians)
0.0

#2.20c
degrees = 45
>>> radians = (math.pi*degrees)/180
>>> 24*math.sin(radians)
16.97056274847714

#2.20d
degrees = 80
>>> radians = (math.pi*degrees)/180
>>> 24*math.sin(radians)
23.63538607229299

#2.23
>>> lst = [0, 5, 10, 20, 25]
>>> lst.sort()
>>> lst[4] - lst[0]
25

#2.24a
>>> lst = [0, 5, 10]
>>> len(lst)//2
1

#2.24b
lst[1]
5

#2.24c
>>> lst.reverse()
>>> lst
[10, 5, 0]

#2.25a
 0 == (1 == 2)
True

#2.25b
 2 + (3 == 4)+5 == 7
True

#2.25c
 (1 < -1) == ( 3>4 )
True
