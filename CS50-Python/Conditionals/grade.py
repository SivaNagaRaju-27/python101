score = int(input("Score: "))

def grd(score):
    if score>=90 and score<=100:
        print("Grade: A")
    elif score>=80 and score<=89:
        print("Grade: B")
    elif score>=70 and score<=79:
        print("Grade: C")
    elif score>=60 and score<=69:
        print("Grade: D")
    else:
        print("Grade: F")

def grd1(score):
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

def grd2(score):
    if score>=90:
        print("Grade: A")
    elif score>=80:
        print("Grade: B")
    elif score>=70:
        print("Grade: C")
    elif score>=60:
        print("Grade: D")
    else:
        print("Grade: F")


grd(score)
grd1(score)
grd2(score)
