# addition -(+)
# print(2+2) #4

# print(-4 + 4)
# print(-4. + 8)
# 0
# 4.0

# subtraction - (-)
# print(7-4) #3

# print(-4 - 4)
# print(4. - 8)
# print(-1.1)

# -8
# -4.0
# -1.1

# Multiplication -(*)
# print(2 * 3)
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)

# 6
# 6.0
# 6.0
# 6.0

# Division
# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)

# 2.0
# 2.0
# 2.0
# 2.0

# Integer division (floor division)
# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)

# 2
# 2.0
# 2.0
# 2.0

# print(6 // 4)
# print(6. // 4)

# 1
# 1.0

# print(-6 // 4)
# print(6. // -4)

# -2
# -2.0

# Remainder (modulo)

# print(14 % 4) # 2
# print(12 % 4.5) # 3.0

# Exponetiation
# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
# print(2 ** 3)
# print(2 ** 3.)
# print(2. ** 3)
# print(2. ** 3.)

# 8
# 8.0
# 8.0
# 8.0

# Unary operator
# print(+2) # 2 

# Operators priorities - (**) - (+,-) Unary operators located next to the right of the power operator bind more strongly - (*,/,//,%) - (+,-)
# print(9 % 6 % 2) # 1

# the exponentiation operator uses right-sided binding.
# print(2 ** 2 ** 3) # 256

# print(-3 ** 2)
# print(-2 ** 3)
# print(-(3 ** 2))

# -9
# -8
# -9

# print(2 * 3 % 5) #1

# operators and parenthesis - subexpressions in parentheses are always calculated first.

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # 10.0

print((2 ** 4), (2 * 4.), (2 * 4)) # 16 8.0 8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # -0.5 0.5 0 -1 

print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # -2 2 512

# (==) - Equality operator, equal to
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# (!=) -Inequality operator, not equal to
var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

n = int(input("Enter a number: "))
print(n >= 100)


x = 5
y = 10
z = 8
 
print(x > y) #False
print(y > z) #True


x, y, z = 5, 10, 8
 
print(x > z) #False
print((y - 5) == x) #True


x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z) #True
print((y - 5) == x) #False







    
    






