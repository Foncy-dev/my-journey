import mysql.connector
from mysql.connector import Error


print ('Did you do math today...')

class Math :
    def __init__(cal,num1, num2):
        cal.num1 = num1
        cal.num2 = num2

    def add(cal):
        return cal.num1 + cal.num2
    
    def subtract(cal):
        return cal.num1 - cal.num2
    
    def multiply(cal):
        return cal.num1 * cal.num2
    
    def divide(cal):
        if cal.num2 == 0:
            return "Error, division by zero is not allowed"
        return cal.num1 / cal.num2
        
    def perform_operation(cal,math_op, num1, num2, opchoose):
        if math_op == 1:
            return  f" The answer of your operation {opchoose} is {cal.add}"
        elif math_op == 2:
            return   f" The answer of your operation {opchoose} is {cal.subtract}"
        elif math_op == 3:
            return   f" The answer of your operation {opchoose} is {cal.multiply}"
        elif math_op == 4:
            return   f" The answer of your operation {opchoose} is {cal.divide}"
        else:
            return "Invalid choice.Please select a valid operation"
    
    

    def store_calculations(cal, opchoose,num1,num2,result):
        try:
            with mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'HustlerNATION21@',
                database = 'calculator_game'
            ) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO calculations (num1, num2, opchoose, result) VALUES (%s, %s, %s, %s)"
                    values = (num1, num2, opchoose, result)
                    cursor.execute(query, values)
                    connection.commit()
                    print("Record inserted successfully into table")

                
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
       

print("\n Choose your operation as follows:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))


opchoose = int(input("Choose your given operation (1/2/3/4): "))
    
math_op = Math(num1,num2)

result = math_op.perform_operation(opchoose,num1, num2, opchoose)



math_op.store_calculations(opchoose, num1, num2, result)
print(result)