#!/usr/bin/env python
# coding: utf-8

# # SQL Challenge - Employee Data

# ## SQL Queries
# ```mysql
# -- list the details of each employee
# SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
# FROM salaries AS s
# INNER JOIN employees AS e ON
# e.emp_no = s.emp_no;
# 
# -- list the first name, last name, and hire date for employees who were hired in 1986
# SELECT first_name, last_name, hire_date
# FROM employees
# WHERE hire_date LIKE '%1986';
# 
# -- list the manager of each department with the following:
# -- department number, department name, manager's employee number, last name, first name
# CREATE VIEW managers AS
# SELECT dm.emp_no, dm.dept_no, d.dept_name
# FROM departments AS d
# JOIN dept_manager AS dm ON
# dm.dept_no = d.dept_no;
# 
# SELECT * FROM managers;
# 
# SELECT m.dept_no, m.dept_name, m.emp_no, e.last_name, e.first_name
# FROM employees AS e
# JOIN managers AS m ON
# m.emp_no = e.emp_no;
# 
# -- list the department of each employee with the following:
# -- employee number, last name, first name, department name
# CREATE VIEW emp_dept_name AS
# SELECT de.emp_no, de.dept_no, d.dept_name
# FROM departments AS d
# JOIN dept_emp AS de ON
# de.dept_no = d.dept_no;
# 
# SELECT * FROM emp_dept_name;
# 
# SELECT e.emp_no, e.last_name, e.first_name, edn.dept_name
# FROM emp_dept_name AS edn
# JOIN employees AS e ON
# e.emp_no = edn.emp_no;
# 
# -- list the first name, last name, and sex for employees
# -- whose first name is "Hercules" and last name begins with "B"
# SELECT first_name, last_name, sex
# FROM employees
# WHERE first_name = 'Hercules'
# AND last_name LIKE 'B%';
# 
# -- list all employees in the sales department, including:
# -- employee number, last name, first name, department name
# SELECT e.emp_no, e.last_name, e.first_name, edn.dept_name
# FROM emp_dept_name AS edn
# JOIN employees AS e ON
# e.emp_no = edn.emp_no
# WHERE dept_name = 'Sales';
# 
# -- list all employees in the sales and development departments, including:
# -- employee number, last name, first name, and department name
# SELECT e.emp_no, e.last_name, e.first_name, edn.dept_name
# FROM emp_dept_name AS edn
# JOIN employees AS e ON
# e.emp_no = edn.emp_no
# WHERE dept_name = 'Sales'
# OR dept_name = 'Development';
# 
# -- in descending order, list the frequency count of employee last names
# -- i.e., how many employees share each last name
# SELECT last_name, COUNT(last_name) AS "name_counts"
# FROM employees
# GROUP BY last_name
# ORDER BY "name_counts" DESC;
# 
# ```

# ## QuickDB Code

# In[ ]:


titles
-
title_id VARCHAR(10) PK
title VARCHAR(50)


employees
-
emp_no INT PK
emp_title_id VARCHAR(10) FK >- titles.title_id
birth_date VARCHAR(20)
first_name VARCHAR(20)
last_name VARCHAR(20)
sex VARCHAR(10)
hire_date VARCHAR(20)


departments
-
dept_no VARCHAR(10) PK
dept_name VARCHAR(50)


dept_emp
-
emp_no INT FK - employees.emp_no
dept_no VARCHAR(10) FK >- departments.dept_no


dept_manager
-
dept_no VARCHAR(10) FK >- departments.dept_no
emp_no INT FK - employees.emp_no


salaries
-
emp_no INT PK FK - employees.emp_no
salary INT


# ## Table Schema
# ``` mysql
# CREATE TABLE titles(
#     title_id VARCHAR(10) PRIMARY KEY,
#     title VARCHAR(50)
# );
# 
# CREATE TABLE employees(
#     emp_no INT PRIMARY KEY,
#     emp_title_id VARCHAR(10),
#     birth_date VARCHAR(20),
#     first_name VARCHAR(20),
#     last_name VARCHAR(20),
#     sex VARCHAR(10),
#     hire_date VARCHAR(20),
#     FOREIGN KEY (emp_title_id) REFERENCES titles(title_id)
# );
# 
# CREATE TABLE departments(
#     dept_no VARCHAR(10) PRIMARY KEY,
#     dept_name VARCHAR(50)
# );
# 
# CREATE TABLE dept_emp(
#     emp_no INT,
#     dept_no VARCHAR(10),
#     FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
#     FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
# );
# 
# CREATE TABLE dept_manager(
#     dept_no VARCHAR(10),
#     emp_no INT,
#     FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
#     FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
# );
# 
# CREATE TABLE salaries(
#     emp_no INT,
#     salary INT,
#     FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
# );
# ```

# ## Visualization

# In[ ]:


get_ipython().system('pip install psycopg2')


# In[1]:


# import the SQL database
from sqlalchemy import create_engine

engine = create_engine(f"postgresql://postgres:TunaFish10@localhost:5432/SQL_challenge")
connection = engine.connect()


# In[2]:


# dependencies
import pandas as pd

# import the database's tables as dataframes
employees = pd.read_sql("SELECT * FROM employees", connection)
titles = pd.read_sql("SELECT * FROM titles", connection)
salaries = pd.read_sql("SELECT * FROM salaries", connection)


# In[15]:


# merge the salary and employee tables
employee_master = pd.merge(employees,salaries,on="emp_no")
employee_master = employee_salaries.rename(columns={"emp_title_id":"title_id"})
employee_master


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




