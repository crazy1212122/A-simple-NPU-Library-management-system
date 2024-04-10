# A-simple-NPU-Library-management-system
This is a easy Library management system in Python and  MySQL, and it's interaction interface is designed by PyQt5.

The work is finished together with **Zhang chao** and **Zhao yunji**.

## Environment Requirements

Python >= 3.8.8

PyQt5 >= 5.15.10

PyMySQL >= 1.1.0

Pandas >= 1.2.4

The MySQL version is MySQL8.0

## How to use

1. First, you need to modify connect.py to the relevant information of the database used by this machine so that it can be connected correctly.
2. Use the terminal to open the library management system folder and enter python zhuhanshu.py to run.
3. Enter the account password and select the corresponding identity to proceed to the next step (you can find the required account password in the database).
4. When borrowing books, please fill in the information correctly and completely.
5. When returning a book, you need to correctly enter the book number (ISBN number) of the borrowed book.

We've provide a basic sql file named npulib.sql. 
