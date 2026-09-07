def apply_discount(price, discount):
    if not (isinstance(price, (int,float))):
        return 'The price should be a number'
    
    if price <= 0:
        return 'The price should be greater than 0'
    
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    discount_price = ((price -(discount/100)*price))
    return discount_price 
    
calculated_price = apply_discount(200, 10)
print(calculated_price)

