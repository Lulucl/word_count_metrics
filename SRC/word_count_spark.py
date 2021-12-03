import pyspark

# initialisation du spark context
configuration = pyspark.SparkConf().setMaster("local[*]").setAppName("word_count_metrics")
sc = pyspark.SparkContext(conf = configuration)

# ouverture du fichier texte 
words = sc.textFile("./../DATA/fichier_texte.txt").flatMap(lambda line: line.split(" "))

# on compte le nombre de mots
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

# sauvegarde dans le dossier output
wordCounts.saveAsTextFile("./../OUTPUT/output_spark/")