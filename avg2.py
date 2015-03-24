# @naam: avg2.py
# @wat: bereken het gemiddelde van 2 getallen

def main():
    print("Dit programma berekent het gemiddelde van 2 getallen. ")

    score1, score2 = eval(input("Geef de twee getallen gescheiden door een comma : "))
    average = (score1 + score2) / 2

    print("Het gemiddelde van de scores is : ", average)

main()
