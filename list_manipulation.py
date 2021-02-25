# -*- coding: utf-8 -*-
"""

johnwoates
CPSC 223P-01
Thu Jan 28, 2021
joates@fullerton.edu

"""

import lists

sports_teams = [lists.football_teams, lists.baseball_teams, lists.basketball_teams]

newList = [w.replace('hot dogs','bratwurst') for w in lists.school_lunches]
print(newList)

for q, a in zip(lists.questions, lists.answers):
  print("What is your {} ? My {} is {}.".format(q,q,a))

NYlist = []
for q in range(len(sports_teams)):
  for x in range(len(sports_teams[q])):
    if 'New York' in sports_teams[q][x]:
      NYlist.append(sports_teams[q][x])
print(NYlist)
LAlist = []
for q in range(len(sports_teams)):
  for x in range(len(sports_teams[q])):
    if 'Los Angeles' in sports_teams[q][x]:
      LAlist.append(sports_teams[q][x])
print(LAlist)
# Print out all the school lunches on the menu, but substitute bratwurst 
# wherever you see hot dogs
# Use list comprehension. Just print the list directly so the output will
# include the brackets and quotations (['item 1', item 2' ... and so on])


# Use zip to iterate over two lists at the same time
# Print out questions and answers in a loop
# Format them: "What is your <question>? My <question> is <answer>."


# Manipulate the nested lists of sports teams to print all teams from New York
# and all teams from Los Angeles.  Just print the lists directly so the output will
# include the brackets and quotations (['team 1', team 2' ... and so on])
