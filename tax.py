taxes = [
    [9275, 0.1, 0.0],
    [37650, 0.15, -463.75],
    [91150, 0.25, -4228.75],
    [190150, 0.28, -6963.25],
    [413350, 0.33, -16470.75],
    [415051, 0.35, -24737.75],
]

def single_tax(income):
    # Check all brackets
    for tax in taxes:
        if income < tax[0]:
            return income * tax[1] + tax[2]
    # We calculated the top bracket earlier
    return income * .396 + -43830.05
