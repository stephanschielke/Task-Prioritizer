# 🧐 Task Prioritizer

A helpful little tool for organizing your tasks by **urgency**, **impact**, and **effort**—especially useful if you struggle with planning or prioritizing (hello ADHD brain 👋).

It assigns a **priority score** (1–7) and gives actionable, emoji-enhanced suggestions to help you decide what to do next.

---

## 📦 Installation

```bash
poetry install
```

---

## 🚀 Usage

### Interactive Mode (Default)

```bash
poetry run python src/main.py
```

You'll be asked for urgency, impact, and effort:

```
Enter values 1-3 for each prompt: 1=HIGH, 2=MEDIUM, 3=LOW.

Urgency (1-3): 2
Impact  (1-3): 2
Effort  (1-3): 2

Priority score: 4

Suggestions:
- 📝 Plan for today
- 📋 Do in the next couple days
- 📓 Schedule in your planner
```

This repeats until you exit (Ctrl+C).

---

### One-Time Execution with CLI Flags

```bash
poetry run python src/main.py --once --urgency 1 --impact 3 --effort 2
```

Outputs a single result and exits—great for scripts or integrations.

---

## 🧽 Priority Factors

For each task, rate the following:

### URGENCY (1–3)

- `1` = HIGH → Deadline is today
- `2` = MEDIUM → Due this week
- `3` = LOW → No rush

### IMPACT (1–3)

- `1` = HIGH → Big change or progress
- `2` = MEDIUM → Routine or moderate impact
- `3` = LOW → Trivial or minor result

### EFFORT (1–3)

- `1` = HIGH → >1 full day of work
- `2` = MEDIUM → A few hours
- `3` = LOW → <1 hour or quick task

---

## 📌 Why Use This?

✅ Prevent overwhelm  
✅ Focus on what truly matters  
✅ Get tailored nudges toward action

Whether you're planning a big project or just trying to clean your apartment, this tool helps you **decide what to do next** with clarity and ease.
