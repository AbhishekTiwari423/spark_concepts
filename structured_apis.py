# Databricks notebook source
# MAGIC %md
# MAGIC ## Chapter-4 : Structured API overview
# MAGIC ## Topics
# MAGIC #### 1.Dataframes 
# MAGIC ###### Distributed data like table with rows and columns .(Untyped API) , basically collection of dataset rows. 
# MAGIC #### 2.Datasets
# MAGIC ###### Typed API, available in JVM language only (Scala, Java)
# MAGIC #### 3.Spark SQL
# MAGIC ###### SQL API for spark
# MAGIC #### 4.Spark execution: 
# MAGIC ##### User code ==> unresolved logical plan ==> resolved logical plan ==> optimized logical plan ===> multiple physical plans ==> most cost efficient physical plan ==> execution with RDD and runtime optimization ==> result return to cluster.
# MAGIC ##### a. User code: 
# MAGIC ###### This is code wriiten by user for spark job
# MAGIC ##### b. unresolved logical plan:
# MAGIC ###### User code first gets converted into unresolved logical plan, its called unresolved logical plan as it is not yet confirmed that the table and columns are available are not.
# MAGIC ##### c. resolved logical plan : 
# MAGIC ###### Spark creates resolved logical plan using catalog after confirming that all tables and columns are available, it can also reject it if its not available.
# MAGIC 
# MAGIC #### 5: Project tungstun and Catalyst optimizer
# MAGIC 
# MAGIC ###### Catalyst optimizer : creates optimized logical plan from analysis of multiple logical plans

# COMMAND ----------

# DBTITLE 1,Dataframe from range of values
df = spark.range(20).toDF("number")
df.display()

# COMMAND ----------

# DBTITLE 1,Addition using spark
df = df.select(df["number"]+ 10)
df.display()

# COMMAND ----------

# DBTITLE 1,Creating rows from dataframe
spark.range(5).collect()
