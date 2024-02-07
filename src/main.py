from enum import IntEnum
from typing import Tuple, List

import numpy as np


class Value(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


DEPTH = len(Value)

# Advice for this task:
effort_vs_impact = np.full((DEPTH, DEPTH), "", dtype=object)
effort_vs_impact[Value.HIGH][Value.HIGH] = "It is a major project."
effort_vs_impact[Value.HIGH][Value.LOW] = "It is a thankless task."
effort_vs_impact[Value.LOW][Value.HIGH] = "It is a quick rewarding task."
effort_vs_impact[Value.LOW][Value.LOW] = "It is a fill in task."

impact_vs_urgency = np.full((DEPTH, DEPTH), "", dtype=object)
impact_vs_urgency[Value.HIGH][Value.HIGH] = "Do it now!"
impact_vs_urgency[Value.HIGH][Value.LOW] = "Decide when to do it!"
impact_vs_urgency[Value.LOW][Value.HIGH] = "Delegate it away!"
impact_vs_urgency[Value.LOW][Value.LOW] = "Delete it!"

urgency_vs_effort = np.full((DEPTH, DEPTH), "", dtype=object)
urgency_vs_effort[Value.HIGH][Value.HIGH] = "You should better hurry up!"
urgency_vs_effort[Value.HIGH][Value.LOW] = "You should bring it to an end."
urgency_vs_effort[Value.LOW][Value.HIGH] = "You should make a plan for it."
urgency_vs_effort[Value.LOW][Value.LOW] = "You can delay it."


def print_guideline() -> None:
    print(
        """
    ===========================================================================
                                     GUIDELINE                               
    ===========================================================================
    URGENCY:
    If the deadline is today the URGENCY should be HIGH (3).
    If the deadline is this week the URGENCY should be MEDIUM (2).
    If the deadline is further away the URGENCY should be LOW (1).
    
    IMPACT:
    If the task really changes things the IMPACT should be HIGH (3).
    If it is a routine task or nothing special the IMPACT should be NORMAL (2).
    For trivial tasks the IMPACT should be LOW (1).
    
    EFFORT:
    If the estimated time is higher than 40h, EFFORT should be HIGH (3).
    If the estimated time is around a day, EFFORT should be MEDIUM (2).
    If the estimated time lower than a day, EFFORT should be LOW (1).
    """
    )


def print_allowed_values():
    print("Allowed input values:")
    for i in range(0, DEPTH):
        # Convert from 0-based machine-readable indexes to 1-based human-readable values
        print("{0} = {1}".format(i + 1, Value(i).name))
    print("")


def read_priorities() -> Tuple[Value, Value, Value]:
    print("Calculate a new task priority")
    print()
    # Convert from 1-based human-readable values to 0-based machine-readable indexes
    urgency = Value(int(input("Urgency: ")) - 1)
    impact = Value(int(input("Impact : ")) - 1)
    effort = Value(int(input("Effort : ")) - 1)
    return urgency, impact, effort


def calc_priority(urgency: Value, impact: Value, effort: Value) -> int:
    """
    The priority is the sum of the indexes + 1
    The further it is from its optimum(0,0,0), the lower is its priority.
    The scale goes from 1 to 7 (but actually from 0 to 6).
    (0,0,0) has prio = 0 + 0 + 0 (+ 1) = 1
    (1,1,1) has prio = 1 + 1 + 1 (+ 1) = 4
    (2,2,2) has prio = 2 + 2 + 2 (+ 1) = 7
       :param urgency: The urgency of the task
       :param impact: The impact of the task
       :param effort: The effort of the task
       :return: A single priority ranging from 1 (Highest) to 7 (Lowest)
    """
    # Fake index on our "3x3x3 matrix"
    multi_index = [(urgency, impact, effort)]
    # Dimensions of our flattened "3x3x3 matrix"
    dimensions = pow(DEPTH, DEPTH)
    # Index array of our flattened "3x3x3 matrix" to flat indices
    priority = np.ravel_multi_index(multi_index, dims=dimensions, mode="raise")
    # Sum up the list of indices and convert from 0-based index to human-readable priority
    return sum(priority) + 1


def print_priority(priority: int) -> None:
    print()
    print("==============================")
    print("The priority of the task is: {0}".format(priority))
    print("==============================")


def get_suggestions(urgency: Value, impact: Value, effort: Value) -> List[str]:
    return [
        suggestion
        for suggestion in [
            effort_vs_impact[effort][impact],
            impact_vs_urgency[urgency][impact],
            urgency_vs_effort[urgency][effort],
        ]
        if suggestion is not ""
    ]


def print_suggestions(urgency: Value, impact: Value, effort: Value):
    print(" ".join(get_suggestions(urgency, impact, effort)))


def main():
    print_guideline()
    print_allowed_values()
    while True:
        try:
            urgency, impact, effort = read_priorities()
            priority = calc_priority(urgency, impact, effort)

            print_priority(priority)
            print_suggestions(urgency, impact, effort)
        except ValueError:
            print("Invalid entered task priority. Please try again.")
        finally:
            print()


if __name__ == "__main__":
    main()
