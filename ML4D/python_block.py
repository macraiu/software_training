import numpy as np
from itertools import count

class p:

    def __init__(self, color, legs):
        #class consturctor __init__()
        self.color = color
        self.legs = legs
    @staticmethod #decorator
    def create_data_structures():
        """
        data structure support: list, dictionary, set ,tuple \n
        Use: \n
        DICTIONARY: when you need a logical association betweeen a key:value pair.
        fast lookup for data based on key
        when data constantly modified (dictionary are mutable)\n
        LIST:  collection of data with order
        when you need a simple iterable collection that is modified frequently\n
        SET: if you need uniqueness for the elements\n
        TUPLES: when data cannot change
        """
        #list
        nums = [1,2,3,4,5,4,3,2,5,6,7,4,0,9]
        print(nums)
        empty_list = []
        things = ["string", 0, [1, 2, 3], 4.56]
        print(things)
        list_slice = nums[2:5]
        print(list_slice)
        print("slice with minus: ", nums[1:-1])
        
        #set
        set_ = {3,5,6}
        print(set_)
        set_.add(10)
        print(set_)
        first = {1,2,3,4,5,6}
        second = {4,5,6,7,8,9}
        print(first | second)
        print(first & second)
        print(first - second)
        print(second - first)
        print(first ^ second)

        #dic
        dic = {2:10, 3:45, 4:55}
        print(dic)

        #tuple : immutable list
        tup = ("spam", "eggs", "sausage")
        empty_tuple = ()

        ages = {"dave": 24, "mary": 42, "john": 58}
        print(ages["dave"])

        primary = {"red": [255,0,0], "green": [0,255,0], "blue": [0,0,255]}
        #add new element
        primary["yellow"] = [120,120,0]
        print(primary)

        for key, value in primary.items():
            print("key: {0}, value: {1}".format(key, value))
        empty_dic = {}
        print(primary.get("albania", "not in dictionary"))

    @staticmethod
    def list_comprehension():
        cubes = [i**3 for i in range(5)]
        print(cubes)
        evens = [n for n in range(10) if n%2 == 0 and n!= 0]
        print('evens', evens)

        """       try: 
                    evens = [2*i for i in range(10**100)]
                except MemoryError:
                    print("memory error")
                finally: 
                    print("in finally") 
        """
    @staticmethod
    def string_format():
        nums = [2,3,4]
        msg = "numbers {0} {1} {2}".format(nums[0], nums[1], nums[2])
        print(msg)
        a = "{x} {y}".format(y=10, x=100)
        print(a)
    
    @staticmethod
    def string_functions():
        print(", ".join(["spam", "eggs", "ham"]))
        print("hello me".replace("me", "world"))
        print("This is a sentence".startswith("This"))
        print("This is a sentence".endswith("nce"))
        print("this is a sentence".upper())
        print("this THIS is A SenteNCE".lower())
        print("this is a sentence".split(" "))
    
    @staticmethod
    def numeric_functions():
        print(min(1,2,3,4,5,6,7,8,9))
        print(max([4,5,6,7,4,3,2]))
        print(abs(-10))
        print(abs(42))
        print(sum([10,100,1000]))
        
    #@classmethod
    def list_functions():
        nums = [55,44,33,22,11]
        if all([i > 5 for i in nums]):
            print("all bigger than 5")
        if any([i % 2 == 0 for i in nums]):
            print("at least one even")
        for v in enumerate(nums):
            print(v)

    #@staticmethod
    def open_file():
        filename = input("enter filenam")
        with open(filename) as f:
            text = f.read

        #print(count_char(text, char))
        
    @staticmethod
    def two_d_grid():
        m = [[1,2,3], [4,5,6]]
        print(m[0][1])

    @staticmethod
    def s():
        str_ = "hello world"
        print(str_[3]) 

    @staticmethod
    def list_operation():
        nums = [1,2,3]
        print(nums + [4,5,6])
        print(nums*3)
        nums.append([3,66,102])
        print(nums)
        print(len(nums))
        nums.insert(2, 2)
        print(nums)
        print(nums.index(2))
        nums.pop(4)
        #nums.remove(2)
        print(nums.count(2))
        nums = [a for a in nums if a != 2]
        print(nums)
        nums.reverse()
        print(nums[::-1])
        print(min(nums))
        print(max(nums))
        numbers = list(range(10))
        range_num = list(range(3,8))
        print(range_num)
        print(list(range(3,8,2)))

    @staticmethod
    def exponent(a, pow):
        print(a**pow)
    
    @staticmethod
    def int_of_div(a, div):
        print(a//div)

    @staticmethod
    def in_print():
        print('Brian\'s  mother: he\'s not an angel')

    @staticmethod
    def take_user_input():
        print(input())

    @staticmethod
    def concatenate_string():
        name = input("Enter your name: ")
        print("hello : " + name)

    @staticmethod
    def in_op():
        word = ["spam", "deny", "almost"]
        print("spam" in word)
        print("egg" not in word)

    @staticmethod
    def try_except():
        """
        # exceptions : \n
        # ImportError, import fails \n
        # IndexError: list index out of range \n
        # NameError: uknown var used \n
        # SyntaxError: code not parsed properly \n
        # TypeError: function called on value of an inappropriate type \n
        # ValueError: function called on avalue of the correct type but with an inappropriate value \n
        # ZeroDivisionError: divided by zero \n
        # OSError: ?? \n
        """
        try:
            num1 = 7
            num2 = 0
            #raise ZeroDivisionError
            print(num1/num2)
            print("done calc")
        except ZeroDivisionError:
            print("error occured ZeroDivError")
            #raise
        except (ValueError, TypeError):
            print("value error or type error")
        except:
            print("all the other errors")
        finally:
            print("in finally try")

        # useful when dealing with user inputs

    def raise_assert():
        #a = input()
        #raise NameError("invalid  name")

        # Use assert at the beginning of function 
        temp = -10
        #assert (temp > 0), "Colder than zero deg"
        print("after assert")

    def lambda_func():
        print((lambda x: 2*x*x)(5))
        #they can also be assigned
        double = lambda x: x * 2
        print(double(7))

    def map_func():
        nums = [11, 13, 15, 122]
        print(list(map(lambda x: x + 5, nums)))
        print(list(filter(lambda x: x%2 == 0, nums)))

    def generator(range_):
        for a in range(range_):
            yield a
    
    def call_generator():
        """      for i in p.generator(10**100):
        print(i) """
        print(list(p.generator(100)))



p.create_data_structures()
p.exponent(5, 5)
p.int_of_div(10, 3)
p.in_print()
#p.take_user_input()
#p.concatenate_string()
p.two_d_grid()
p.s()
p.list_operation()
p.in_op()

operation = p.in_op()
print(operation)
# if no return in function python return automatically none type

p.try_except()
p.list_comprehension()
p.string_format()
p.string_functions()
p.numeric_functions()
p.list_functions()
#p.open_file()
p.lambda_func()
p.map_func()
p.call_generator()