from django.shortcuts import render
from collections import Counter

def home(request):
    return render(request,'home.html')

def count(request):
    entered_text = request.GET['textarea']
    word_list = entered_text.split()
    word_dictionary = Counter(word_list)

    return render(request,'count.html',
    {'alltext':entered_text, 
    'total':len(word_list),
    'dictionary':word_dictionary.most_common(15)})
# Create your views here.
