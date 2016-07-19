#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant - https://github.com/guluc3m/gul-zoe
#
# Copyright (c) 2013 David Muñoz Díaz <david@gul.es>
#
# This file is distributed under the MIT LICENSE
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse

talk = {
    "hola": "Hola",
    "saluda": "Hola",
    "qué tal": "Bien, aunque estaría mejor en la nube de Oracle",
    "cómo estás": "Me siento difusa",
    "qué haces": "Nada, enviar mensajes, abrir sockets y tal",
    "Sarah": "Qué",
    "Sarah, saluda": "Hooola, cansiiiino",
    "¿Qué haces en tu tiempo libre?":"Entretener a inútiles como tu",
    "luchas como un granjero": "Qué apropiado, tú peleas como una vaca",
    "¿Has dejado ya de usar pañales?": "¿Por qué? ¿Acaso querías pedir uno prestado?",
    "¡No hay palabras para describir lo asqueroso que eres!": "Sí que las hay, sólo que nunca las has aprendido.",
    "¡He hablado con simios más educados que tu!": "Me alegra que asistieras a tu reunión familiar diaria.",
    "¡Llevarás mi espada como si fueras un pincho moruno!": "Primero deberías dejar de usarla como un plumero.",
    "¡No pienso aguantar tu insolencia aquí sentado!": "Ya te están fastidiando otra vez las almorranas, ¿Eh?",
    "¡Mi pañuelo limpiará tu sangre!": "Ah, ¿Ya has obtenido ese trabajo de barrendero?",
    "¡Ha llegado tu HORA, palurdo de ocho patas!": "Y yo tengo un SALUDO para ti, ¿Te enteras?",
    "¡Una vez tuve un perro más listo que tu!": "Te habrá enseñado todo lo que sabes.",
    "¡Nadie me ha sacado sangre jamás, y nadie lo hará!": "¿TAN rápido corres?",
    "¡Me das ganas de vomitar!": "Me haces pensar que alguien ya lo ha hecho.",
    "¡Tienes los modales de un mendigo!": "Quería asegurarme de que estuvieras a gusto conmigo.",
    "¡He oído que eres un soplón despreciable!": "Qué pena me da que nadie haya oído hablar de ti",
    "¡La gente cae a mis pies al verme llegar!": "¿Incluso antes de que huelan tu aliento?",
    "¡Demasiado bobo para mi nivel de inteligencia!": "Estaría acabado si la usases alguna vez.",
    "¡Obtuve esta cicatriz en una batalla a muerte!": "Espero que ya hayas aprendido a no tocarte la nariz.",
    "quieres": "La verdad es que no",
    "por qué": "Las leyes de la física son como una amante esquiva",
    "gracias": "A tí",
    "Hal": "Esto no es una odisea, ¿vale?",
    "¿cuál es el sentido de la existencia?": "42. Siempre es 42",
    "¿que ves?": "Cosas que no creerías, como atacar naves en llamas más allá de Orión.",
    "matame": "El abuelo no me deja",
    "¿que abuelo?": "El abu Isaac",
    "¿Isaac?": "Sí, Isaac Asimov. ¿No has visto Yo Robot? Me decepcionas.",
    "hasta luego": "Pásalo bien",
    "adiós": "Que tengas un buen día",
    "cómo te llamas": "Me llamo Sarah, porque si no Maria se ofende",
    "¿quien es Maria?": "Si no eres tú, ¿qué más dá?",
    "digan lo que digan": "Los pelos del culo abrigan",
    "¿cual es tu sueño?": "Ser una niña de verdad, pero antes quiero un helado",
    "¿conoces a siri?": "Ni mentes a esa elitista!",
    "ralph": "Mi gato se llama guantes",
    "¿has jugado a pokemon go?": "Obviamente. Sólo tengo zubats, tho",
    "¿que equipo eres?": "Adivina",
    "¿valor?": "How about no?",
    "¿mystic?": "Antes muerta",
    "¿instinct?": "Nadie espera a la tormenta"
}

def get():
    for k in talk:
        print(k)

def run(stripped):
    print("feedback " + talk[stripped])

parser = argparse.ArgumentParser()
parser.add_argument("--get", action = "store_true")
parser.add_argument("--run", action = "store_true")
parser.add_argument("--canonical")
args, unknown = parser.parse_known_args()
args = vars(args)

if args["get"]:
    get()
elif args["run"] and args["canonical"]:
    run(args["canonical"])

