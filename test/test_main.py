from main import calc_priority, Value, get_suggestions


class Test3dPriority:
    def test_calc_priority(self):
        # Check extremes
        assert calc_priority(urgency=Value.HIGH, impact=Value.HIGH, effort=Value.HIGH) == 1
        assert calc_priority(urgency=Value.MEDIUM, impact=Value.MEDIUM, effort=Value.MEDIUM) == 4
        assert calc_priority(urgency=Value.LOW, impact=Value.LOW, effort=Value.LOW) == 7

        # Check a mix
        assert calc_priority(urgency=Value.LOW, impact=Value.MEDIUM, effort=Value.HIGH) == 4
        assert calc_priority(urgency=Value.HIGH, impact=Value.MEDIUM, effort=Value.LOW) == 4

        # Check at least every other priority is hit
        assert calc_priority(urgency=Value.HIGH, impact=Value.HIGH, effort=Value.MEDIUM) == 2
        assert calc_priority(urgency=Value.HIGH, impact=Value.MEDIUM, effort=Value.MEDIUM) == 3
        assert calc_priority(urgency=Value.MEDIUM, impact=Value.MEDIUM, effort=Value.LOW) == 5
        assert calc_priority(urgency=Value.MEDIUM, impact=Value.LOW, effort=Value.LOW) == 6

    def test_get_suggestions(self):
        assert get_suggestions(urgency=Value.HIGH, impact=Value.HIGH, effort=Value.HIGH) == [
            "It is a major project.",
            "Do it now!",
            "You should better hurry up!",
        ]

        assert get_suggestions(urgency=Value.MEDIUM, impact=Value.MEDIUM, effort=Value.MEDIUM) == ["", "", ""]

        assert get_suggestions(urgency=Value.LOW, impact=Value.LOW, effort=Value.LOW) == [
            "It is a fill in task.",
            "Delete it!",
            "You can delay it.",
        ]
