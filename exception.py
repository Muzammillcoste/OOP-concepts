try:
    amount=int(input('Enter amount to be shared: '))
    sharers=int(input('Enter number of sharers: '))
    print('Each one will get Rs. ',amount/sharers)
except ValueError as e:
    print('Please enter value in digit:',type(e),e)
except ZeroDivisionError as e:
    print('Problem with value:',type(e),e)
except:
    print('Cannot identify the problem')
print('Have a blessed day')

#user define 
class mini_age(Exception):
    pass
try:
    age=int(input('Enter age: '))
    if age>16:
        print('eligible')
    else:
        raise mini_age()
except ValueError as e:
    print('problem with value:',type(e),e)
except mini_age as m:
    print('not eligiable',type(m),m)
print('Have a nice day!')