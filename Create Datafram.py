# Databricks notebook source
df=spark.range(1,100)
df.write.mode('overwrite').saveAsTable('databricks281194.bronze.testing123')
