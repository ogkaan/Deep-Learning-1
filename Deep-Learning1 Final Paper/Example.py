#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


# In[2]:


x = [1, 4, 3, 8, 4, 9]
y = [2, 5, 3.2, 8, 5.7, 11]

plt.scatter(x,y)
plt.show()


# In[3]:


X = np.array([[1, 2],
              [4, 5],
              [3, 3.2],
              [8, 8],
              [4, 5.7],
              [9, 11]])


# In[4]:


kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)


# In[5]:


colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
		


# In[ ]:





# In[ ]:




