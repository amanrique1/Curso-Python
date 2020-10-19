def square(num):
    return num **2

square2=lambda num:num**2
print(square2(3))

def sum(num1,num2):
    return num1+num2

sum2=lambda num1,num2:num1+num2
print(sum2(3,4))

sumDob=lambda num,suma:num+suma(num,num)
print(sumDob(1,sum2))

sumDob2=lambda num,suma:num+suma(num,num)
print(sumDob(1,sum))

larger_num = lambda num1, num2: num1 if num1 > num2 else (num2 if num1 < num2 else 'They are equal')