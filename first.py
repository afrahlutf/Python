def getAverage(query_name):
    for name in student_marks:
        if(name == query_name):
            avg += 
   
  

n = int(input("enter a number:"))
student_marks = {}
for _ in range(n):
    name, *line = input("enter students names:").split( )
    print(name,line)
    scores = list(map(float,line))
    student_marks[name] = scores
    query_name = input("enter query name:")
    getAverage(query_name)
    print(line)
