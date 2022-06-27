
CREATE ROLE dev_tworedbirds WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'abc123';

CREATE DATABASE dev_tworedbirds
    WITH
    OWNER = dev_tworedbirds
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

CREATE SCHEMA dev_tworedbirds
    AUTHORIZATION dev_tworedbirds;


INSERT INTO auth_user ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")
 VALUES ('pbkdf2_sha256$320000$4nkfZVnYj1StKwuHq1BgZi$cYVPLGAIzZgfojWCxUoeANnZvK2aOghzbcho9k5klZg=', NULL, true, 'admin', '', '', '', true, true, now())


insert into department (id_department, nm_department) values (1, 'Engineering');
insert into department (id_department, nm_department) values (2, 'Human Resources');
insert into department (id_department, nm_department) values (3, 'Marketing');
SELECT setval('department_id_department_seq', 3);

insert into role (id_role, nm_role) values (1, 'Intern');
insert into role (id_role, nm_role) values (2, 'Junior');
insert into role (id_role, nm_role) values (3, 'Intermediate');
insert into role (id_role, nm_role) values (4, 'Senior');
insert into role (id_role, nm_role) values (5, 'Lead');
SELECT setval('role_id_role_seq', 5);

