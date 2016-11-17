#!/usr/bin/env python3
import sys
from urllib.request import urlopen

url="http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"

def create_list(url):
    values = []
    
    with urlopen(url) as file:
        for line in file:
            words = line.decode('utf-8').replace(" ", "").replace("\n", "").split(',')
            for word in words:
                if len(word) == 1:
                    values.append(word)
                if len(word) == 4:
                    values.append(word)
    #print(values)  
    #print(len(values))
    return values
    #print(values)
    
    #print("Reading Record 1:")
    #print("Left dashboard switch (0 or 1):" + values[11])
    #print("Right dashboard switch (0 or 1):" + values[12])
    #print("Child lock switch (0 or 1):" + values[13])
    #print("Master unlock switch (0 or 1):" + values[14])
    #print("Left inside handle (0 or 1):" + values[15])
    #print("Left outside handle (0 or 1):" + values[16])
    #print("Right inside handle (0 or 1):" + values[17])
    #print("Right outside handle (0 or 1):" + values[18])
    #print("Gear shift position (P, N, D, 1, 2, 3 or R):" + values[19])
    #if values[19] == " P\n":
    #    print("Both doors open")
    #else:
    #    print("Both doors stay closed")

# Main function
def main():
    create_list(url)

if __name__ == "__main__":
    # Call main
    main()
    #exit(0)

