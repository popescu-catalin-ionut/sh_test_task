import jaydebeapi

jdbc_driver = "v-jdbc/DatabricksJDBC42.jar"
jdbc_url = "jdbc:databricks:sql://community.cloud.databricks.com/?o=1747392662590981#folder/3273203243887561"
user = "popescu.catalin.ionut@gmail.com"
password = "A Random password1!"

# Establish JDBC connection
conn = jaydebeapi.connect("com.simba.spark.jdbc.Driver",
                          jdbc_url,
                          {"user": user, "password": password},
                          jdbc_driver)

# Create a cursor
cursor = conn.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM games")

# Fetch results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()