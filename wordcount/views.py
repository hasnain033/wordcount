from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):

	return render(request,'home.html')

def count(request):

	fultext= request.GET['fultext']

	wordlist=fultext.split()

	worddict={}

	for words in wordlist:
		if words in worddict:
			# increse num
			worddict[words]+=1
		else:
			# add to dict
			worddict[words]=1

	sortedword=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)

	return render(request,'count.html',{'fultext':fultext,'wordlist':len(wordlist),'worddict':sortedword})


def about(request):

	return render(request,'about.html')

