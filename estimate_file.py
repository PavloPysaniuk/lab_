#Estimate_file.py
class estimatec(object): #оголошуємо клас
 def __init__(self, aa, mm, bb): #визначаємо функцію для створення екземпляру класу(self) 
  self.a_in = aa
  self.m_in = mm
  self.b_in = bb
 def do_estimate(self): #визначаємо функцію для розрахунків
  self.e_task = (self.a_in + 4*self.m_in+self.b_in) / 6
  self.sd_task = (self.b_in-self.a_in) / 6
  self.ci_project_1 = self.e_task-2*self.sd_task
  self.ci_project_2 = self.e_task+2*self.sd_task
  print('Projects 95% confidence interval: ',self.ci_project_1,' ... ',self.ci_project_2,' points')
