coursecode=["       ","ESLEO = English Level 5","ESLDO = English Level 4","ENG3U = Grade 11 English","BAF3M = Grade 11 Accounting","ICS3U = Grade 11 Computer Science","MTH1W = Grade 9 Math","MPM2D = Grade 10 Math","     "]
students=[["        ","Name:","   Andrew", "Courses:","   MTH1W","   ELSEO","   BAF3M","   ICS3U","        "],
["      ","Name:","   Rafi","Courses:","   MPM2D","   ESLDO","   BAF3M","   None","      "],
["      ","Name:","   Dane","Courses:","   Unknown","   ESLEO","   Unknown","   ICS3U","     "],
["      ","Name:","   Phat","Courses:","   Unknown","   ESLEO","   Unknown","   ICS3U","     "],
["      ","Name:","   Eleanor", "Courses:","   Unknown","   ENG3U","   BAF3M","   ICS3U","       "],
["      ","Name:","   Krystal","Courses:","   Unknown","   Unknown","   BAF3M","   ICS3U","      "],
["      ","Name:","   Green","Courses:","   Unkown","   ESLEO","   BAF3M","   Unknown","     "],
["      ","Name:","   Jenny","Courses:","   MPM2D","   ESLEO","   Unknown","   Unknown","        "],
["      ","Name:","   Khalid","Courses:","   MTH1W","   Unknown","   BAF3M","   Unknown","      "]]
studentlist=["Andrew","Rafi","Dane","Phat","Eleanor","Krystal","Green","Jenny","Khalid"]

while True:
    x=int(input("Input A number 1-9(input '0' for the student and course code reference list):\n"))
    if x == 0:
        z=int(input("Input '0' for student list or '1' for course codes.\n"))
        if z==0:
            for j in range(len(studentlist)):
                print("(",(j+1),")",studentlist[j])
        elif z==1:
            for k in range(len(coursecode)):
                print(coursecode[k])
    elif x in range(1,10):
        for a in range(len(students)):
            y=0+a
            print(students[x-1][y])
    else:
        print("That student isn't in our database yet.")
        break