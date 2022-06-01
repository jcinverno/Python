# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:06:12 2021

@author: jcinv
"""

"""
#usado para extrair as cores do desenho 
#foi criada uma lista que se chamou cores

import colorgram

colors = colorgram.extract('C:/Users/jcinv/OneDrive/Ambiente de Trabalho/image1.jpg', 20)

color = []
lista = []

for e in range(len(colors)):

    first_color = colors[e]
    color.append(first_color.rgb)
    t = (color[e][0], color[e][1], color[e][2])
    lista.append(t)

print (lista)
"""

cores = [(234, 229, 231), (236, 35, 108), (222, 231, 237), 
         (145, 28, 65), (239, 74, 34), (6, 148, 93), (232, 168, 40),
         (184, 158, 46), (44, 191, 233), (27, 127, 195),
         (126, 193, 74), (253, 223, 0), (85, 28, 93), (172, 36, 98),
         (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]

#bolas com cores
#10 by 10 
#20 de diametro
#separados por 50


from turtle import Turtle
from random import choice
from turtle import Screen
import turtle 

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.pencolor(choice(cores))

def line():
    
    for e in range(9):
        
        tim.pendown()
        tim.dot(20, choice(cores))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20, choice(cores))


def virar_esquerda():
    
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    

def virar_direita():
    
    tim.penup()
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    

def andar():

    line()
    virar_esquerda()
    line()
    virar_direita()


tim.penup()
tim.forward(-200)
tim.right(90)
tim.forward(200)
tim.left(90)
tim.pendown()
tim.dot(20, choice(cores))
for e in range(5):
   
    andar()


tim.hideturtle()
screen = Screen()
screen.exitonclick()














