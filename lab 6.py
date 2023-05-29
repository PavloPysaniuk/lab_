#Lab_6_check.py
from estimated import estimate_file #з папки estimated "взяти" файл estimate_file
a=1.0
b=1.0
m=1.0
a=float(input(" a ="))
m=float(input("  m ="))
b=float(input("   b = "))
es=estimate_file.estimatec(a, m, b) #створюємо екземпляр es класу estimatec (викликається функція __init__ з параметрами a, m, b)
es.do_estimate() #викликаємо функцію do_estimate
