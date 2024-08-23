import pandas as pd

myclass = {
    "Name": ["Rishabh", "Sanjana Nayak", "Shaina Michael", "Monali", "Chaitanya", "Anish",
             "Nandey", "Rishabh", "Adarsh", "Simran", "Anish", "Siddharth", "Atheendra", "Aayushi"],
    "Age": [22, 24, 23, 25, 27, 26, 22, 24, 25, 23, 26, 27, 28, 24],
    "GPA": [3.8, 3.9, 3.7, 3.5, 3.6, 3.8, 3.4, 3.9, 3.2, 3.7, 3.5, 3.6, 3.9, 3.8],
    "Major": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering",
              "Computer Science", "Data Science", "Computer Science", "Data Science",
              "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
              "Mechanical Engineering", "Computer Science", "Data Science"]
}

data_frame = pd.DataFrame(myclass)
print(data_frame)

print("looping over column")
for column in data_frame.columns:
    print(f"column name = {column}")
    print(f"column values = {data_frame[column]}")

print("_"*100)
print("looping over rows")
for index, row in data_frame.iterrows():
    print(f"student Number = {index + 1}")
    print(f"student Name = {row['Name']}\n Age = {row['Age']}\n GPA = {row['GPA']}")

#let is get the minimum and maximum and mean and mode and median age
print("_"*100)
print("statistics of GPA")
print("minimum GPA of students = {min(data_frame['GPA'])}")
print("maximum GPA of students = {max(data_frame['GPA'])}")
print("mode GPA of students = {data_frame['GPA'].mode())}")
print("median GPA of students = {median(data_frame['GPA'])}")
print("mean GPA of students = {mean(data_frame['GPA'])}")


print("_"*100)
print("statistics of Age")
print(f"minimum Age of students = {min(data_frame['Age'])}")
print(f"minimum Age of students method 2 = {data_frame['Age'].min()}")
print(f"maximum Age of students = {max(data_frame['Age'])}")
print(f"maximum Age of students method 2  = {data_frame['Age'].max()}")
print(f"mode Age of students = {data_frame['Age'].mode()[0}")
print(f"median Age of students = {data_frame['Age'].median()}")
print(f"mean Age of students = {mean(data_frame['Age'].meam()}")


print("_"*100)
print("statistics of GPA")
print(f"Minimum GPA of students = {min(data_frame['GPA'])}")
print(f"Minimum GPA of students method 2 = {data_frame['GPA'].min()}")
print(f"Maximum GPA of students = {max(data_frame['GPA'])}")
print(f"Maximum GPA of students method 2  = {data_frame['GPA'].max()}")
print(f"Mode GPA of students = {data_frame['GPA'].mode()[0}")
print(f"Median GPA of students = {data_frame['GPA'].median()}")
print(f"Mean GPA of students = {mean(data_frame['GPA'].meam()}")