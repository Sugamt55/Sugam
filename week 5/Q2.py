'''Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument). '''

import sys

def report_args():
    num_args = len(sys.argv) - 1
    print(f"{num_args} argument(s) were provided.")

report_args()