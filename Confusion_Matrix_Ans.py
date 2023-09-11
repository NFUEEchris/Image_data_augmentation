import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
a=np.array(([0.99,0,0],[0,1,0],[0.01,0,0.97]))
sns.heatmap(a,annot=True,ax=ax,cmap='Blues')
plt.show()

