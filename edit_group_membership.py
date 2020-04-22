"""
Import a csv, present user with options to skip.
Write the results to a csv.
"""

import functions

original_members = functions.open_csv_populate_lst()
original_members_numbered = functions.number_original_members(original_members)
nums = functions.get_list_of_keys(original_members_numbered)
functions.output_options(original_members_numbered)
members_to_skip = functions.prompt_user(nums)
remaining_members = \
functions.output_remaining_members(original_members_numbered, members_to_skip)
functions.write_lst_to_csv('remaining_members.csv', remaining_members, \
                           ['member'])
