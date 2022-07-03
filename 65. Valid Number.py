def isNumber(s: str) -> bool:
	if s=='':
		return False
	s= s.strip().lower()
	
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
	if (isDec(li3[0]) or isInt(li3[0])) and (isInt(li3[1])):
		return True	
	return False
	
def isInt( s):
	if s=='' :
		return False
	if len(s.split('.'))>1:
		return False
	if (s[0]== '+' or s[0] == '-'):
		s= s[1:len(s)]
	if ('+' in s) or ('-' in s):
		return False
	for ch in s:
		if ch not in '0987654321':
			return False
	return True
	

def isDec(s):
	if s== '.':
		return False
	if len(s)==0:
		return False
	if s[0]=='+' or s[0]=='-':
		s= s[1:len(s)]
	if ('+' in s) or ('-' in s):
		return False
	
	li2= s.split('.')
	if len(li2)>2:
		return False
	if len(li2) == 1: #123
		if isInt(li2[0]):
			return True
		else:
			return False
		
	if len(li2)==2: #12.2, .12, 12.
		if (isInt(li2[0]) or isInt(li2[1])):
			return True
		else:
			return False
	
	return True
print(isDec('-1.'), isInt('-1.'),)
print(isDec('-.1'), isInt('-.1'),)
print(isDec('-.1'), isInt('1'),)

inp= ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789","abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for i in inp:
	print(isNumber(i))
