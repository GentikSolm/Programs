from mpmath import mp
help = "DigPi asks user for a number, and then calculates that many digits of pi."
def main():
    mp.dps = int(input("How many digits do you want to calculate?\n-> "))
    print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)
