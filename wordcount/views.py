from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, './home.html')

def test(request):
    return render(request, './test.html')  # goes to the page    

def count(request):
    fulltext = request.GET['fulltext']  # variable of 'fulltext' that is from: home.html - text area, name='fulltext'.
    
    wordlist = fulltext.split()  # this splits the fulltext.

    worddictionary = {}  # create empty dictionary, counter = zero/empty

    # this the counter
    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] +=1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # v1 return render(request, './count.html', {'fulltext':fulltext})  # goes to the page // pass dictionary:fulltext // 
    # v2 return render(request, './count.html', {'fulltext':fulltext, 'count':len(wordlist)})  # goes to the page // pass dictionary:fulltext and length of wordlist // 
    return render(request, './count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})  # goes to the page // pass dictionary:fulltext and length of wordlist // 


