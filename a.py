class a:
	def b(self,q):
		print(1)
	
	def c(self,p):
		print(2)
		self.b(2)
		
obj= a()
obj.b(2)
obj.c(4)
