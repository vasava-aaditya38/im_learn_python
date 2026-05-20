marks={
    "aaditya":98,       
    "viren":95,
    "dhruv":96,
    "jeet":90
}
print(marks.items())
print(marks.keys())
marks.update({"aaditya":99 , "hemil":90})           #{ } is important

print(marks.get("viren"))
marks.update({"hemil":41})
print(marks)
