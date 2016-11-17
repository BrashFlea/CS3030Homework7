#!/usr/bin/env python3
import sys
from urllib.request import urlopen
import module1

def testModule1():
    url="http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv"
    values = module1.create_list(url)
    #def fetch_file(url):
        #values = []
    
        #with urlopen(url) as file:
            #for line in file:
                 #words = line.decode('utf-8').split(',')
                #for word in words:
                    #values.append(word)
    i=0
    j=0

    while i < (len(values)/9):
        if i > 0:
            j=9*i

        print("Reading Record #" + str(i + 1) + ":")
        print("Left dashboard switch (0 or 1):" + values[j])
        print("Right dashboard switch (0 or 1):" + values[j + 1])
        print("Child lock switch (0 or 1):" + values[j + 2])
        print("Master unlock switch (0 or 1):" + values[j + 3])
        print("Left inside handle (0 or 1):" + values[j + 4])
        print("Left outside handle (0 or 1):" + values[j + 5])
        print("Right inside handle (0 or 1):" + values[j + 6])
        print("Right outside handle (0 or 1):" + values[j + 7])
        print("Gear shift position (P, N, D, 1, 2, 3 or R):" + values[j + 8])
        
        if values[j + 8] == "P":
            print("Both doors open")
        else:
            print("Both doors stay closed")
        
        print("")
        i += 1

# Main function
def main():
   testModule1() 

if __name__ == "__main__":
    
    # Call main
    main()

    exit(0)

