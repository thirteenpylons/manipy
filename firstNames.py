"""
Find most common first names in a list of people.

This can be used after cleaning your data.

Example of cleaned data used: ./example/names.txt

Author: Christian M. Fulton
Date: 05.Aug.2021
"""


def main():
    """
    Exec
    """
    first_names()

    #impl opt exp data
    #ex = input("Would you like to export data?: ")


def first_names():
    """
    Count first names in dataset

    This function will sort and place names in dict('name': i, ..) 
    """
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

def top_n(names):
    """
    Provide top n list of names

    input(n)
    """
    pass

def export():
    """
    Option to export data
    """
    pass