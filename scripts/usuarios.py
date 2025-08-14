from faker import Faker
import random
from datetime import datetime
from google.colab import files

fake = Faker()

def write_to_sql_file(filename, statements):
    with open(filename, 'a') as file:
        for statement in statements:
            file.write(statement + ';\n')

def generate_user_statements(batch_size, start_index):
    statements = []
    for i in range(start_index, start_index + batch_size):
        username = f'user_{i}'
        email = fake.email()
        password = fake.password()
        plan_type = fake.random_element(elements=["Beginner Plan", "Intermediate Plan", "Professional Plan"])
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date='today', end_date='+1y')
        statement = f"INSERT INTO subscriber (username, email, password, type, start_date, end_date) VALUES ('{username}', '{email}', '{password}', '{plan_type}', '{start_date}', '{end_date}')"
        statements.append(statement)
    return statements

batch_size = 1000
total_users = 30000
filename = 'data_inserts_users.sql'
open(filename, 'w').close()

for start in range(0, total_users, batch_size):
    user_statements = generate_user_statements(min(batch_size, total_users - start), start)
    write_to_sql_file(filename, user_statements)

files.download(filename)
print("SQL file created successfully!")