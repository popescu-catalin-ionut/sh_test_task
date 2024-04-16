# sh_test_task

unfortunately I couldn't touch as much as I wanted.

# Requirements

* python 3.11
* Java 11 - JRE (WIP - Both of Java 8 or 11 did not pass samba error)
  (typeerror: class com.simba.spark.jdbc.driver is not found)
* Oracle account for download java
* python requirements ```pip install -r requirements```
* https://www.elephantsql.com/ account
* databricks account
* Microsoft/google/amazon account with cloud activated
* https://github.com account

# Local run

For local running use

```py 
python main.py
```

# Structure

* In ```databricks-jdbc``` you can find databricks jar used as jdbc
* In ```v1``` there are files for v1
* In ```common``` you can find files that are common to this solution
* Folder ```_databricks_integration_tests_junk``` is a temp folder that is used for
  testing databricks connection. I've pushed the CSV into databricks, but I could not 
  connect from local (because I don't have paid cloud, I cannot see in databricks 
  token creation section - I cannot use pandas/ with Java I encountered issues)