#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 3 "juego de la vida (parte 1)" del Módulo 5 (esqueleto inicial)

FILAS = 0
COLUMNAS = 0
tablero_texto = """\
11100000000000000000000000000000000000000000000000000000000000000000000000000000
00000000110000000000000000011100000011100000000000000000000000000000000000000000
00000001001000000000000000000000010000000000000000000000000000000000000000000000
00000000110000000000000000000000010000000000000000000000000000000000000000000000
00000000000000000000000000000000010000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000110000000000000000000000000000000010000000000000000000000000000000
00000000000000110000000000000000000000000000001010000000000000000000000000000000
00000000000000001100000000000000000000000000000110000000000000000000000000000000
00000000000000001100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000110000000000000000000000000000000
00000000000000000000000000000000000000000000001100000000000000000000000000000000
00000000000000000000000000000000000000000000000100000000000000000000000000000000
"""

def leer_tablero(tablero_cadena):
    """Convierte una cadena adecuada en una matriz, para operar mejor con ella"""
    i = 0
    l = []  # Una lista para ir generando una fila
    m = []  # La matriz resultado
    global FILAS, COLUMNAS
    for celda in tablero_cadena:
        if celda == '\n':
            if COLUMNAS == 0:
                COLUMNAS = len(l)
            elif COLUMNAS != len(l):
                print(f"Error en la fila {FILAS}, faltan o sobran datos!")
                exit(1)
            FILAS = FILAS + 1
            m.append(l)
            l = []
        else:
            # Por si acaso se usa algo distinto de 1's, lo aceptamos igual
            valor = 0 if celda == "0" else 1
            l.append(valor)

    return m



def print_tablero(m):
    """Escribe por pantalla la matriz m con formato de tablero de 0's y 1's"""
    print(str(m).replace(",", "").replace(" ", "").replace("[", "").replace("]","\n"))

def num_vecinos(m, x, y):
    """Devuelve el número de vecinos de la celda m[y][x], como un valor de 0 a 8"""
    vecinos=0
    i=0
    while i<3:
        if m[y-1][x-1+i] ==True:
            vecinos=vecinos+1
        i+=1
    i=0
    if m[y][x-1] ==True:
            vecinos=vecinos+1
    if m[y][x+1] ==True:
            vecinos=vecinos+1
    while i<3:
        if m[y+1][x-1+i] ==True:
            vecinos=vecinos+1
        i+=1
    return vecinos

# Comienzo del programa
m = leer_tablero(tablero_texto)
print("Tablero inicial:")
print_tablero(m)
print(num_vecinos(m,1,0))

