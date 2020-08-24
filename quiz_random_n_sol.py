#1
class Geeks: 
	def __init__(self, id): 
		self.id = id

manager = Geeks(100) 

manager.__dict__['life'] = 49

print manager.life + len(manager.__dict__)  # 15


#2 dictionary = {} 
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1

sum = 0
for k in dictionary: 
	sum += dictionary[k] 

print sum           # 4
 
