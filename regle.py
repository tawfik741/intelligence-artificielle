class Regle:
	def __init__(self):
		self.conditions = dict()
		self.resultat = dict()
	
	def add_condition(self,variable_name,operator,value):
		if(not( variable_name in self.conditions)):
			self.conditions[variable_name] = [[value,operator]]
		else:
			self.conditions[variable_name].append([value,operator])
	
	def define_result(self,variable_name,value):
		self.result = dict()
		self.result[variable_name] = value
	
	def match_conditions_to_Faits(self,faits):
		for k in self.conditions:
			if( not k in faits):
				return False
		return True
	
	def compare(self,a,b,operator):
		if(operator == '<'):
			return a < b
		if(operator == '>'):
			return a > b
		if(operator == '<='):
			return a <= b
		if(operator == '>='):
			return a >= b
		if(operator in ['=','==']):
			return a == b
	
	def show_raw(self):
		print(self.conditions)
		print(self.resultat)




	def execute(self,facts):
		if(not self.match_conditions_to_faits(faits)):
			return 
		
		for k in self.conditions:
			for l in self.conditions[k]:
				if(not self.compare(faits[k],l[0],l[1])):
					return
		return self.resultat
