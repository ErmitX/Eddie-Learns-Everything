import time
import random

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.008)
    print()

def pause():
    input("\nPress ENTER to continue...")

print("=" * 65)
print("                     THE LEARNING MONTAGE")
print("=" * 65)
print()

type_text("NZT has changed the way Eddie sees the world.")
type_text("But he quickly discovers something even more powerful.")
type_text("Knowledge.")
print()

type_text("He doesn't want to know a little.")
type_text("He wants to know everything.")
pause()

subjects = {
    "Languages": [
        "Spanish",
        "Italian",
        "French",
        "Japanese",
        "Mandarin"
    ],
    "Science": [
        "Physics",
        "Chemistry",
        "Biology",
        "Astronomy"
    ],
    "Humanities": [
        "History",
        "Psychology",
        "Philosophy",
        "Economics"
    ],
    "Skills": [
        "Piano",
        "Chess",
        "Programming",
        "Public Speaking"
    ]
}

total = 0

for category, items in subjects.items():
    print()
    print("=" * 50)
    print(category.upper())
    print("=" * 50)

    for item in items:
        type_text("Studying " + item + "...")
        time.sleep(0.3)

        speed = random.randint(92, 100)
        total += speed

        print("Understanding:", str(speed) + "%")
        print("Status: MASTERED")
        print()

type_text("Days become weeks.")
type_text("Eddie barely sleeps.")
type_text("He reads entire books in a single evening.")
type_text("He watches lectures at impossible speed.")
type_text("He remembers everything.")
pause()

print()
print("=" * 65)
print("                     A NEW EDDIE")
print("=" * 65)
print()

print("Knowledge:", min(100, total // 5), "/ 100")
print("Memory:   100 / 100")
print("Focus:    100 / 100")
print("Confidence: 95 / 100")

print()

type_text("Eddie walks into a piano store.")
type_text("He has never played before.")
print()

type_text("A salesman watches him sit down.")

print()
print("1. Play something simple")
print("2. Play something impossible")
print("3. Leave")

while True:
    answer = input("\n> ")

    if answer == "1":
        type_text("Eddie begins to play.")
        type_text("The melody is flawless.")
        break

    elif answer == "2":
        type_text("Eddie begins playing.")
        type_text("The salesman stops breathing.")
        type_text("Every note is perfect.")
        type_text("Eddie has never touched a piano before.")
        break

    elif answer == "3":
        type_text("Eddie walks away.")
        type_text("There are still thousands of things left to learn.")
        break

    else:
        print("Choose 1, 2, or 3.")

print()
type_text("The world is no longer a mystery.")
type_text("It is a puzzle.")
type_text("And Eddie finally knows how to solve it.")