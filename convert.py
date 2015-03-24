# @naam: convert.py
# @wat: omrekenen van Celsius naar Fahrenheit .

def main():
    celsius = eval(input("Wat is de temperatuur in graden Celsius ? "))
    fahrenheit = 9/5 * celsius + 32
    print("De temperatuur in Fahrenheit is ", fahrenheit, " graden Fahrenheit. ")

main()
