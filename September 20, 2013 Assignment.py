#4.12
s = 'abcdefghijklmnopqrstuvwxyz'
s1 = s[1:4]
print (s1)
s2 = s[0:3]
print (s2)
s3 = s[3:-2]
print (s3)
s4 = s[-4:-1]
print (s4)
s5 = s[-4:]
print (s5)


#4.15
s = '10 20 30 40 50 60'
print(s.split(' '))
s = '10,20,30,40,50,60'
print(s.split(','))
s = '10&20&30&40&50&60'
print(s.split('&'))
s = '10 - 20 - 30 - 40 - 50 - 60'
print(s.split(' - '))


#4.18
s = '''It was the best of times, it was the worst of times; it was the age of wisdom, it was the age of foolishness; it was the epoch of belief, it was the epoch of incredulity; it was...'''

#4.18a
newS = s.replace(',',' ')
newS = s.replace('.',' ')
newS = s.replace(';',' ')

#4.18b
newS = s.strip()

#4.18c
newS = s.lower()

#4.18d
newS = s.count('it was')

#4.18e
newS = s.replace('was','is')

#4.18f
listS = s.split()


#4.22
def month(month):
	abr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	print (abr[month-1])

	
