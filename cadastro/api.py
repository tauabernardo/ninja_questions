from ninja import Schema, NinjaAPI
from .models import Question
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class QuestionInput(Schema):
    questao: str
    resposta: str
    materia: str
    erro: str

class QuestionSchema(Schema):
    id: int
    questao: str
    resposta: str
    materia: str
    erro: str

@api.get("/questions", response=list[QuestionSchema])
def listar(request):
    question = Question.objects.all()
    return [model_to_dict(q) for q in question]

@api.get("/questions/{id}", response=QuestionSchema)
def listar_questao(request, id: int):
    questao = get_object_or_404(Question, id=id)
    return model_to_dict(questao)

@api.post("/questions", response=QuestionSchema)
def questao_criar(request, body: QuestionInput):
    q = Question.objects.create(**body.dict())
    return model_to_dict(q)

