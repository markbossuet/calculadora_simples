def Welcome():
     print('''Welcome to my frist calculator
       ''')

def calculate():
     operation = input('''        
 Please Type in the math operation you would like to complete:
+ for addition
- for subbtraction
* for multiplication
/ for division 
** for power
'%' for modulo 
''')
      
     number_1 = int(input('please enter the first number: '))
     number_2 = int(input('please enter the second number: '))
     
     if operation == '+':
          print('{} + {} = ' .format(number_1, number_2))
          print(number_1 + number_2)
          
     elif operation == '-':
          print('{} - {} = ' .format(number_1, number_2))
          print(number_1 - number_2)
     
     elif operation == '*':
          print('{} * {} = ' .format(number_1, number_2))
          print(number_1 * number_2)
          
     elif operation == '/':
          print('{} / {} = ' .format(number_1, number_2))
          print (float(number_1 / number_2))
          
     else:
          print('you have not typed a valid operator, please run the program again.')
                    
def again ():
     calc_again = input('''
     Do you want to calculate again?
     Please type Y for Yes and N for no.                        
     ''')                        
     
     if calc_again .upper() == 'Y':
          calculate()
     
     elif calc_again .upper() == 'N':
          print('see you later.')
          
     while calc_again .upper() == 'Y':
          calculate()
     else: 
          again()

Welcome()       
calculate()
again()
