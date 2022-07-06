class Tovar(object):
 def __init__(self):
  self.dia_ek1 = '24 inches'
  self.tp_mat = 'OLED'
  self.os = 'Android 10'
  self.ki_kam = '4'
  self.dia_ek2 = '18 inches'
  self.tp_pro = 'Intel i7'
 def print_abilities1(self):
  print(self.__class__.__name__)
  print('Діагональ екрана:', self.dia_ek1)
  print('Тип матриці:', self.tp_mat); print()
 def print_abilities2(self):
  print(self.__class__.__name__)
  print('Операційна система:', self.os)
  print('Кількість камер:', self.ki_kam); print()
 def print_abilities3(self):
  print(self.__class__.__name__)
  print('Діагональ екрана:', self.dia_ek2)
  print('Тип процесора:', self.tp_pro); print()

class Televisor(Tovar):
 def __init__(self):
  super().__init__()
  self.dia_ek1 = '24 inches'
  self.tp_mat = 'OLED'

class Telephon(Tovar):
 def __init__(self):
  super().__init__()
  self.os = 'Android 10'
  self.ki_kam = '4'

class Noytbyk(Tovar):
 def __init__(self):
  super().__init__()
  self.dia_ek2 = '18 inches'
  self.tp_pro = 'Intel i7'

def main():
 TV = Televisor()
 TV.print_abilities1()
 Smartphone = Telephon()
 Smartphone.print_abilities2()
 Notebook = Noytbyk()
 Notebook.print_abilities3()
if __name__ == '__main__': main()