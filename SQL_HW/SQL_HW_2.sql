        1. Таблица employees

Создать таблицу employees
- id. serial,  primary key,
- employee_name. Varchar(50), not null
Наполнить таблицу employee 70 строками.


create table employees
(id SERIAL PRIMARY KEY,
employee_name varchar(50) not null);


insert into employees (employee_name)
values ('Anton'),
('Olga'),
('Max'),
('Serg'),
('Petr'),
('Polina'),
('Sveta'),
('Igor'),
('Dmitry'),
('Vasiliy'),
('Rosa'),
('Elena'),
('Alex'),
('Maxim'),
('Michail'),
('Volody'),
('Vadim'),
('Ivan'),
('Nasty'),
('Gena'),
('Artem'),
('Artur'),
('Bogdan'),
('Ira'),
('Inna'),
('Nikita'),
('Inga'),
('Den'),
('Marya'),
('Natasha'),
('Denis'),
('Jim'),
('Ekaterina'),
('Jack'),
('William'),
('Rita'),
('Milana'),
('Sony'),
('Sofia'),
('Galina'),
('Leonid'),
('Lyba'),
('Tom'),
('Bred'),
('Rima'),
('Slavomir'),
('Nikolay'),
('Andrey'),
('Anton'),
('Max'),
('Polina'),
('Grisha'),
('Arnold'),
('Valentina'),
('Eva'),
('Vika'),
('Veronika'),
('Alina'),
('Diana'),
('Kirill'),
('Vladislav'),
('Tima'),
('Timur'),
('Adam'),
('Lev'),
('Danila'),
('Karolina'),
('Nina'),
('Nika');


        2. Таблица salary

Создать таблицу salary
- id. Serial  primary key,
- monthly_salary. Int, not null
Наполнить таблицу salary 15 строками:
- 1000
- 1100
- 1200
- 1300
- 1400
- 1500
- 1600
- 1700
- 1800
- 1900
- 2000
- 2100
- 2200
- 2300
- 2400
- 2500

create table salary
(id serial primary key,
monthly_salary int not null);

insert into salary (monthly_salary)
values (1000),
       (1100),
       (1200),
       (1300),
       (1400),
       (1500),
       (1600),
       (1700),
       (1800),
       (1900),
       (2000),
       (2100),
       (2200),
       (2300),
       (2400),
       (2500);


        3. Таблица employee_salary

Создать таблицу employee_salary
- id. Serial  primary key,
- employee_id. Int, not null, unique
- salary_id. Int, not null
Наполнить таблицу employee_salary 40 строками:
- в 10 строк из 40 вставить несуществующие employee_id

create table employee_salary
(id serial primary key,
employee_id int not null unique,
salary_id int not null);

insert into employee_salary (employee_id, salary_id)
values (1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(10,10),
(11,11),
(12,12),
(13,13),
(14,14),
(15,15),
(16,16),
(17,17),
(18,18),
(19,19),
(20,20),
(21,21),
(22,22),
(23,23),
(24,24),
(25,25),
(26,26),
(27,27),
(28,28),
(29,29),
(30,30),
(100,31),
(101,32),
(102,33),
(103,34),
(104,35),
(105,36),
(106,37),
(107,38),
(108,39),
(109,40);


        4. Таблица roles

Создать таблицу roles
- id. Serial  primary key,
- role_name. int, not null, unique
Поменять тип столба role_name с int на varchar(30)
Наполнить таблицу roles 20 строками:

create table roles 
(id serial primary key,
role_name int not null unique);

ALTER TABLE roles 
ALTER COLUMN role_name
TYPE varchar(30);

insert into roles (role_name)
values ('Junior Python developer'),
	   ('Middle Python developer'),
	   ('Senior Python developer'),
	   ('Junior Java developer'),
	   ('Middle Java developer'),   
	   ('Senior Java developer'),
	   ('Junior JavaScript developer'),
	   ('Middle JavaScript developer'),
	   ('Senior JavaScript developer'),
	   ('Junior Manual QA engineer'),
	   ('Middle Manual QA engineer'),
	   ('Senior Manual QA engineer'),
	   ('Project Manager'),
	   ('Designer'),
	   ('HR'),
	   ('CEO'),
	   ('Sales manager'),
	   ('Junior Automation QA engineer'),
	   ('Middle Automation QA engineer'),
	   ('Senior Automation QA engineer');

        5. Таблица roles_employee

Создать таблицу roles_employee
- id. Serial  primary key,
- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
- role_id. Int, not null (внешний ключ для таблицы roles, поле id)
Наполнить таблицу roles_employee 40 строками:

create table roles_employee
(id serial  primary key,
employee_id int not null unique,
role_id int not null,
foreign key (employee_id)
references employees(id),
foreign key (role_id)
references roles(id));

insert into roles_employee (employee_id,role_id)
values (1,1),
	   (2,2),
	   (3,3),
	   (4,4),
	   (5,5),
	   (6,6),
	   (7,7), 
	   (8,8),
	   (9,9),
	   (10,10),
	   (11,11),
	   (12,12),
	   (13,13),
	   (14,14),
	   (15,15),
	   (16,16), 
	   (17,17),
	   (18,18),
	   (19,19),
	   (20,20),
	   (21,17),
	   (22,13),
	   (23,9),
	   (24,4),
	   (25,8),
	   (26,15),
	   (27,20), 
	   (28,11),
	   (29,14),
	   (30,2),
	   (31,5),
	   (32,19),
	   (33,1),
	   (34,18),
	   (35,7),
	   (36,3),
	   (37,7),
	   (38,10), 
	   (39,12),
	   (40,15);
