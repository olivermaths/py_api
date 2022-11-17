from rest_framework.response import Response
from rest_framework.decorators import api_view
from decision_tree.utils import *
from decision_tree.classify import *
import decision_tree.constants as consts 
from data.firebase_settings import *
from decision_tree.start_tree import *

@api_view(['GET'])
def getData(request):
    person = {"Hello": "Bem vindo a API :))))"}
    return Response(person)

@api_view(['POST'])
def getResult(request):
    unhadle_data = request.data
    data = handle_data(consts.header, unhadle_data)
    if consts.const_decision_tree == None:
        consts.const_decision_tree = train_decision_tree()
    classification = classify(data, consts.const_decision_tree)
    percent = print_leaf(classification)
    return Response({"ok": percent})

