

#inp = input("")
#while inp:
 #   print(eval(inp))
  #  inp = input()





def calculator(num1: int, num2: int, operator, exit=0):
    while True:
        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '*':
            print(num1 * num2)
        elif operator == '/':
            if not num2:
                print('haytarary 0 chi karogh linel')
            print(num1 / num2)
        print()
        for_exit = input('for close, write any: ')
        if not for_exit:
            calculator(int(input('number1: ')), int(input('number2: ')), input('operator: '))
        else:
            break
calculator(int(input('number1: ')), int(input('number2: ')), input('operator: '))