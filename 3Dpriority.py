from enum import IntEnum


class Priorities(IntEnum):
    """
    # Axes with weight
    """

    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Axes(IntEnum):
    """
    # Axes with weight
    """

    URGENCY = 3
    IMPACT = 2
    EFFORT = 1


depths = len(list(Priorities))
# dimension = len(list(Axes))

# Define the priority matrix
matrix3D = [[[0 for k in range(depths)] for j in range(depths)] for i in range(depths)]

# The priority is the sum of the indexes + 1
# The further it is from its optimum(0,0,0), the lower is its priority.
# Scale goes from 1 to 7:
# (0,0,0) has prio = 0 + 0 + 0 + 1 = 1
# (1,1,1) has prio = 1 + 1 + 1 + 1 = 4
# (2,2,2) has prio = 2 + 2 + 2 + 1 = 7

for i in range(depths):  # urgency
    for j in range(depths):  # impact
        for k in range(depths):  # effort
            matrix3D[i][j][k] = i + j + k + 1
            # with weighted axes:
            # matrix[i][j][k] = i*Axes.URGENCY + j*Axes.EFFORT + k*Axes.IMPACT +1
# pprint.pprint(matrix3D)

# Advices for this task:
EffortVsImpact = [["" for _ in range(4)] for _ in range(4)]
EffortVsImpact[Priorities.HIGH][Priorities.HIGH] = "It is a major project."
EffortVsImpact[Priorities.HIGH][Priorities.LOW] = "It is a thankless task."
EffortVsImpact[Priorities.LOW][Priorities.HIGH] = "It is a quick rewarding task."
EffortVsImpact[Priorities.LOW][Priorities.LOW] = "It is a fill in task."

UrgentVsImpact = [["" for _ in range(4)] for _ in range(4)]
UrgentVsImpact[Priorities.HIGH][Priorities.HIGH] = "Do it now!"
UrgentVsImpact[Priorities.HIGH][Priorities.LOW] = "Delegate it away!"
UrgentVsImpact[Priorities.LOW][Priorities.HIGH] = "Decide when to do it!"
UrgentVsImpact[Priorities.LOW][Priorities.LOW] = "Delete it!"

UrgentVsEffort = [["" for _ in range(4)] for _ in range(4)]
UrgentVsEffort[Priorities.HIGH][Priorities.HIGH] = "You should better hurry up!"
UrgentVsEffort[Priorities.HIGH][Priorities.LOW] = "You should bring it to an end."
UrgentVsEffort[Priorities.LOW][Priorities.HIGH] = "You should make a plan for it."
UrgentVsEffort[Priorities.LOW][Priorities.LOW] = "You can delay it."

print("=======================================================================")
print("                               GUIDELINE                               ")
print("=======================================================================")
print("URGENCY:")
print("If the deadline is today the URGENCY should be HIGH (3).")
print("If the deadline is this week the URGENCY should be MEDIUM (2).")
print("If the deadline is further away the URGENCY should be LOW (1).")
print("")
print("IMPACT:")
print("If the task really changes things the IMPACT should be HIGH (3).")
print("If it is a routine task or nothing special the IMPACT should be NORMAL (2).")
print("For trivial tasks the IMPACT should be LOW (1).")
print("")
print("EFFORT:")
print("If the estimated time is higher than 40h, EFFORT should be HIGH (3).")
print("If the estimated time is around a day, EFFORT should be MEDIUM (2).")
print("If the estimated time lower than a day, EFFORT should be LOW (1).")
print("")
print("")
print("Allowed input values:")
for i in range(1, depths + 1):
    print("{0} = {1}".format(i, Priorities(i).name))
print("")
print("=======================================================================")
print()
while True:
    try:
        # Input
        print("Calculate a new task priority")
        print()
        urgency = Priorities(int(input("Urgency: ")))
        impact = Priorities(int(input("Impact : ")))
        effort = Priorities(int(input("Effort : ")))

        # Output
        priority = matrix3D[urgency - 1][impact - 1][effort - 1]
        print()
        print("==============================")
        print("The priority of the task is: {0}".format(priority))
        print("==============================")
        print(
            "{0}{1}{2}".format(
                EffortVsImpact[effort][impact],
                UrgentVsImpact[urgency][impact],
                UrgentVsEffort[urgency][effort],
            )
        )

    except ValueError:
        print("Invalid entered task priority. Please try again.")
    finally:
        print()
