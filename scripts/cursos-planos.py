import random
from faker import Faker
from google.colab import files

fake = Faker()

def write_to_sql_file(filename, statements):
    with open(filename, 'a') as file:
        for statement in statements:
            file.write(statement + ';\n')

def generate_course_plan_statements(batch_size, course_plans):
    values_list = []
    for course_code, plan_type in course_plans:
        values_list.append(f"({course_code}, '{plan_type}')")
        if len(values_list) == batch_size:
            yield f"INSERT INTO course_plan (code, type) VALUES " + ", ".join(values_list)
            values_list = []
    if values_list:
        yield f"INSERT INTO course_plan (code, type) VALUES " + ", ".join(values_list)

curso_planos = []
curso_planos.extend(
    (course_code, "Beginner Plan") for course_code in range(1, 200001)
)
curso_planos.extend(
    (course_code, "Intermediate Plan") for course_code in range(1, 350001)
)
curso_planos.extend(
    (course_code, "Professional Plan") for course_code in range(1, 500001)
)

batch_size = 1000
filename = 'data_inserts_courses_plans.sql'

open(filename, 'w').close()

for statement in generate_course_plan_statements(batch_size, curso_planos):
    write_to_sql_file(filename, [statement])

files.download(filename)

print("SQL file created successfully!")