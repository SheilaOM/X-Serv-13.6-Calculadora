#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
    sys.exit("Usage: python3 calculadora.py operacion operando1 operando2")

_, operacion, operando1, operando2 = sys.argv

try:
    operando1 = float(operando1)
    operando2 = float(operando2)
except ValueError:
    sys.exit("Los operandos deben ser numeros")

if (operacion == "suma"):
    print(float(operando1) + float(operando2))
elif (operacion == "resta"):
    print(float(operando1) - float(operando2))
elif (operacion == "multi"):
    print(float(operando1) * float(operando2))
elif (operacion == "div"):
    try:
        print(float(operando1) / float(operando2))
    except ZeroDivisionError:
        print("Error, no dividir entre 0")
else:
    print("Introducir las siguientes operaciones:\nsuma, resta, multi o div")
