total_purchase = float (input ('Total purchase: ')) #122.00 or 24.90

student = input ('Are you student:  ')

tax = 0.05
discount = 0.20

if student == 'yes':
    discount_amount = total_purchase * discount
    discounted_total = total_purchase - discount_amount
    sales_tax = total_purchase * tax
    total = discounted_total + sales_tax
    print (f'Total: {total:.2f}')
else :
    discount_amount = 0
    sales_tax = total_purchase *tax
    total = total_purchase - discount_amount + sales_tax
    print(f'Total:{total:.2f} ')

