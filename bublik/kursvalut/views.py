from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def currency_conversion(request):
    currency_original = request.GET.get("currency_original")
    currency_required = request.GET.get("currency_required")
    quantity = request.GET.get("quantity")
    return HttpResponse(f"исходная: {currency_original} требуемая: {currency_required} количество {quantity} </h2>")


# Create your views here.
