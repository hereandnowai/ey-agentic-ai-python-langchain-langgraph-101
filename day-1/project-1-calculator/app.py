# ==========================================================================
# DAY 1 · Project 1 · Calculator — the FRONTEND (the screen the user sees)
# --------------------------------------------------------------------------
# Gradio is a Python library that builds a simple web UI for you. Here we
# use gr.Interface: you give it a function (fn) plus a description of the
# inputs and outputs, and Gradio draws the page and runs your function
# whenever the user clicks the button.
#
# The maths lives in calculator.py (the backend). This file only collects
# input from the screen, calls calculate(), and shows the result.
# Run it with:  python app.py   (needs: pip install gradio)
# ==========================================================================

import gradio as gr
from calculator import calculate  # our own backend function from calculator.py

def run(a, operation, b):
    """Called when the user clicks Calculate; returns the result as text.

    Gradio passes in the three input values (a, the chosen operation, and b).
    We hand them to calculate() and turn the number into a string so the
    Textbox can display it.
    """
    return str(calculate(a, operation, b))

demo = gr.Interface(
    fn=run,
    inputs=[
        gr.Number(label="First number"),
        gr.Radio(["add", "subtract", "multiply", "divide"], label="Operation", value="add"),
        gr.Number(label="Second Number")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Simple Calculator",
    description="Python backend + Gradio frontend"
)

# This line means: "only launch the web app when this file is run directly
# (python app.py), not when it is imported by another file."
if __name__ == "__main__":
    demo.launch()


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  the calculator "frontend"
# --------------------------------------------------------------------------
# Change the code above, then re-run:  python app.py
#
# 1. Change the title to "My Calculator" and write a better
#    description.
# 2. First add a "power" operation in calculator.py (see its activity 1),
#    THEN add "power" to the Radio choices here so it appears in the UI.
# 3. Add  examples=[[10, "add", 5], [9, "divide", 3]]  to gr.Interface so
#    users get one-click sample inputs.
# 4. In the UI, divide a number by zero. What happens? Make run() catch the
#    error (try/except) and return a friendly message instead of crashing.
# 5. BONUS: give the app a nicer theme — read the Gradio docs for
#    gr.themes.Soft() and pass it to demo.launch(theme=...).
# ==========================================================================