import numpy as np
from bokeh.models import Slider, ColumnDataSource, CustomJS
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.layouts import row, column

#import matplotlib.pyplot as plt

ilosckrok=300
S=np.zeros(ilosckrok)
I=np.zeros(ilosckrok)
R=np.zeros(ilosckrok)
x=np.linspace(0,100,ilosckrok)
S[0]=997
I[0]=3
N=1000
gamma=0.05
beta=0.4

for i in range (1,ilosckrok):
    S[i]=S[i-1]-beta*I[i-1]*S[i-1]/N
    I[i]=I[i-1]+beta*I[i-1]*S[i-1]/N-gamma*I[i-1]
    R[i]=R[i-1]+gamma*I[i-1]
data={'x_values':x,'S_values':S,'I_values':I,'R_values':R}
source=ColumnDataSource(data=data)
fig=figure(width=400, aspect_ratio=1)
fig.line('x_values','S_values',source=source,color='blue',legend_label='S')
fig.line('x_values','I_values',source=source,color='red',legend_label='I')
fig.line('x_values','R_values',source=source,color='green',legend_label='R')
def update_b(attrname, old, new):
    ilosckrok=300
    S=np.zeros(ilosckrok)
    I=np.zeros(ilosckrok)
    R=np.zeros(ilosckrok)
    x=np.linspace(0,100,ilosckrok)
    S[0]=997
    I[0]=3
    N=1000
    beta=new
    for i in range (1,ilosckrok):
        S[i]=S[i-1]-beta*I[i-1]*S[i-1]/N
        I[i]=I[i-1]+beta*I[i-1]*S[i-1]/N-gamma*I[i-1]
        R[i]=R[i-1]+gamma*I[i-1]
    source.data['S_values']=S
    source.data['I_values']=I
    source.data['R_values']=R
def update_g(attrname, old, new):
    ilosckrok=300
    S=np.zeros(ilosckrok)
    I=np.zeros(ilosckrok)
    R=np.zeros(ilosckrok)
    x=np.linspace(0,100,ilosckrok)
    S[0]=997
    I[0]=3
    N=1000
    gamma=new
    for i in range (1,ilosckrok):
        S[i]=S[i-1]-beta*I[i-1]*S[i-1]/N
        I[i]=I[i-1]+beta*I[i-1]*S[i-1]/N-gamma*I[i-1]
        R[i]=R[i-1]+gamma*I[i-1]
    source.data['S_values']=S
    source.data['I_values']=I
    source.data['R_values']=R

s_gamma=Slider(start=0.02,end=0.1,step=0.01,value=0.05,title='gamma',sizing_mode='stretch_width')
s_beta=Slider(start=0.1,end=1,step=0.01,value=0.4,title='beta',sizing_mode='stretch_width')
s_gamma.on_change('value',update_g)
s_beta.on_change('value',update_b)
layout=row(s_beta,s_gamma,fig)
curdoc().add_root(layout)
