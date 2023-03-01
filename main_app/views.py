from django.shortcuts import render
from django.http import HttpResponse
from .models import Verbiage

# class Verbiage:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, word, language, definition):
#     self.word = word
#     self.language = language
#     self.definition = definition
#
# verbiages = [
#     Verbiage('Kintsugi', 'Japanese', "The art of repairing broken pottery by filling the cracks with gold or silver. It is based on the idea that the broken pieces are part of the object's history and should be celebrated rather than hidden."),
#     Verbiage('Gumusservi', 'Turkish', "The reflection of moonlight on water. It is a poetic term that is used to describe the shimmering, silvery light that can be seen on the surface of water on a moonlit night."),
#     Verbiage('Iktsuarpok', "Inuit", "The feeling of anticipation that makes you keep looking outside to see if anyone is coming. It is often used to describe the feeling of waiting for someone, such as a guest, and checking outside repeatedly to see if they have arrived."),
#     Verbiage('Jayus', "Indonesian", "A joke so poorly told and unfunny that one cannot help but laugh. The term is often used to describe a bad pun or a joke that is so bad it's good."),
#     Verbiage('Eleutheromania', "Greek", "An intense desire for freedom, sometimes to the point of obsession."),
#     Verbiage('Tsundoku', "Japanese", "The act of buying and collecting books but never getting around to reading them."),
#     Verbiage('Defenestration', "Latin", "The act of throwing someone or something out of a window."),
#     Verbiage("L'appel du vide", "French", "The instinnctive urge to jump from a high place, such as a cliff or a tall building."),
#     Verbiage("Shemomedjamo", "Georgian", "The act of eating beyond the point of being full, simply because the food is delicious.")
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def verbiages_index(request):
    verbiages = Verbiage.objects.all()
    return render(request, 'verbiages/index.html', {'verbiages': verbiages})
