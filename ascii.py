run_condition='True'
from colorama import Fore 
import time 
import sys 
import string 
import keyword
def error_msg(txt):
    for chars in txt:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{Fore.RED}{chars}')
    else:
        reset_to_default_color=Fore.RESET 
        print(f'\n{reset_to_default_color}')
        
run_condition='True'
while bool(run_condition):
    identifier=str(input('identifier:'))
    def check_if_valid_identifier(sample_identifier):
        check_if_keyword=keyword.iskeyword(sample_identifier)
        check_digits=sample_identifier[0].isdigit()
        maximum_length=79
        if check_if_keyword==True:
            Invalid_identifer_msg_1='Error, your identifier cannot be a python keyword.'
            error_msg(txt=Invalid_identifer_msg_1)
        else:
            pass
        if check_digits==True:
          Invalid_identifier_msg_2='Your indentifier Should not start with any numeric values'
          error_msg(txt=Invalid_identifier_msg_2)
        else:
          pass 
        if len(sample_identifier)>maximum_length:
          Invalid_identifier_msg_3='Your identifier cannot exceed 79 characters'
          error_msg(Invalid_identifier_msg_3)
        else:
          pass
          result=string.punctuation 
          special_characters=[]
          for chars in result:
            special_characters.append(chars)
          else:
            special_characters.pop(26)
            for char in  sample_identifier:
              if char in ''.join(special_characters):
                Invalid_identifier_msg_4='Your identifier cannot contain special characters'
                error_msg(txt=Invalid_identifier_msg_4)
                break 
              else:
                pass    
            else:
              if len(sample_identifier)<maximum_length and check_if_keyword==False and check_digits==False and char is not ''.join(special_characters):
                print('Valid Identifier')
                
    check_if_valid_identifier(sample_identifier=identifier)