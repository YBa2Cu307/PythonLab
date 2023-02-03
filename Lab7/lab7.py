import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
sp.init_printing()

x=sp.Function('x')
w0=sp.Symbol('omega_0',real=True, positive=True)
t=sp.Symbol('t')
x0=sp.Symbol('x_0',real=True)
v0=sp.Symbol('v_0',real=True)
b=sp.Symbol('b',real=True)
w=sp.Symbol('omega',real=True, positive=True)
amp=sp.Symbol('A',real=True, positive=True)

eq=sp.Eq(x(t).diff(t,2)+2*b*x(t).diff(t)+w0**2*x(t),amp*sp.cos(w*t))
sol=sp.dsolve(eq,x(t),ics={x(0):x0,x(t).diff(t).subs(t,0):v0})
solf1=sp.lambdify(t,sol.rhs.subs({x0:60,v0:2,w0:1,b:0,w:0,amp:0}))
solf2=sp.lambdify(t,sol.rhs.subs({x0:20,v0:2,w0:1,b:0.3,w:0,amp:0}))
solf3=sp.lambdify(t,sol.rhs.subs({x0:50,v0:2,w0:1,b:0,w:50,amp:3}))
solf4=sp.lambdify(t,sol.rhs.subs({x0:50,v0:2,w0:1,b:0,w:1.01,amp:30}))
solf5=sp.lambdify(t,sol.rhs.subs({x0:10,v0:2,w0:1,b:0.4,w:1.01,amp:3}))
ts=np.linspace(-10,10,1000)
plt.plot(ts,solf1(ts),label='bez tłumienia i wymuszenia')
plt.plot(ts,solf2(ts),label='bez wymuszenia ale z tłumieniem')
plt.plot(ts,solf3(ts),label='wymuszenie ale bez tłumienia, |w-w0|>>1')
plt.plot(ts,solf4(ts),label='wymuszenie ale bez tłumienia, |w-w0|<<1')
plt.plot(ts,solf5(ts),label='tłumienie i wymuszenie, |w-w0|<<1')
plt.legend()
plt.show()