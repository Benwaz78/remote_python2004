
class MyMathClass():

    def my_range(self, start, stop):
        start = int(input('Enter start numnber: '))
        stop = int(input('Enter stop numnber: '))
        total = 0
        for x in range(start, stop+1):
            total += x
        print(total)

    def smallest_number(self):
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        num3 = int(input('Enter number 3: '))
        if num1 < num2 and num1 < num3:
            print(f'{num1} is less than {num2} and {num3}')
        elif num2 < num1 and num2 < num3:
            print(f'{num2} is less than {num1} and {num3}')
        elif num3 < num1 and num3 < num2:
            print(f'{num3} is less than {num1} and {num2}')


    def my_average(self, my_list):
        total = 0
        for x in my_list:
            total += x
        average = total/len(my_list)
        print(average)

    def print_even_numbers(self, start, stop):
        for x in range(start, stop+1):
            if x % 2 == 0:
                print(x)
    
    



m1 = MyMathClass()
# m1.my_range(1, 20)
# m1.smallest_number()
my_list = [10, 20, 30, 40]
m1.my_average(my_list)



        
        


        
