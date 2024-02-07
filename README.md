# Task-Prioritizer

Give your tasks a fixed priority with this tool.
Calculates a task priority by its urgency, impact and effort.

It also gives you advice what to do with your tasks.

# Usage

```
poetry install
poetry run python src/main.py
```

starts the script.

# Guide

There are three factors that determine the priority of your task:
URGENCY, IMPACT and EFFORT.

## URGENCY

If the deadline is today, the URGENCY should be HIGH.

If the deadline is this week, the URGENCY should be MEDIUM.

If the deadline is further away, the URGENCY should be LOW.

## IMPACT

If the task really changes things, the IMPACT should be HIGH.

If it is a routine task or nothing special, the IMPACT should be NORMAL.

For trivial tasks, the IMPACT should be LOW.

## EFFORT

If the estimated time is higher than 40h, EFFORT should be HIGH.

If the estimated time is around a day, EFFORT should be MEDIUM.

If the estimated time is lower than a day, EFFORT should be LOW.
