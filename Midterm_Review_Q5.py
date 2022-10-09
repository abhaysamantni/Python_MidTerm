# In this question, I am providing you with the driver (main) code (file Q1Driver.py) below which
#will use the class Coin that you will be writing.
import coin
def main():
    # Create an object from the Coin class.
    my_coin = coin.Coin()
# Display the side of the coin that is facing up by default
#(without toss).
    print('This side is up:', my_coin.get_sideup())
    # Toss the coin 10 times.
    for i in range(10):
        print('I am tossing the coin...')
        my_coin.toss()
   # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())
# Call the main function.
main()


# <Write a Python program to create a class called Coin
# Write the initialization function (__init__) for the class Coin. The class should have
# a private attribute sideup which can be either one of the two values: “Heads” or
# “Tails”
# Write the method toss for the class which generates a random integer using the
# function random.randint(0, 1). It sets the attribute sideup equal to Heads if
# the random integer is equal to 0 and equal to Tails if the random integer is equal to 1.
# Write a method get_sideup that returns the current value of the private attribute
# sideup.

