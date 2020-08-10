#importing the Python Libraries

import matplotlib.pyplot as plt    
import numpy as np

#using linspace method from numpy library to create the range axis
t=np.linspace(-np.pi,np.pi,100)

#plotting the trigometric functions of sine and cosine w.r.t range

#----------------------sine starts------------------------
sinex=np.sin(t)     #sinx
sine2x=np.sin(2*t)  #sin(2x)
sinex_by_2=np.sin(t/2)  #sin(x/2)
#----------------------sine ends------------------------


#----------------------cosine starts------------------------
cosinex=np.cos(t)       #cos(X)
cosine2x=np.cos(2*t)    #cos(2x)
cosinex_by_2=np.cos(t/2) #cos(x/2)

#----------------------cosine ends------------------------

plt.plot(t,sinex,label='Sin(x)' )
plt.plot(t,sine2x,label='Sin(2x)')
plt.plot(t,sinex_by_2,label='Sin(x/2)')


plt.plot(t,cosinex,label='cos(x)')
plt.plot(t,cosine2x,label='cos(2x)')
plt.plot(t,cosinex_by_2,label='cos(x/2)')

plt.axhline(color='black')  #centre y-axis
plt.axvline(color='black')  #centre x-axis
# plt.axis('off')   #elemenating the outer ref axis

plt.title('Sine and Cosine Functions')
plt.xlabel('Range/Time')
plt.ylabel('Value')


plt.legend(loc=4,ncol=4)    #plotting the legends/names of curves
plt.show()  #displaying the plot

