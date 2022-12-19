num1 = int(input("enter first number"))

num2 = int(input("Enter Second Number"))

operand = input("Enter operand")
#
# if num1==45 and num2==3 and operand=='*':
#     print('555')
#     elif num1==56 and num2==9 and operand=='+':
#         print('77')
#         elif num1==56 and num2==6 and operand=='/':
#             print('4')
#         elif operand == '*':
#             print(num1 * num2)
# elif operand == '+':
# print(num1+num2)

if num1==45 and num2==3 and operand=='*':
    print("555")
elif num1==56 and num2==9 and operand =='+':
    print('77')
elif num1==56 and num2==6 and operand=='/':
    print('4')
elif operand =='+':
    print(num1+num2);
elif operand == '-':
    print (num1-num2)
elif operand == '*':
    print(num1 * num2)
elif operand == '/':
    print(num1/num2)
else:
    print('output wrong')
