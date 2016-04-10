# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    """Print Hello World."""

    print "Hello World"

# print_hello_world()


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def greet(name):
    """Print Hi name."""

    print "Hi", name

# greet("Kathy")


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def product(x, y):
    """Get the product of two integers."""

    print x * y

# product(x=2, y=3)


# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def string_repeat(string, integer):
    """Print string n times."""

    print string * integer

# string_repeat(string="Hello", integer=5)


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def higher_or_lower(integer):
    """Print if integer >, <, or = to zero."""

    if integer > 0:
        print "Higher than 0"

    elif integer < 0:
        print "Lower than 0"

    else:
        print "Zero"

# higher_or_lower(0)
# higher_or_lower(1)
# higher_or_lower(-1)


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_3(integer):
    """Return True or False if integer is evenly divisible by 3.

    Integer is evenly divisible by 3 if integer % 3 has a remainder of 0.
    Otherwise, it is not divisible by 3.
    """

    if integer % 3 == 0:
        return True

    else:
        return False

# divisible_by_3(2)
# divisible_by_3(3)


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def num_spaces(string):
    """Returns number of spaces in string."""

    return string.count(' ')

# num_spaces("food")
# num_spaces("I love to eat food.")


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def meal_cost_tip_calculator(price, tip=0.15):
    """Get total meal cost with tip.

    Total meal cost is price of meal + price of meal * tip. If no
    tip is passed, default tip is 15%.
    """

    total = price + (price * tip)

    return total

# meal_cost_tip_calculator(price=15, tip=0.20)
# meal_cost_tip_calculator(price=15)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def num_info(integer):
    """Get sign and parity of integer."""

    pos = "Positive"
    neg = "Negative"
    even = "Even"
    odd = "Odd"
    sign_parity_list = []

    if integer >= 0:
        sign_parity_list.append(pos)

    else:
        sign_parity_list.append(neg)

    if integer % 2 == 0 and integer != 0:
        sign_parity_list.append(even)

    elif integer % 2 != 0 and integer != 0:
        sign_parity_list.append(odd)

    else:
        sign_parity_list.append("Neither 'even' or 'odd'")  # This condition is only true for integer 0.


    sign, parity = sign_parity_list  # Unpack list onto two variables.

    print sign, parity
    return sign_parity_list


# num_info(2)
# num_info(3)
# num_info(-2)
# num_info(-3)
# num_info(0)


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    price as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def cost_with_tax(state_abbrev, price, tax=0.05):
    """Get total cost including tax.

    Total cost is price + price * tax. Tax for any state is 5%, except for 'CA',
    where tax is 7%.
    """
    price = float(price)

    if state_abbrev == 'CA':
        tax = 0.07

    total = price + price * tax

    return total


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
