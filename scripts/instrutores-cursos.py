from faker import Faker
import random
from google.colab import files

fake = Faker()

def write_to_sql_file(filename, statements):
    with open(filename, 'a') as file:
        for statement in statements:
            file.write(statement + ';\n')

def generate_instructor_statements(batch_size, start_index):
    statements = []
    for i in range(start_index, start_index + batch_size):
        name = fake.name()
        biography = fake.paragraph()
        statement = f"INSERT INTO instructor (id, name, biography) VALUES ({i}, '{name}', '{biography}')"
        statements.append(statement)
    return statements

def generate_course_statements(batch_size, start_index):
    course_categories = ["Computer Science", "Data Analysis", "Networks", "Softwares", "Business", "Economics", "Artificial Intelligence", "Robotics"]
    statements = []
    for i in range(start_index, start_index + batch_size):
        title = fake.catch_phrase()
        category = random.choice(course_categories)
        description = fake.paragraph()
        instructor_id = random.randint(1, 50000)
        statement = f"INSERT INTO course (code, title, category, description, instructor_id) VALUES ({i}, '{title}', '{category}', '{description}', {instructor_id})"
        statements.append(statement)
    return statements

batch_size = 1000
total_instructors = 50000
total_courses = 500000
filename = 'data_inserts_instructors_courses.sql'

open(filename, 'w').close()

for start in range(1, total_instructors + 1, batch_size):
    instructor_statements = generate_instructor_statements(min(batch_size, total_instructors - start + 1), start)
    write_to_sql_file(filename, instructor_statements)

for start in range(1, total_courses + 1, batch_size):
    course_statements = generate_course_statements(min(batch_size, total_courses - start + 1), start)
    write_to_sql_file(filename, course_statements)

files.download(filename)

print("SQL file created successfully!")