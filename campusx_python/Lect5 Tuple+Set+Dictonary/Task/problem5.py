# Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# Show every students record in form of tuples if matches all required criteria.

# It is assumed that there will be only one primry skill.

# If no such candidate found, print No such candidate

# Input:

# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
# Output

# ('Manohar', 'B.tech', 'Python', '2022')

# Shortlist Students for a Job role

n = int(input("Enter No of records- "))

# List to store shortlisted students
p = []

# List to store all student records as tuples
students = []

# Taking student records as input
for i in range(n):
    print(f"Enter Details of student-{i+1}")

    name = input("Enter Student name- ")
    education = input("Enter Higher Education- ")
    skill = input("Enter Primary Skill- ")
    year = input("Enter Year of Graduation- ")

    # Storing each student's details in a tuple
    students.append((name, education, skill, year))

# Taking job requirements as input
print("\nEnter Job Role Requirement")

req_skill = input("Enter Skill- ")
req_education = input("Enter Higher Education- ")
req_year = input("Enter Year of Graduation- ")

# Checking each student against the required criteria
for i in students:

    # Tuple format:
    # (name, education, skill, year)
    #   0         1        2      3

    if i[2] == req_skill and i[1] == req_education and i[3] == req_year:
        p.append(i)

# If matching students are found, print them
if len(p) > 0:
    print("The students who qualified the criteria are:")
    for i in p:
        print(i)

# If no matching student is found
else:
    print("No such candidate")
        
        