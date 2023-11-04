run_condition='True'
from colorama import Fore
import time
import sys 
while bool(run_condition):
  try:
    userint=int(input('Whole_number:'))
    def check_if_even_or_odd(even):
     if userint%even==0:   
      print(f'{userint} is an even number')
     else:
       print(f'{userint} is an odd number')

    check_if_even_or_odd(2)
  except ValueError:
    error_msg='Error  the type of argument is correct but the value is improper'
    error_string=Fore.RED+f'{error_msg}'
    for n in error_string:
      sys.stdout.flush()
      time.sleep(0.1)
      sys.stdout.write(n)
    else:
     reset_to_default_color=Fore.RESET 
     print(f'{reset_to_default_color}\n')
