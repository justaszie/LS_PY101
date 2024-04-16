# Asuming user inputs valid numbers
bill = float(input('What is the bill? '))
tip_rate = float(input('What is the tip percentage? '))

tip = bill * (tip_rate / 100)
total_bill = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total_bill:.2f}')