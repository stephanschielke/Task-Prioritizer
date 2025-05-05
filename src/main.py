from enum import IntEnum
import argparse


class Value(IntEnum):
    """
    Priority levels (internal 0-based):
      0 = HIGH
      1 = MEDIUM
      2 = LOW
    """
    HIGH = 0
    MEDIUM = 1
    LOW = 2

# Emoji-enhanced suggestion mappings tuned for everyday tasks
_effort_vs_impact: dict[Value, dict[Value, str]] = {
    Value.HIGH: {
        Value.HIGH: "💼 Tackle with a dedicated session",
        Value.MEDIUM: "🔧 Break into smaller steps",
        Value.LOW: "📤 Postpone or delegate"
    },
    Value.MEDIUM: {
        Value.HIGH: "🕒 Allocate a focused time block",
        Value.MEDIUM: "📝 Plan for today",
        Value.LOW: "📆 Do when convenient"
    },
    Value.LOW: {
        Value.HIGH: "⚡ Quick win—handle now",
        Value.MEDIUM: "🧩 Fit into next free slot",
        Value.LOW: "🗂️ Skip or batch later"
    }
}

_impact_vs_urgency: dict[Value, dict[Value, str]] = {
    Value.HIGH: {
        Value.HIGH: "🚨 Do immediately",
        Value.MEDIUM: "📌 Schedule for today",
        Value.LOW: "🗓️ Plan by week's end"
    },
    Value.MEDIUM: {
        Value.HIGH: "⏰ Set a quick reminder",
        Value.MEDIUM: "📋 Do in the next couple days",
        Value.LOW: "📥 Add to to-do list"
    },
    Value.LOW: {
        Value.HIGH: "📤 Delegate or drop",
        Value.MEDIUM: "📉 Tackle during downtime",
        Value.LOW: "🗃️ Ignore or archive"
    }
}

_urgency_vs_effort: dict[Value, dict[Value, str]] = {
    Value.HIGH: {
        Value.HIGH: "📅 Block out a free afternoon",
        Value.MEDIUM: "⏳ Carve out a 30-minute slot",
        Value.LOW: "⚡ Handle right away"
    },
    Value.MEDIUM: {
        Value.HIGH: "🕓 Plan a tomorrow time slot",
        Value.MEDIUM: "📓 Schedule in your planner",
        Value.LOW: "🕰️ Do when you get a minute"
    },
    Value.LOW: {
        Value.HIGH: "📆 Plan for next week",
        Value.MEDIUM: "🗓️ Slot into calendar",
        Value.LOW: "🎈 Do whenever"
    }
}

def print_mapping() -> None:
    """
    Show valid input range and meaning.
    """
    print("Enter values 1-3 for each prompt: 1=HIGH, 2=MEDIUM, 3=LOW.\n")

def calc_priority(urgency: Value, impact: Value, effort: Value) -> int:
    """
    Compute priority: sum of values + 1 ⇒ range 1–7.
    """
    return urgency + impact + effort + 1

def get_suggestions(urgency: Value, impact: Value, effort: Value) -> list[str]:
    """
    Return suggestions based on pairwise comparisons.
    """
    return [
        _effort_vs_impact[effort][impact],
        _impact_vs_urgency[impact][urgency],
        _urgency_vs_effort[urgency][effort],
    ]

def prompt_once(args: argparse.Namespace | None = None) -> None:
    """
    Single round: read inputs, compute and display results.
    Accept CLI args if provided.
    """
    try:
        if args and args.urgency is not None and args.impact is not None and args.effort is not None:
            u = Value(args.urgency - 1)
            i = Value(args.impact - 1)
            e = Value(args.effort - 1)
        else:
            u = Value(int(input("Urgency (1-3): ")) - 1)
            i = Value(int(input("Impact  (1-3): ")) - 1)
            e = Value(int(input("Effort  (1-3): ")) - 1)
    except (ValueError, KeyError):
        print("Invalid input; please enter 1, 2, or 3.\n")
        return

    score = calc_priority(u, i, e)
    suggestions = get_suggestions(u, i, e)

    print(f"\nPriority score: {score}\n")
    print("Suggestions:")
    for s in suggestions:
        print(f"- {s}")

def interactive_loop() -> None:
    """
    Continuously prompt until user stops (Ctrl+C).
    """
    try:
        while True:
            prompt_once()
            print()  # blank line between rounds
    except KeyboardInterrupt:
        print("\nExiting interactive mode.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Task priority calculator")
    parser.add_argument('-o', '--once', action='store_true', help='run a single round and exit')
    parser.add_argument('--urgency', type=int, choices=range(1, 4), help='urgency (1=HIGH, 2=MEDIUM, 3=LOW)')
    parser.add_argument('--impact', type=int, choices=range(1, 4), help='impact (1=HIGH, 2=MEDIUM, 3=LOW)')
    parser.add_argument('--effort', type=int, choices=range(1, 4), help='effort (1=HIGH, 2=MEDIUM, 3=LOW)')
    args = parser.parse_args()

    print_mapping()
    if args.once or (args.urgency and args.impact and args.effort):
        prompt_once(args)
    else:
        interactive_loop()


if __name__ == "__main__":
    main()
