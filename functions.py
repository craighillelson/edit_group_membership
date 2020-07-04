"""Functions."""

import csv
import functions
import pyinputplus as pyip
from collections import namedtuple


def print_return():
    """Print return."""
    print('\n')


def open_csv_populate_lst():
    """Open a csv and populate a list with its contents."""
    with open('csvs/members.csv') as f:
        lst = []
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            lst.append(row.member)

    return lst


def number_original_members(lst):
    """
    After importing a list of members, number them and populate a dictionary
    with each member's assigned number as the key and their name as the value.
    """
    dct = {}
    for i, member in enumerate(lst, 1):
        dct[i] = member
    return dct


def get_list_of_keys(dct):
    """Return a list comprised of the keys of a dictionary."""
    return list(dct.keys())


def output_options(dct):
    """Present user with options."""
    print_return()
    print('options')
    for k, v in dct.items():
        print(k, v)


def prompt_user(a):
    """Prompt user for members to remove."""
    lst = []
    while True:
        print_return()
        print(f'Enter the number of corresponding members you\'d like to skip '\
              f'(1 - {len(a)}) or enter nothing to stop')
        response = pyip.inputInt('> ', max=len(a), blank=True)
        if response == '':
            break
        lst = lst + [response]

    return lst


def output_remaining_members(dct, lst1):
    """
    Filter the list of original members, excluding the members the user chose to
    skip. Populate a list with the remaining members.
    """
    print_return()
    print('remaining members')
    lst2 = []
    for k, v in dct.items():
        if k not in lst1:
            print(v)
            lst2.append(v)
    return lst2
    print_return()


def update_user(update):
    """Output user update."""
    print(update)


def write_lst_to_csv(file, LST, HEADER):
    """Write list to csv. Update user that the csv has been exported
    successfully."""
    path = 'output/'
    path_file = path + file
    with open(path_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADER)
        for i in LST:
            out_csv.writerow([i])

    print(f'\n"{file}" exported successfully\n')
