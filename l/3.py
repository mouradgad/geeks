num_days = int(input("Enter Number of Days: "))
current_amount = 0.01
total_accumulated = 0
print("\nProject Two (02) : Magguilli Retirement Fund\n")
for day in range(1, num_days + 1):
    print(f"Day  {day:2}  Current Amount:         $ {current_amount:,.2f}")
    total_accumulated += current_amount
    print(f"Day  {day:2}  Current Accumulated:    $ {total_accumulated:,.2f}\n")
    current_amount *= 2
print(f"Final Value:                    $ {current_amount/2:,.2f}")
print(f"Total Accumulated:              $ {total_accumulated:,.2f}\n")
print("END: Project Two (02)")
