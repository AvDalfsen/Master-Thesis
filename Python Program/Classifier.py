# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:26:10 2018

@author: Anne van Dalfsen
"""

#import numpy as np
import pandas as pd
from sklearn.metrics import classification_report

dataset = pd.read_csv('ClassifierData/data_words.csv')

x = dataset.iloc[:,3:].values
y = dataset.iloc[:,0].values

#x_train = dataset.iloc[np.r_[0:31,44:63,71:83,88:100,105:130,141:178,189:242,264:285,294:350,374:394,403:420,427:431,433:453,462:482,491:497], 3:].values
#x_test = dataset.iloc[np.r_[31:44,63:71,83:88,100:105,130:141,178:189,242:264,285:294,350:374,394:403,420:427,431:433,453:462,482:491,497:500], 3:].values
#y_train = dataset.iloc[np.r_[0:31,44:63,71:83,88:100,105:130,141:178,189:242,264:285,294:350,374:394,403:420,427:431,433:453,462:482,491:497], 1].values
#y_test = dataset.iloc[np.r_[31:44,63:71,83:88,100:105,130:141,178:189,242:264,285:294,350:374,394:403,420:427,431:433,453:462,482:491,497:500], 1].values

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 1613)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

sns.heatmap(cm.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=['press_rep', 'press_ed', 'press_rev', 'religion','skill_hob', 'pop_lore','bel_bio_mem','misc','learned','gen_fic','mys_det','sci_fi','adv_west','rom_love','humor'], yticklabels=['press_rep', 'press_ed', 'press_rev', 'religion','skill_hob', 'pop_lore','bel_bio_mem','misc','learned','gen_fic','mys_det','sci_fi','adv_west','rom_love','humor'])
#sns.heatmap(cm.T, square=True, annot=True, fmt='d', cbar=False, xticklabels = ['non fiction', 'fiction'], yticklabels = ['non-fiction', 'fiction'])
plt.xlabel('true label')
plt.ylabel('predicted label')

print(classification_report(y_test, y_pred))