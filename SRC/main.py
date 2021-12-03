import pyspark
import time
import os 

start=time.time()

os.system("spark-submit word_count_spark.py")
end1 = time.time()

os.system("spark-submit word_count_panda.py")
end2 = time.time()

exec(open("word_count_panda.py").read())
end3 = time.time()

print("On compte le nombre d'occurence de chaque mot dans un texte donnee : ")
print("On compare le temps de calcul entre un programme spark et une programme panda ")
print("Temps de calcul du programme avec spark :",abs(end1-start))
print("Temps de calcul du programme avec panda lancer avec spark :",abs(end2-end1))
print("Temps de calcul du programme avec panda lancer avec python :",abs(end3-end2))
