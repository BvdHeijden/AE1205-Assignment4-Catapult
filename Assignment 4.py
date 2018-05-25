# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:46:56 2018

@author: vdhei
"""
from numpy import sin,cos,arctan,pi,sqrt,radians

m=90.
rho_rock=1600.
rho_air=1.225
Cd=0.7
R=3.0
L0=0.5
Ke=5000.
g=9.80665
v_init=0.

dt=0.001

phi_start=0.
phi_stop=60.


phi_start=radians(phi_start)
phi_stop=radians(phi_stop)

t=0
phi=phi_start
v_tang=v_init


while phi<phi_stop:
    x_cat=R*cos(phi)
    y_cat=R*sin(phi)
    
    L_elas=sqrt(x_cat**2+(R-y_cat)**2)
    
    theta=arctan((R-y_cat)/x_cat)
    
    Fg=m*g
    
    F_elas=Ke*(L_elas-L0)
    
    a_tang=F_elas/cos(pi/2-theta-phi)-Fg*cos(phi)
    v_tang=v_tang+a_tang*dt
    
    
    t+=dt
    
