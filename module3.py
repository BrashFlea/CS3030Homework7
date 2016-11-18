#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys

"""
This program takes user a zip code as input and prints it in bar code form
    Args:
        Zipcode
    Returns:
        Barcode representation of zipcode
        : denotes half bars
        | denotes full bars
"""


def printDigit(d):
    """
    Converts a single digit into a barcode representation
        Args:
            d = digit
        Returns:
            Barcode representation of digit
            : denotes half bars
            | denotes full bars
    """
    value = {
            1: ":::||",
            2: "::|:|",
            3: "::||:",
            4: ":|::|",
            5: ":|:|:",
            6: ":||::",
            7: "|:::|",
            8: "|::|:",
            9: "|:|::",
            0: "||:::",
        }
    return value.get(d, "Invalid Input")

def printBarCode(zipCode):
    """
    Converts a zipcode into barcode format
    Splits the zipcode and loops through it using printDigit() to convert the number
        Args:
            zipCode
        Returns:
            Prints zipCode in Barcode format
            Note: Adds | to beginning and ending as well as Check Digit
    """
    barcode = []
    digits = [int(i) for i in str(zipCode)]
    for d in digits:
        barcode.append(printDigit(d))

    print("".join(str(x) for x in barcode))



# Main function
def main(zipcode):
    printBarCode(zipcode)
    return


if __name__ == "__main__":
    # Call Main
    main(sys.argv[1])
    exit(0)

