DROP DATABASE IF EXIST restaurant_baza;

USE restaurant_baza;

CREATE TABLE restaurant (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    adress VARCHAR(255) NOT NULL,
    postcode VARCHAR(10) NOT NULL
);

CREATE TABLE employee_position (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE roles (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    personal_id VARCHAR(11) NOT NULL
);

CREATE TABLE employment (
    restaurant_id INT UNSIGNED NOT NULL,
    employee_id INT UNSIGNED NOT NULL,
    employee_position_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (restaurant_id, employee_id),
    CONSTRAINT FK_Restaurant_Employee_Restaurant FOREIGN KEY (restaurant_id) REFERENCES restaurant(id),
    CONSTRAINT FK_Restaurant_Employee_Employee FOREIGN KEY (employee_id) REFERENCES employee(id),
    CONSTRAINT FK_Restaurant_Employee_Roles FOREIGN KEY (employee_position_id) REFERENCES employee_position(id)
);

CREATE TABLE reservation (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT UNSIGNED NOT NULL,
    restaurant_table_id INT UNSIGNED NOT NULL,
    surname VARCHAR(50) NOT NULL,
    reservation_date DATE NOT NULL,
    phone VARCHAR(12) NOT NULL,
    guests INT UNSIGNED NOT NULL,
    CONSTRAINT FK_Reservation_Restaurant FOREIGN KEY (restaurant_id) REFERENCES restaurant(id),
    CONSTRAINT FK_Reservation_Restaurant_Table FOREIGN KEY (restaurant_table_id) REFERENCES restaurant_table(id)
);

CREATE TABLE meal_type (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE meal (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    meal_type_id INT UNSIGNED NOT NULL,
    restaurant_id INT UNSIGNED NOT NULL,
    price INT NOT NULL,
    meal_name VARCHAR(100) NOT NULL,
    CONSTRAINT FK_Meal_Meal_Type FOREIGN KEY (meal_type_id) REFERENCES meal_type(id),
    CONSTRAINT FK_Meal_Restaurant FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
);