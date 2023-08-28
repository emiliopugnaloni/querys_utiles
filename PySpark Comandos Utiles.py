

#GUARDAR CSV EN EL HDFS

	# Replace with your keytab and principal
	spark.conf.set("spark.yarn.keytab", "epugnalo.keytab")
	spark.conf.set("spark.yarn.principal", "epugnalo@TASA.COM")

	 
	# Replace with your DataFrame and output path
	df_sample.coalesce(1).write.format("csv") \
	  .option("header", "true") \
	  .option("delimiter", "|") \
	  .option("nullValue", "") \
	  .mode("overwrite") \
	  .save("hdfs://hdpvelez/user/epugnalo/files-view/your_big_file.csv")