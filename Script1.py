#write a program to ask the user  their baggages 
totalAllowance=60
totalBaggage=0
while totalBaggage<totalAllowance:
    weight=int(input('Enter baggage weight: '))
    if weight<10:
        print('Bag may be brought on board')
    elif weight<=15:
        print('Bag may be carried')
    elif weight <=30:
        print('Baggage allowance of 15kg exceeded, extra charges will apply')
    else:
        print('Bag is too heavy!')
    totalBaggage=totalBaggage+weight
print('Thank you')
