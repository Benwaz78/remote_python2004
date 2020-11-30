import math_class


class MathSubClass(math_class.MyMathClass):
    def times_table(self, multiplied_by, multiplyer=1, stop=12):
        while multiplyer <= stop:
            print(multiplied_by, ' X ', multiplyer,
                  ' = ', multiplied_by*multiplyer)
            multiplyer += 1

    def nested_times_table(self, start, stop):
        for x in range(start, stop+1):
            for y in range(start, stop+1):
                print(x, 'X', y, '=', x*y)



sub1 = MathSubClass()
# sub1.my_range(1, 20)
# sub1.smallest_number()
sub1.times_table(2)
