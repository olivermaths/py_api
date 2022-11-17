import csv
from decision_tree.decision_tree import *


def handle_data(header, data):
    handled_data = []
    if type(data) is list:
        for patient in data:
            row = []    
            [row.append(patient.get(key)) for key in header if patient.get(key) != None]
            handled_data.append(row)
    else:
        [handled_data.append(data.get(key)) for key in header if data.get(key) != None]
    
    return handled_data

def print_leaf(counts):
    total = sum(counts.values())*1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    result = {}
    print(probs)
    if probs.get('Y') != None:
        result["Teste"] = "Positivo"
        result["Resultado: "] = "Paciente tem problemas cardiacos"
        result["Certeza"] = probs.get('Y')
    else:
        result["Teste"] = "Negativo"
        result["Resultado: "] = "Paciente não apresenta problemas cardiacos"
        result["Certeza"] = probs.get('N')
    return result
