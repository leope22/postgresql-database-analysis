CREATE TABLE instructor (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    biography TEXT
);

CREATE TABLE course (
    code INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    instructor_id INT,
    
    FOREIGN KEY(instructor_id) REFERENCES instructor(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE lesson (
    code INT,
    title VARCHAR(100),
    description TEXT,
    
    PRIMARY KEY (code, title),
    FOREIGN KEY(code) REFERENCES course(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE plan (
    type VARCHAR(100) PRIMARY KEY,
    price FLOAT NOT NULL
);

CREATE TABLE subscriber (
    username VARCHAR(50) PRIMARY KEY,
    email VARCHAR(75) NOT NULL,
    password VARCHAR(50) NOT NULL,
    type VARCHAR(100),
    start_date DATE,
    end_date DATE,
    
    FOREIGN KEY(type) REFERENCES plan(type)
        ON UPDATE CASCADE
        ON DELETE SET DEFAULT
);

CREATE TABLE course_plan (
    code INT,
    type VARCHAR(100),
    
    PRIMARY KEY(code, type),
    FOREIGN KEY(code) REFERENCES course(code)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(type) REFERENCES plan(type)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO plan (type, price) VALUES ('Beginner Plan', 50.00), ('Intermediate Plan', 100.00), ('Professional Plan', 250.00);