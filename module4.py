#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Jonathan <jonathanmirabile@mail.weber.edu>
#
# Distributed under terms of the MIT license.
import sys
import urllib
import urllib.request
"""

"""

def fetch_url():
    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    resource = urllib.request.urlopen(url)
    content = resource.read().decode()
    print(content)

# Main function
def main():
    fetch_url()
    return


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)

