
# Panorbit Machine test

## Installation


1. Create an Virtual environment `python -m venv env`
2. Activate environment `source env/bin/activate`
3. Clone the repository.
4. Run `pip install -r requirements.txt`.
5. Enter postgres terminal using `sudo -u postgres psql`
6. Create database using `CREATE DATABASE db_panorbit1`
7. Create database User `CREATE USER alwin WITH PASSWORD '1234'`;


8. Alter Role `ALTER ROLE alwin SET client_encoding TO 'utf8';`

`ALTER ROLE alwin SET default_transaction_isolation TO 'read committed';`

`ALTER ROLE alwin SET timezone TO 'UTC';`

9. Grant Permission `GRANT ALL PRIVILEGES ON DATABASE db_panorbit1 TO alwin;`

10. Exit from psql `\q`

11.Open terminal to the cloned directory

12. Upon activating the env `python manage.py makemigrations`

13. Make sure the columns of table are ordered with the same order in the models.py of the country app.(If any changes are encountered make changes accordingly in the 0001migration file before running the next command).``

14. Migrate table `python manage.py migrate`

15. Enter into db_panorbit1 database using `sudo -u postgres psql` and `\c db_panorbit1`


16. To Insert all the datas, paste all the values in new_world.sql in the psql terminal
 
17. Run the app using `python manage.py runserver` upon activating env

## Note

I have made changes in the  world.sql file by changing table name and adding a new field id(primary key) as no unique element were given in the countrylanguage table ,inorder to make a smooth run for the ORM queries.
