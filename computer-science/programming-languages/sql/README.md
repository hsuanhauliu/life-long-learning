# SQL

Follow this [SQL style guide](https://www.sqlstyle.guide/) to follow SQL conventions

Database creation pipeline:
Create a database -> create tables -> fill-in values.

## Common Commands
```
/* Create a new database */
CREATE DATABASE database_name;

/* Delete an existing database */
DROP DATABASE database_name;

/* Create a new table */
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);

/*  Delete a table */
DROP TABLE table_name;

/* Element Constraints */
/* Create a new table */
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
   ....
);


/********************************/
/* ADD: add a column to a table */
ALTER TABLE Customers
ADD Email varchar(255);

/*  */

/*  */

/*  */

/*  */

/*  */
```

Reference: https://www.w3schools.com/sql/sql_examples.asp

## Datatypes
Every element in the database table has a specific type (defined when the column that it belongs to was created).
- Numerical:
  - int
  - float
  - decimal, bit, tinybit, real, bigint,smallint, numeric...
- Characters:
  - char
  - varchar
  - text
- Date/time:
  - date
  - time
  - datetime
  - timestamp
  - year
- Binary:
  - binary
  - varbinary, image...
- Unicode Characters/String:
  - NChar
  - NVarchar
  - NText
- Miscellaneous:
  - Clob, Blob, XML, JSON...

Reference: https://www.journaldev.com/16774/sql-data-types

## Constraints
Constraints are used when creating a table to restrict the elements when inserting and modifying.

- NOT NULL: Ensures that a column cannot have a NULL value
- UNIQUE: Ensures that all values in a column are different
- PRIMARY KEY: A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
- FOREIGN KEY: Uniquely identifies a row/record in another table
- CHECK: Ensures that all values in a column satisfies a specific condition
- DEFAULT: Sets a default value for a column when no value is specified
- INDEX: Used to create and retrieve data from the database very quickly
