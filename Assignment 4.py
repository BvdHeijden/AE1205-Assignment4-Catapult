# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:46:56 2018

@author: vdhei
"""

import matplotlib.pyplot as plt
from numpy import sin,cos,arctan,pi,sqrt,radians

#Fixed variables
m=90.
rho_rock=1600.
rho_air=1.225
Cd=0.7
R=3.0
L0=0.5
Ke=5000.
g=9.81
v_init=0.
dt=0.001
phi_start=0.
phi_stop=60.

#convert start/stop angles to radians
phi_start=radians(phi_start)
phi_stop=radians(phi_stop)

#initialise output lists
t_tab=[0]
x_tab=[-R*cos(phi_start)]
y_tab=[R*sin(phi_start)]
v_tab=[0]
a_tab=[0]
phi_tab=[phi_start]

#loop for launch phase
while phi_tab[-1]<phi_stop:
    t=t_tab[-1]
    x=x_tab[-1]
    y=y_tab[-1]
    v=v_tab[-1]
    a=a_tab[-1]
    phi=phi_tab[-1]
    
    L_elas=sqrt((-x)**2+(R-y)**2)
    alpha=arctan((R-y)/(-x))
    theta=(pi/2)-alpha-phi
    
    F_g=m*g*cos(phi)
    F_elas=cos(theta)*Ke*max(0,L_elas-L0)
    
    a_tang=(F_elas-F_g)/m
    v_tang=v+a_tang*dt
    phi=phi+(v_tang*dt/R)
    
    t_tab.append(t+dt)
    x_tab.append(-R*cos(phi))
    y_tab.append(R*sin(phi))
    v_tab.append(v_tang)
    a_tab.append(a_tang)
    phi_tab.append(phi)
    
print(v_tab[-1])
plt.plot(t_tab,v_tab)

vx_tab=[v_tab[-1]*sin(phi_stop)]
vy_tab=[v_tab[-1]*cos(phi_stop)]

#while y_tab[-1]>0:
#    t=t_tab[-1]
#    x=x_tab[-1]
#    y=y_tab[-1]
#    vx=vx_tab[-1]
#    vy=vy_tab[-1]
#    
#    theta=arctan(vy/vx)
#    
    