# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from Catapult import Catapult

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

#Call Catapult algorithm from Catapult.py
t,x,y,v,theta,a=Catapult(m,rho_rock,rho_air,Cd,R,L0,Ke,g,v_init,dt,phi_start,phi_stop)

plt.plot(x,y)