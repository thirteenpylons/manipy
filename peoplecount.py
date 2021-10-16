"""
Find most common first names in a list of people.

Author: Christian M. Fulton
Date: 05.Aug.2021
"""


def main():
    file = input("Enter the filename: ")

    p = []
    with open(file, "r") as rfile:
        for line in rfile:
            fname = line.split(' ')[0].lower()
            if fname not in p:
                p.append(fname)
    p.sort()
    d = dict(zip(p, [0]*len(p))) # make p a dict with 0 values
    with open(file, "r") as rfile:
        for line in rfile:
            fname = line.split(' ')[0].lower()
            if fname in d:
                d[fname] += 1

    print(d)
