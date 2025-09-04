marks = {
    "Azham": 100,
    "Ali": 35,
    "Ahmad" : 68
}

print(marks)
print(marks.items())

marks.update({"Ahmad":70})
print(marks)

print(marks.get("Ali"))
print(marks.keys())

print(marks.pop("Azham"))
print(len(marks))

marks.clear()
print(marks)