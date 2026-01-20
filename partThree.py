def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"charge £{charge:.2f}")



def pounds_to_float(d):
    output1 = d.removeprefix("£")
    output1_str = str(output1)
    output1_float = float(output1_str)
    return output1_float
def percent_to_float(p):
    output2 = float(p.removesuffix("%")) / 100
    return output2
main()
