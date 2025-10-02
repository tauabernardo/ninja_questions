from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/questions")
def get_questions(request):
    return 1
