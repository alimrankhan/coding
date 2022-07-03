def isNumber(s: str) -> bool:
	if s=='':
		return False
	s= s.strip().lower()
	if noE(s)>1:
		return False
	li= s.split('.')
	if len(li)>2:
		return False
	for ch in s:
		if ch not in '0123456789e+-.':
			return False
	li3= s.split('e')
	if len(li3)>2:
		return False
	if len(li3) == 1 and ((isDec(li3[0])) or (isInt(li3[0]))) :
		return True
	else :
		if (isDec(li3[0]) or isInt(li3[0])) and (isInt(li3[1])):
			return True
		else:
			return False
	
		
	return True
	
def isInt( s):
	if s=='' :
		return False
	if len(s.split('.'))>1:
		return False
	if s[0]== ('+' or '-'):
		s= s[1:len(s)]
	for ch in s:
		if ch not in '0987654321':
			return False
	return True
	

def isDec(s):
	if s[0]== ('+' or '-'):
		s= s[1:len(s)]
	li2= s.split('.')
	if len(li2)>2:
		return False
	for ch in li2:
		if not isInt(ch) and ch!='':
			return False
	return True

def noE(s):
	E=0
	for ch in s:
		if ch=='e':
			E+=1
	return E
print (isNumber('+6e-1'))
print (isNumber('-90E3'))
print (isNumber('-.9'))
print (isNumber('-123.456e789'))
print ('fal')
#print (isNumber('e3'))
