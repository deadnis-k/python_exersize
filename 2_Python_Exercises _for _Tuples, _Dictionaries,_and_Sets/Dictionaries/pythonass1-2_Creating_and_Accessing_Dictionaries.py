student = {
    'name': 'John Doe',
    'age': 16,
    'grade': '10th'
}

print(student['name'])

student['school'] = 'Greenwood High School'
print(student)

student['age'] = 2
student.pop('grade')



print(student)