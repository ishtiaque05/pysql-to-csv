### To install the plugin from master branch

`pip install git+https://github.com/ishtiaque05/pysql-to-csv.git-master` 

### To clone and install locally
cd into the repo directory:

`pip install -e .`

### To convert a dump sql file to csv

Run the following command 

`dump-to-csv target_file_name.sql`

### To convert an sql table by connecting to mysql database

`pysql-to-csv hostname user password databasename tablename`
