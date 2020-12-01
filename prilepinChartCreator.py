import openpyxl, os, sys

#TODO: creates specific Prilepin Chart, and print it to the specific sheet on .xlsx file

def create_chart():
    pass


def one_rm_calc(weight, reps):
    return weight * reps * 0.300

def record_for_how_many():
    return input("How many reps on this?")

onerm = one_rm_calc(100, 4)

print(onerm)