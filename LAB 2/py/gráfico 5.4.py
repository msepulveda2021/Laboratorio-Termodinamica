#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[9]:


t_1= np.array([0,224.3,254.9,304,344.4,382,401.4,446.3])
T_1=np.array([0,9.4,21.6,41.2,57.3,72.2,80,97.9])
t_2=np.array([0,7.7,23.5,48.7,60.9,72.7,88.5,108.3])
T_2=np.array([0,5.2,19.9,32.9,41.4,49.2,59.9,73.3])
t_3=np.array([0,8.5,25.9,84.5,100.3,130.3,145.2,157.5])
T_3=np.array([0,5.5,5.5,7.4,22.4,51,65.2,76.9])


# In[12]:


plt.plot(t_1,T_1, marker=".",color="purple",label="Agua")
plt.plot(t_2,T_2, marker=".",color="c",label="Alcohol")
plt.plot(t_3,T_3, marker=".",color="m",label="Benceno")
plt.xlabel("Tiempo [s]")
plt.ylabel("Temperatura [°C]")
plt.title("Gráfico puntos de ebullición según naturaleza de la sustancia")
plt.legend()
plt.savefig("naturaleza.pdf")


# In[ ]:




