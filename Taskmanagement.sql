CREATE DATABASE taskmanager;
USE taskmanager;

CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    priority VARCHAR(255),
    status VARCHAR(255)
);
