from ninja import Schema
from ninja import NinjaAPI
from .models import Question
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import HttpRequest  
import orjson
from ninja.parser import Parser


api = NinjaAPI()


@api.get("/questions")
def listar(request):
    question = Question.objects.all()
    response = [{'id': i.id, 
                 'questao': i.questao, 
                 'resposta': i.resposta, 
                 'materia': i.materia, 
                 'erro': i.erro } for i in question]
    print(response)
    return response

@api.get('questions/{id}')
def listar_questao(request, id: int):
    question = get_object_or_404(Question, id=id)
    return model_to_dict(question)

@api.get('question_consulta/')
def listar_consulta(request, id: int):
    question = get_object_or_404(Question, id=id)
    return model_to_dict(question)

class QuestionSchema(Schema):
    questao: str
    resposta: str
    materia: str
    erro: str

