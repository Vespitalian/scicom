def single_tax(pay):
    tax = 0
    if pay > 415050:
        tax += (pay - 415050) * .396
        pay = 415050
    if pay > 413350:
        tax += (pay - 413350) * .35
        pay = 413350
    if pay > 190150:
        tax += (pay - 190150) * .33
        pay = 190150
    if pay > 91150:
        tax += (pay - 91150) * .28
        pay = 91150
    if pay > 37650:
        tax += (pay - 37650) * .25
        pay = 37650
    if pay > 9275:
        tax += (pay - 9275) * .15
        pay = 9275
    return tax + pay * .1
