from file_parser import FileParser
from regle import Regle
class FaitManager:
	def __init__(self,filename):
		
		self.filepath=filename
		self.file_parser=FileParser(filename," et ")
	def read_faits (self):
		self.file_parser.read_faits()
	def read_regles (self):
		self.file_parser.read_regles()
	def get_faits(self):
		return self.file_parser.read_faits()
	def get_regles (self):
		return self.file_parser.read_regles()
	def test_value (self):
		regles=self.get_regles()
		faits=self.get_faits()
		print (faits)
		for r in regles :
			print (r)

if __name__=="__main__":
	filepath="files/méteorologies.txt"
	fm = FaitManager(filepath)
	fm.test_value()
