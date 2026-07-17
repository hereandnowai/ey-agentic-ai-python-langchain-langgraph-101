# 🎓 Capstone Project — Build Your Own Python App

Welcome to your capstone! This is where **you** put together everything from
Day 1 and Day 2 — variables, lists, dicts, functions, JSON, and a Gradio UI —
to build a small but complete application **on your own**.

This folder is intentionally almost empty. There is **no finished solution
here**. Instead, this guide shows you *how* to build it, with small examples
and hints. Copy the ideas, don't copy a solution — that's how you actually
learn. 💪

---

## 🧠 What you already know how to build

You have already built two working apps this week. Your capstone reuses the
**exact same shape**:

```
   contacts.py   (BACKEND: functions + JSON)   ← the real Python
        │
        ▼
   app.py        (FRONTEND: a Gradio screen)   ← just calls the backend
        │
        ▼
   contacts.json (DATA: saved on disk)          ← survives restarts
```

Your capstone is just this same pattern applied to a **new idea**.

---

## 1️⃣ Pick ONE project

Choose whichever excites you. Each is the same difficulty and uses the same
skills. (Want your own idea? Great — just clear it with your instructor.)

| # | Project | Each item stores… |
|---|---------|-------------------|
| A | **Expense Tracker** 💸 | title, amount, category, date |
| B | **To-Do / Task Manager** ✅ | task, priority, done (True/False) |
| C | **Personal Library** 📚 | title, author, rating, read? |
| D | **Recipe Box** 🍲 | name, ingredients (list), minutes |
| E | **Habit Tracker** 🔥 | habit, streak (number), last done |

Throughout this guide we'll use the **Expense Tracker** as the running
example. Swap in your own fields for the project you picked.

---

## 2️⃣ Set up your folder

Inside this `capstone/` folder, create three files:

```
capstone/
├── store.py          # BACKEND — your functions + JSON (like contacts.py)
├── app.py            # FRONTEND — your Gradio screen (like the calculator/contact app)
└── data.json         # created automatically the first time you save
```

> 💡 Tip: open `day-2/contact_book/contacts.py` in one window as your
> reference while you build `store.py`. You are writing the *same kind* of
> code for a different topic.

---

## 3️⃣ Milestones (build in this order!)

Don't try to build everything at once. Finish one milestone, **run it**,
make sure it works, then move to the next. Small steps, always working.

### ✅ Milestone 1 — Save & load data (JSON)

Start with the two functions every project needs. This is straight from
`contacts.py`:

```python
# store.py
import json
import os

FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load():
    """Return all saved items as a list (empty list on the first run)."""
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []                      # tip: use [] if you store a LIST of items

def save(items):
    """Write the whole list back to the JSON file."""
    with open(FILE, "w") as f:
        json.dump(items, f, indent=2)
```

> ❓ Decision: a **list** `[]` or a **dict** `{}`? Use a **dict** when every
> item has a unique name (like the contact book). Use a **list** when items
> can repeat or have no natural key (expenses, tasks) — that's what we do here.

**Test it before moving on:**

```python
# temporary test at the bottom of store.py — delete later
save([{"title": "Coffee", "amount": 120, "category": "food"}])
print(load())
```

Run: `python store.py` — you should see your item printed, and a new
`data.json` file should appear. 🎉

---

### ✅ Milestone 2 — Add an item

```python
def add(title, amount, category):
    """Add one expense and return a friendly message."""
    items = load()
    items.append({
        "title": title,
        "amount": float(amount),        # remember: input from a screen is text!
        "category": category,
    })
    save(items)
    return f"Added {title} ({amount})."
```

> ⚠️ Common beginner trap: numbers typed into a UI arrive as **strings**.
> Convert with `float(amount)` or `int(amount)` before you do maths.

---

### ✅ Milestone 3 — Show all items + a total

Use a **loop** (Day 2) to build a report, and `sum()` with a **comprehension**
for the total:

```python
def list_all():
    items = load()
    if not items:
        return "No expenses yet."
    lines = [f"- {it['title']}: {it['amount']} ({it['category']})" for it in items]
    total = sum(it["amount"] for it in items)      # comprehension inside sum()
    return "\n".join(lines) + f"\n\nTOTAL: {total:.2f}"
```

---

### ✅ Milestone 4 — Delete / mark done / update

Pick what fits your project. Example: delete by position.

```python
def delete(index):
    items = load()
    if 0 <= index < len(items):        # guard against a bad index
        removed = items.pop(index)
        save(items)
        return f"Deleted {removed['title']}."
    return "That item does not exist."
```

> 🧩 For a **To-Do** app, write `mark_done(index)` that flips the item's
> `"done"` value to `True` instead of deleting it.

---

### ✅ Milestone 5 — A simple Gradio screen

Now the frontend. Start with the **simple `gr.Interface` style** from the
calculator — it's the easiest. Your UI just *calls* your backend functions.

```python
# app.py
import gradio as gr
import store                      # your own backend from store.py

def add_expense(title, amount, category):
    store.add(title, amount, category)
    return store.list_all()       # show the refreshed report after adding

demo = gr.Interface(
    fn=add_expense,
    inputs=[
        gr.Textbox(label="Title"),
        gr.Number(label="Amount"),
        gr.Dropdown(["food", "travel", "bills", "fun"], label="Category"),
    ],
    outputs=gr.Textbox(label="Your expenses"),
    title="My Expense Tracker",
    description="My capstone project",
)

if __name__ == "__main__":
    demo.launch()
```

Run: `python app.py`, open the link, and add a few expenses. **You built an
app!** 🚀

> 🎨 Want the polished, CRM-style look from the contact book? That uses the
> more advanced `gr.Blocks` layout. Get the simple version working **first**,
> then study `day-2/contact_book/app.py` and borrow ideas from it.

---

## 4️⃣ Stretch goals (only after the 5 milestones work)

Pick any that appeal to you:

- 🔎 **Search / filter** — show only expenses in one category (reuse the
  filtering comprehension from `04_comprenhensions.py`).
- 📊 **Summary by category** — a dict `{category: total}` built in a loop
  (like the word-count example in `02_dicts.py`).
- 🧮 **Sorting** — show items sorted by amount using
  `sorted(items, key=lambda it: it["amount"])` (see `05_nested_loops_and_sorting.py`).
- 🧠 **Type hints + docstrings** on every function (see `07_type_hints_docstrings.py`).
- ✅ **Self-tests** with `assert` at the bottom of `store.py`.
- 🎨 **Custom theme / colours** in Gradio.

---

## 5️⃣ Definition of "done" ✅

Tick these off before you present:

- [ ] `store.py` has `load`, `save`, `add`, `list_all`, and one more action.
- [ ] Data survives a restart (close the app, reopen — items still there).
- [ ] `app.py` runs with `python app.py` and has no crashes.
- [ ] Numbers from the UI are converted before any maths.
- [ ] Every function has a one-line docstring saying what it does.
- [ ] You added at least **one** stretch goal.
- [ ] You can explain, in your own words, how the frontend talks to the backend.

---

## 6️⃣ How to get unstuck 🆘

1. **Read the error message** — it usually names the file and line number.
2. **Print things** — add `print(...)` to see what a variable actually holds.
3. **Go back to the lesson file** that covers the topic (lists, dicts, JSON…).
4. **Compare with the contact book** — you have a full working example.
5. **Build smaller** — get one tiny piece working, then add the next.

---

### 🏆 Remember

> You are not expected to write perfect code. You are expected to build
> something that **works**, understand **why** it works, and be able to
> **explain** it. That is what a real developer does.

**Good luck — you've got this!** 🌟
