Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 in (0,2,4,6)
False
>>> 5 not in (0,2,4,6)
True
>>> 6 in range(1,6)
False
>>> 6 in range (1,6,)
False
>>> x = range(1,6)
>>> if 3 in x
SyntaxError: invalid syntax
>>> if 3 in x:
	print("Contido")
	else:
		
SyntaxError: invalid syntax
>>> if 3 in x:
	print("Contido")
else:
	print("NAO contido")

	
Contido
>>> ((1 and 6) or (5 and 6)) in range (1,6)
False
>>> ((1 and 3) or (5 and 6)) in range (1,6)
True
>>> (10 or 2) in range (1,6)
False
>>> (2) in range (1,6)
True
>>> (2 or 10) in range (1,6)
True
>>> ((1 and 3) or (5 and 6)) in range(1,6)
True
>>> ((5 and 6) or (1 and 3)) in range (1,6)
False
>>> 
