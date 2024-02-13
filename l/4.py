def format_currency(amount):
    if amount >= 1000:
        return "${:,.2f}".format(amount)
    else:
        return "${:.2f}".format(amount)


def main():
    print("Project Two (02) : Magguilli Retirement Fund\n")

    num_days = int(input("Enter Number of Days: "))

    current_amount = 0.01
    total_accumulated = 0.01
    print(f"Day  1  Current Amount:         0.01")
    print(f"Day  1  Current Accumulated:    0.01\n")
    for day in range(2, num_days + 1):
        current_amount *= 2
        total_accumulated += current_amount
        print(f"Day  {day:2}  Current Amount:         {format_currency(current_amount)}")
        print(f"Day  {day:2}  Current Accumulated:    {format_currency(total_accumulated)}\n")
        


    print(f"Final Value:                    {format_currency(current_amount)}")
    print(f"Total Accumulated:              {format_currency(total_accumulated)}\n")
    print("END: Project Two (02)")



main()
