from faker import Faker
import random
from google.colab import files

fake = Faker()

def write_to_sql_file(filename, statements):
    with open(filename, 'a') as file:
        for statement in statements:
            file.write(statement + ';\n')

def generate_lesson_statements(batch_size):
    values_list = []
    for _ in range(batch_size):
        course_code = random.randint(1, 500000)
        title = fake.sentence().replace("'", "''")
        description = fake.text().replace("'", "''")
        values_list.append(f"({course_code}, '{title}', '{description}')")
    return f"INSERT INTO lesson (code, title, description) VALUES " + ", ".join(values_list)

batch_size = 1000
total_lessons = 1000000
filename = 'data_inserts_lessons.sql'
open(filename, 'w').close()

for start in range(0, total_lessons, batch_size):
    lesson_statement = generate_lesson_statements(min(batch_size, total_lessons - start))
    write_to_sql_file(filename, [lesson_statement])

files.download(filename)
print("SQL file created successfully!")