def ticket_price(age):
    if age <=3:
        return "FREE"
    elif age <=12:
        return "RS10"
    else:
        return "RS20"
age = int(input("Enter a passanger age:"))
ticket_price = ticket_price(age)
print(f"the ticket_price:{ticket_price}")
