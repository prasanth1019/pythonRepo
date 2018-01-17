class taxCalcu:

	def _init_(self, year, age, taxAmnt, incomeInt):
		self.year = year
		self.age = age
		self.taxAmnt = taxAmnt
		self.incomeInt = incomeInt

	
	def yearTax(self):
		taxFrYear = self.taxAmnt / self.incomeInt
		print("This year tax is {:taxFrYear}", {taxFrYear: taxFrYear})
