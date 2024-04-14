# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

# function analysis available here: https://colab.research.google.com/drive/1GnQSIrmojZgFNYE_6WuvlpFv5NE7sX-c

def func_0():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    inflexion_point_x = 2
    
    inflexion_point_y = (inflexion_point_x**3/3)-2*inflexion_point_x**2+3*inflexion_point_x+5/3
    
    label = f"$Concave \ down: \ x \in (-\infty;{inflexion_point_x}) \ \ Concave \ up: \ x \in ({inflexion_point_x};+\infty)$"
    
    title = "$y = (x^3/3)-2*x^2+3*x+5/3$"

    return x, (x**3/3)-2*x**2+3*x+5/3, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}

def func_1():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    label = "$Concave \ down: \ x \in \Re$"
    
    inflexion_point_x = 0
    
    inflexion_point_y = (inflexion_point_x**2)**(1/3)
    
    title = "$y = (x^2)^{1/3}$"
    
    return x, (x**2)**(1/3), label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}

def func_2():
    
    x = np.arange(-10, 5, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None

    inflexion_point_x = -3, 2
    
    label = f"Concave \ up: $(-\infty;{inflexion_point_x[0]}) \cup ({inflexion_point_x[1]};+\infty) \ \ Concave down: ({inflexion_point_x[0]};{inflexion_point_x[1]})$"
    
    inflexion_point_y = inflexion_point_x[0]+36*inflexion_point_x[0]**2-2*inflexion_point_x[0]**3-inflexion_point_x[0]**4,  inflexion_point_x[1]+36*inflexion_point_x[1]**2-2*inflexion_point_x[1]**3-inflexion_point_x[1]**4
    
    title = "$y = x+36x^2-2x^3-x^4$"
    
    return x, x+36*x**2-2*x**3-x**4, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}

def func_3():
    
    x = np.arange(-6, 3, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    inflexion_point_x = None
    
    inflexion_point_y = None
    
    label = "$Concave \ up: \ x \in \Re$"

    title = "$y = (x+1)^4+e^x$"
    
    return x, (x+1)**4+np.exp(x), label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}

def func_4():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    inflexion_point_x = 5/3
    
    inflexion_point_y = inflexion_point_x**3 - 5*inflexion_point_x**2 + 3*inflexion_point_x - 5
    
    label = f"$Concave up: ({inflexion_point_x};+\infty) \ \ Concave \ down: (-\infty;{inflexion_point_x})$"
    
    title = "$y = x^3 - 5x^2 + 3x - 5$"
    
    return x, x**3 - 5*x**2 + 3*x - 5, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}
