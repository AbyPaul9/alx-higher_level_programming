#!/usr/bin/python3
""" append_after module """


def append_after(prmFileName="", prmSearch="", prmReplace=""):
    """
        Function to add string after a specific string
        Args:
            prmSearch: string to identify
            prmReplace: string to add
    """
    new = ""

    with open(prmFileName, 'r') as file:
        for line in file:
            new += line
            if prmSearch in line:
                new += prmReplace

    with open(prmFileName, 'w') as file:
        file.write(new)
