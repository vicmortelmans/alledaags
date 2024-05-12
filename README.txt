source env/bin/activate

mariadb:
 - sudo apt install mariadb (that should come with loading the requirements.txt as well)
 - install MariaDB Connector/C from the CS Package Repository:
https://mariadb.com/docs/server/connect/programming-languages/c/install/#CS_Package_Repository
 - pip install mariadb
 - sudo mariadb
   > CREATE DATABASE alledaags
   > CREATE USER alledaags@localhost IDENTIFIED BY 'geloven';
   > GRANT ALL PRIVILEGES ON alledaags.* TO alledaags@localhost;
 - python reset_database.py
 
to check:
 - sudo mariadb
   > use alledaags
   > describe cache;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| key   | varchar(128) | NO   | PRI | NULL    |       |
| json  | longblob     | YES  |     | NULL    |       |
| image | longblob     | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
   > describe historical;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| hash  | varchar(128) | NO   | PRI | NULL    |       |
| data  | blob         | NO   |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
   > describe dailyfeed;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| key         | varchar(128) | NO   | PRI | NULL    |       |
| day         | varchar(128) | NO   |     | NULL    |       |
| title       | varchar(128) | NO   |     | NULL    |       |
| description | varchar(128) | NO   |     | NULL    |       |
| url         | varchar(128) | NO   |     | NULL    |       |
| image_url   | varchar(128) | NO   |     | NULL    |       |
| pubDate     | varchar(128) | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
   > pager less -S
   > select * from cache; 
   > select cache.key,left(cache.json,50),right(cache.json,50) from cache; 

SERVER=http://localhost python alledaags.py
SERVER=http://localhost gunicorn --bind 0.0.0.0:8080 wsgi:app

Installed a new module?

(env) $ pip freeze > requirements.txt

Once a collaborator pulls down your project - they can then install a fresh python environment:

$ python3 -m venv local_python_environment

And then activate that environment and install from your requirements.txt which you have included in your version control:

$ source local_python_environment/bin/activate

(local_python_environment) $ pip install -r requirements.txt

