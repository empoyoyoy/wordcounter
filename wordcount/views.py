from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
    return render(request,'home.html',{'hithere': 'This is me'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    counts = Counter(wordlist)
    mxwrdcnt = max(counts.values())
    maxwords = [key for key, value in counts.items() if value == mxwrdcnt] 
    print(maxwords)
    

    return render(request,'count.html',{'fulltext':fulltext,'count': len(wordlist),'maxwords':",".join(maxwords),'mxwordapp':mxwrdcnt})

def about(request):
    return render(request,'about.html')