

def create_outline():
    print("Course Topics:")
    Course_Topics = {
    "Introduction to Python",
    "Tools of the Trade",
    "How to make decisions",
    "How to repeat code",
    "How to structure data",
    "Functions",
    "Modules"
    }
    topics = list(Course_Topics)
    topics.sort()
    for T in topics:
        print("*",T)
        
    print("Problems:")
    var = ["Problem 1"," Problem 2"," Problem 3"]
    for i in topics:
        my_dict = {i: var}
        print('* '+i + " :" ,','.join(my_dict[i]))
    
    
    print("Student Progress:")
    student_progress = [("Belo","Functions","Problem 2","[GRADED]"),
        ("Andiswa","Tools of trade","Problem 1","[STARTED]"),
        ("Tokollo","Modules","Problem 3","[COMPLETED]"),
        ("Jeffgazi","How to structure data","Problem 1","[COMPLETED]")]
    student_progress.sort()
    t = 0
    for a,b,c,d in(student_progress):
        t += 1
        print(str(t)+". "+a," -",b+" -",c,d)
           


if __name__ == "__main__":
    create_outline()
