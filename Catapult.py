# -*- coding: utf-8 -*-

from numpy import sin,cos,arctan,pi,sqrt,radians

def Catapult(m,rho_rock,rho_air,Cd,R,L0,Ke,g,v_init,dt,phi_start,phi_stop):
    
    s=pi*((3*m)/(4*pi*rho_rock))**(2/3)
    
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
    theta_tab=[(pi/2)-phi_start]
    
    #loop for launch phase
    while phi_tab[-1]<phi_stop:
        t=t_tab[-1]
        x=x_tab[-1]
        y=y_tab[-1]
        v=v_tab[-1]
        phi=phi_tab[-1]
        
        L_elas=sqrt((-x)**2+(R-y)**2)
        alpha=arctan((R-y)/(-x))
        beta=(pi/2)-alpha-phi
        
        F_g=m*g*cos(phi)
        F_elas=cos(beta)*Ke*max(0,L_elas-L0)
        
        a_tang=(F_elas-F_g)/m
        v_tang=v+a_tang*dt
        phi=phi+(v_tang*dt/R)
        
        t_tab.append(t+dt)
        x_tab.append(-R*cos(phi))
        y_tab.append(R*sin(phi))
        v_tab.append(v_tang)
        a_tab.append(a_tang)
        phi_tab.append(phi)
        theta_tab.append((pi/2)-phi)
        
    
    #loop for ballistic phase
    while y_tab[-1]>0:
        t=t_tab[-1]
        x=x_tab[-1]
        y=y_tab[-1]
        v=v_tab[-1]
        theta=theta_tab[-1]
        
        vx=v*cos(theta)
        vy=v*sin(theta)
        
        F_d=Cd*.5*rho_air*(v**2)*s
        F_d_x=F_d*cos(theta+pi)
        F_d_y=F_d*sin(theta+pi)
        
        
        F_g=m*g
        
        ax=(F_d_x)/m
        ay=(F_d_y-F_g)/m
        
        vx=vx+ax*dt
        vy=vy+ay*dt    
        x=x+vx*dt
        y=y+vy*dt
        
        t_tab.append(t+dt)
        x_tab.append(x)
        y_tab.append(y)
        v_tab.append(sqrt(vx**2+vy**2))
        a_tab.append(sqrt(ax**2+ay**2))
        theta_tab.append(arctan(vy/vx))
        
    theta_tab=[i*(180/pi) for i in theta_tab]
    
    return t_tab,x_tab,y_tab,v_tab,theta_tab,a_tab


    