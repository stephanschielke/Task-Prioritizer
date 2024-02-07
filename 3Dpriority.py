from enum import IntEnum
from typing import Tuple

import numpy as np
from numpy import ndarray


class Values(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


depth = len(Values)

# Advice for this task:
effort_vs_impact = np.full((depth, depth), "", dtype=object)
effort_vs_impact[Values.HIGH][Values.HIGH] = "It is a major project."
effort_vs_impact[Values.HIGH][Values.LOW] = "It is a thankless task."
effort_vs_impact[Values.LOW][Values.HIGH] = "It is a quick rewarding task."
effort_vs_impact[Values.LOW][Values.LOW] = "It is a fill in task."

impact_vs_urgency = np.full((depth, depth), "", dtype=object)
impact_vs_urgency[Values.HIGH][Values.HIGH] = "Do it now!"
impact_vs_urgency[Values.HIGH][Values.LOW] = "Decide when to do it!"
impact_vs_urgency[Values.LOW][Values.HIGH] = "Delegate it away!"
impact_vs_urgency[Values.LOW][Values.LOW] = "Delete it!"

urgency_vs_effort = np.full((depth, depth), "", dtype=object)
urgency_vs_effort[Values.HIGH][Values.HIGH] = "You should better hurry up!"
urgency_vs_effort[Values.HIGH][Values.LOW] = "You should bring it to an end."
urgency_vs_effort[Values.LOW][Values.HIGH] = "You should make a plan for it."
urgency_vs_effort[Values.LOW][Values.LOW] = "You can delay it."


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
    for i in range(0, depth):
        # Convert from 0-based machine-readable indexes to 1-based human-readable priorities
        print("{0} = {1}".format(i + 1, Values(i).name))
    print("")


def read_priorities() -> Tuple[Values, Values, Values]:
    print("Calculate a new task priority")
    print()
    # Convert from 1-based human-readable priorities to 0-based machine-readable indexes
    urgency = Values(int(input("Urgency: ")) - 1)
    impact = Values(int(input("Impact : ")) - 1)
    effort = Values(int(input("Effort : ")) - 1)
    return urgency, impact, effort


def calc_priority(urgency: Values, impact: Values, effort: Values) -> int:
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
    priority_matrix: ndarray = np.zeros((depth, depth, depth), dtype=int) + 1
    flat_matrix = priority_matrix.flatten()
    multi_index = [(urgency, impact, effort)]
    priority = np.ravel_multi_index(multi_index, dims=flat_matrix.shape, mode="raise")
    return sum(priority) + 1


def print_priority(priority: int) -> None:
    print()
    print("==============================")
    print("The priority of the task is: {0}".format(priority))
    print("==============================")


def print_suggestions(urgency: Values, impact: Values, effort: Values):
    print(
        " ".join(
            [
                effort_vs_impact[effort][impact],
                impact_vs_urgency[urgency][impact],
                urgency_vs_effort[urgency][effort],
            ]
        )
    )


def main():
    print_guideline()
    print_allowed_values()
    while True:
        try:
            urgency, impact, effort = read_priorities()
            priority = calc_priority(urgency, impact, effort)

            print_priority(priority)
            print_suggestions(urgency, impact, effort)
        except ValueError as exc:
            print("Invalid entered task priority. Please try again.")
        finally:
            print()


if __name__ == "__main__":
    main()
