def single_tax(pay):
    tax_policy = [
        [415050, .396], 
        [413350, .35],
        [190150, .33],
        [91150, .28],
        [37650, .25],
        [9275, .15]
    ]
    tax = 0
    for bracket in tax_policy:
        if pay > bracket[0]:
            tax += (pay - bracket[0]) * bracket[1]
            pay = bracket[0]
    return tax + pay * .1
