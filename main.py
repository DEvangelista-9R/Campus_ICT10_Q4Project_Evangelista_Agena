from pyscript import display # type: ignore
from js import document # type: ignore

import numpy as np
import matplotlib.pyplot as plt


# =========================
# CLASSMATE PROGRAM
# =========================

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello! My name is {self.name}. I am from Section {self.section}, and my favorite subject is {self.favorite_subject}."


# Existing classmates
classmates = [
    Classmate("Kaitlyn", "Ruby", "Math"),
    Classmate("Aisha", "Ruby", "Science"),
    Classmate("Zipporah", "Ruby", "English"),
    Classmate("Jade", "Ruby", "Social Studies"),
    Classmate("Koby", "Ruby", "Homeroom")
]


# Show classmates
def show_classmates():
    output = document.getElementById("output")

    text = "<h2>Classmate Introductions</h2>"

    for student in classmates:
        text += f"<p>{student.introduce()}</p>"

    output.innerHTML = text


# Add new classmate
def add_classmate(*args):

    name = document.getElementById("name").value
    section = document.getElementById("section").value
    favorite_subject = document.getElementById("favorite_subject").value

    if name == "" or favorite_subject == "":
        return

    new_student = Classmate(name, section, favorite_subject)

    classmates.append(new_student)

    show_classmates()

    document.getElementById("name").value = ""
    document.getElementById("favorite_subject").value = ""


show_classmates()


# =========================
# ATTENDANCE TRACKER
# =========================

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

absences = np.zeros(len(days), dtype=int)


def get_value(element_id):
    elem = document.getElementById(element_id)

    return elem.value if elem else ""


def draw_graph():

    plt.clf()

    x = np.arange(len(days))

    plt.bar(x, absences, width=0.6)

    plt.xticks(x, days)

    plt.ylim(0,5)

    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.title("Weekly Absences", pad=10)

    plt.xlabel("Days")

    plt.ylabel("Absences")

    display(plt.gcf(), target="plot", append=False)


def submit_data(*args):

    day = get_value("day")

    try:
        value = int(get_value("value") or 0)

    except ValueError:
        return

    if day not in days:
        return

    index = days.index(day)

    absences[index] = min(value)

    value_input = document.getElementById("value")

    if value_input:
        value_input.value = ""

    draw_graph()


draw_graph()
