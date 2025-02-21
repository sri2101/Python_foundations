# 1.Basic Printing:

#Print "Hello, World!"
#print("Hello, World!") #Hello, World!

#Having done that, use the print() function again, but this time print your first name.
#print("Sri") #Sri

#Remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
#print(Sri) #NameError: name 'Sri' is not defined

#Then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
#print"Sri" #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#Change double quotes to single quotes
#print'sri' #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#print('Sri') #Sri

#use multiple print() functions on the same line, and then on different lines. 
# print(print(print("Hello!")))
#Hello!
# None
# None

# print("Hello")
# print("Sri!")
#Hello
#Sri!

# print("The itsy bitsy spider climbed up the waterspout.")
# print("Down came the rain and washed the spider out.")

#The itsy bitsy spider climbed up the waterspout.
#Down came the rain and washed the spider out.

# print("The itsy bitsy spider climbed up the waterspout.")
# print()
# print("Down came the rain and washed the spider out.")

#The itsy bitsy spider climbed up the waterspout.

#Down came the rain and washed the spider out.

#Python escape and newline characters
# print("The itsy bitsy spider\nclimbed up the waterspout.")
# print()
# print("Down came the rain\nand washed the spider out.")

# The itsy bitsy spider
# climbed up the waterspout.

# Down came the rain
# and washed the spider out.

#Print multiple strings in a single print() call or multiple arguments.
#print("Hello,", "Welcome", "to","the","Coding","World!") #Hello, Welcome to the Coding World!

#Positional arguments
# print("My name is", "Python.")
# print("Monty Python.")

# My name is Python.
# Monty Python.

#Keyword arguments
# print("My name is", "Python.", end=" ")
# print("Monty Python.")

# My name is Python. Monty Python.

# print("My name is ", end="")
# print("Monty Python.")

# My name is Monty Python.

# seperator - keyword argument
# print("My", "name", "is", "Monty", "Python.", sep="-")

# My-name-is-Monty-Python.

# print("My", "name", "is", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*")

# My_name_is*Monty*Python.*

# print("Programming","Essentials","in",sep="***",end="...")
# print("Python")

# Programming***Essentials***in...Python

# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#     *
#    * *
#   *   *
#  *     *
# ***   ***
#   *   *
#   *   *
#   *****

# print("        *")
# print("       * *")
# print("      *   *")
# print("     *     *")
# print("    *       *")
# print("   *         *")
# print("  *           *")
# print(" *             *")
# print("******     ******")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *     *")
# print("     *******")

# print("        *        "*2)
# print("       * *       "*2)
# print("      *   *      "*2)
# print("     *     *     "*2)
# print("    *       *    "*2)
# print("   *         *   "*2)
# print("  *           *  "*2)
# print(" *             * "*2)
# print("******     ******"*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *     *     "*2)
# print("     *******     "*2)

# print("My\nname\nis\nBond.", end=" ")
# print("James Bond.")

# My
# name
# is
# Bond. James Bond.

# print(sep="&", "fish", "chips") # SyntaxError: positional argument follows keyword argument

# print("fish", "chips",sep="&") #fish&chips

# print('Greg\'s book.')
# print("'Greg's book.'")
# print('"Greg\'s book."')
# print("Greg\'s book.")
# print('"Greg's book."') # Line will raise SyntaxError, because the ' symbol in the Greg's book. string requires an escape character.

# SyntaxError: unterminated string literal (detected at line 152)

# print('"I\'m"\n""learning""\n"""Python"""')

# "I'm"
# ""learning""
# """Python"""


# 2.String Formatting:

#Use f-strings to format and print a message.
#mssg = "Hello,"
#print(f"{mssg}This is String Formatting using F-string")
#Print a formatted string using .format().
# print(f"{mssg}This is formatted String using .format()!!".format(mssg= "Hello,"))
# print("My name is {}, I'm {}".format("Sri",23))
# print("My name is {0}, I'm {1}".format("Sri",23))
# print("My name is {}, I'm {}".format("Sri",23,20,"po","52"))


