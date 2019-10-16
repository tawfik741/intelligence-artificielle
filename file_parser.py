
from regle import Regle 

class FileParser:
	def __init__(self,filename,and_separator):
			self.faits={}
			self.regles={}
			self.filepath=filename
			self.and_char= and_separator
			self.then_char=" alors "

	def is_operator(self,char):
		if(char in ['=','==','<','>','<=','>=','!=']):
			return True
		return False

	def clean_parsed_data(self,data):
		result = []
		for x in data:
			if( not (x.strip() in ['','"'])):
				if(x[0]=='"'):
					x = x.strip()
					x = x[1:len(x)]
				if(x[-1]=='\n'):
					x = x[0:len(x)-1]  
				if(x[-1]=='"'):
					x = x.strip()
					x = x[0:len(x)-1]
				result.append(x.strip())
				
		return result

	def recover_lost_space(self,data):
		result =  []
		if(len(data)>3):
			left = ''
			right = ''
			rightSide = False
			for x in data:
				if(not rightSide and not self.is_operator(x)):
					left = left + ' ' + x
				elif(self.is_operator(x)):
					rightSide = True
					result.append(left.strip())
					result.append(x)
				else:
					right = right + ' ' + x
			result.append(right.strip())
			return result
		return data

	def condition_line_to_object(self,line):
		line = line[2:]
		line_to_array = line.split(self.then_char)
		conditions = line_to_array[0].split(self.and_char)
		
		#print (conditions)
		result = line_to_array[1].split(' ')
		for i in range(0,len(conditions)):
			conditions[i] = self.recover_lost_space(self.clean_parsed_data(conditions[i].split(' ')))
		#print ("CONDITIONS")
		#print (conditions)
		result = self.recover_lost_space(self.clean_parsed_data(result))
		#print ("RESULTAT")
		#print (result)
		rule = Regle()
		for x in conditions:
			rule.add_condition(x[0],x[1],x[2])
		rule.define_result(result[0],result[2])
		return rule
	
	def facts_line_object(self,line):
		result = line.split(' ')
		result = self.recover_lost_space(self.clean_parsed_data(result))

	def read_faits(self):
		f = open(self.filepath, 'r')
		faits = dict()
		for line in f:
			if (not line[0:2]=='si' and len(line)>1):
				split_result = self.recover_lost_space(self.clean_parsed_data(line.split(' ')))
				faits[split_result[0]] = split_result[2]
		#print(faits)
		return faits

	def read_regles(self):
		f = open(self.filepath, 'r')
		rules = []
		for line in f:
			if (line[0:2]=='si'):
		#		print(line)
				rules.append(self.condition_line_to_object(line))
		#	print("___________________")
		return rules

