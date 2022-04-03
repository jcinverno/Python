# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:36:28 2021

@author: jcinv
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def soma ():
    #Soma o valor posto dentro da máquina
    quarters = int(input ('How many quarters?: '))
    dimes = int (input ('How many dimes?: '))
    nickles = int (input('How many nickles?: ' ))
    pennies = int(input('How many pennies?: '))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies 
    return total

def pedir(pedido):
    # vai ao menu buscar os ingredientes e o preco
    pedir = MENU[pedido]
    custo = pedir["cost"]
    ingredientes = pedir["ingredients"]
    ingredientes_e_custo = []
    ingredientes_e_custo = [ingredientes, custo]
    return ingredientes_e_custo

def comparar(dado, preço):
    #comparar e diz que valor é mais alto
    if dado < preço:
        avancar = False
    else:
        avancar = True
    return avancar

def ingrediente(ing_e_custo):
    #vê se ha ingredientes disponiveis
    #retorna ou true ou ingredientes em falta
    ing= ing_e_custo[0]
    agua = ing["water"]
    leite = ing["milk"]
    cafe = ing["coffee"]
    aguam = resources["water"]
    leitem = resources["milk"]
    cafem = resources ["coffee"]
    falta = []
    if agua < aguam:
        falta.append('water')
    if leite < leitem:
        falta.append('milk')
    if cafe < cafem:
        falta.append('coffee')
    if agua < aguam and cafe < cafem and leite < leitem:
        resources["water"] = int(aguam) - int(agua)
        resources["milk"] = int(leitem) - int(leite)
        resources ["coffee"] = int(cafem) - int(cafe)
        falta = True
    return falta
            
def dinheiro(preco, d):
    #adiciona o valor do cappuccino
    d += preco
    din = str(d)
    return din
    
def vdd(pedido):
    
    if pedido == 'espresso':
        p = True

    elif pedido == 'latte':
        p = True

    elif pedido == 'cappuccino':
        p = True

    elif pedido == 'report':
        p ='re'
    return p



machine = True
d = 0

while machine == True:
    
    pedido = input ('What would you like? (espresso/latte/cappuccino): ').lower()
    valo = vdd(pedido) 
    
    if valo == True:    
        ing_e_custo = pedir(pedido)
        ingredient = ingrediente(ing_e_custo)
        
        if ingredient == True:
            
            preco = int(ing_e_custo[1])
            dado = soma()
            suficiente = comparar (dado, preco)
            
            if suficiente == 0:
                print (f' Here is your {pedido}. Enjoy!')
                resources["money"] = dinheiro(preco, d)
                
            elif suficiente > 0:
                troco = round(dado - suficiente, 2)
                print (f' Here is your {pedido}. Your change is {troco}. Enjoy!')
                resources["money"] = dinheiro(preco, d)
                
            else:
                print (' Sorry that is not enough money. Return money.')
        else:
            i = ingrediente(ing_e_custo)
            d = ''
            for e in i:
                d = d + e +' '
            print (f' Sorry there is not enough {d}.')
            
    elif valo == 're' :
        w = resources['water'] 
        m = resources['milk'] 
        c = resources['coffee'] 
        p = resources['money']
        
        print(f' Water: {w}mL \n Milk: {m}mL \n Coffee: {c}g \n Money: {p}$')
    

    else:
        
        machine = False