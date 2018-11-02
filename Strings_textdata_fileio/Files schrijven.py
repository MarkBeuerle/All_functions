from datetime import datetime
with open("hardlopers.txt", "w") as f:
    date = datetime.today().strftime("%a %d %b %Y")
    time = datetime.today().strftime("%T")
    runner = input("Hardloper : ")
    print(date+", ", time, runner)
    f.write(", ".join([date, time, runner]) + "\n")
