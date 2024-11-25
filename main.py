import os
import parseJson


"""
Loop through the test files (Valid and Invalid JSON) for parsing.
"""
def parser():
    for root, dirs, files in os.walk("tests"): #loop through files in directories and subdirectories
        for file in files:
            parseJson(file)


if __name__ == "__main__":
    parser()