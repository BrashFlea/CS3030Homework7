#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys

"""
This program takes user a zip code as input and prints it in postal barcode form
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
    #Python representation of a case statement
    #Invalid Input at the bottom is the default statement and will trigger when passed double digits
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
    Converts a zipcode into postal barcode format
    Splits the zipcode and loops through it using printDigit() to convert the number
        Args:
            zipCode
        Returns:
            Prints zipCode in Barcode format
            : denotes half bars
            | denotes full bars
            Note: Adds | to beginning and ending as well as check digit
    """
    #Create a list that will represent the barcode and add the leading guard
    barcode = ["|",]
    #Break the zipcode apart into a list of values
    digits = [int(i) for i in str(zipCode)]
    #Convert each digit into the barcode representation
    for d in digits:
        barcode.append(printDigit(d))
    #Handle the checkdigit and convert it as well
    checkDigit = sum(digits) % 10
    if checkDigit %10 != 0:
        checkDigit = printDigit(10 - checkDigit)
    else:
        checkDigit = printDigit(checkDigit)
    #Create an empty string and add all the elements from the barcode list, the check digit, and the trailing guard
    #Note: sep = "" strips the spaces from the print statement
    print("".join(str(x) for x in barcode),checkDigit,"|",sep="")


# Main function
def main(zipcode):
    printBarCode(zipcode)
    return


if __name__ == "__main__":
    # Call Main
    main(sys.argv[1])
    exit(0)

