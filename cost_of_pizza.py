#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program calculates the cost of a pizza
#     with user input of diameter

import constants


def main():
    # this function calculates the subtotal and total of the pizza

    # input
    diameter = int(input("Enter the diameter for your preferred " +
                         "pizza (inch): "))

    # process
    subTotal = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = subTotal + (subTotal * constants.HST)

    # output
    print("")
    print("The total cost for a {0} inch pizza is: ${1:,.2f} "
          .format(diameter, total))


if __name__ == "__main__":
    main()
