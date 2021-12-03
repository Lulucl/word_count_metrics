import pandas as pd
import numpy as np
from collections import Counter
 
# lecture du fichier texte et sauvegarde dans une dataframe
df = pd.read_fwf("./../DATA/fichier_texte.txt",header = None)

# creation d'une nouvelle dataframe avec une colonne words qui contient tou les mots
new_df = df.assign(words = '')
for x in df :
    new_df['words'] = new_df['words'] + " " + df[x]

# on compte le nombre de mots dans la colonne words de la nouvelle dataframe
wd = pd.DataFrame(new_df.words.str.split(expand = True).stack().value_counts())

# sauvegarde des resultats dans un fichier texte
wd.to_csv("./../OUTPUT/output_panda.txt", sep ='\t', header = False)