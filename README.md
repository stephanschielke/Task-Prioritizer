# Task-Prioritizer
Give your tasks a fixed priority with this tool.
Calculates a task priority by its urgence, impact and effort.
It also gives you advice what to do with your tasks.

# Requirements
Needs Python 3.4 or Python 2.7 with an backported [Enum package](https://pypi.python.org/pypi/enum34#downloads)

# Usage
`python 3Dpriority.py` starts the script.

# Guide
There are three factors which determine the priority of your task:
URGENCE, IMPACT and EFFORT.

## URGENCE
If the deadline is today the URGENCE should be HIGH.
If the deadline is this week the URGENCE should be MEDIUM.
If the deadline is further away the URGENCE should be LOW.

## IMPACT
If the task really changes things the IMPACT should be HIGH.
If it is a routine task or nothing special the IMPACT should be NORMAL.
For trivial tasks the IMPACT should be LOW.

## EFFORT
If the estimated time is higher than 40h, EFFORT should be HIGH.
If the estimated time is around a day, EFFORT should be MEDIUM.
If the estimated time lower than a day, EFFORT should be LOW.