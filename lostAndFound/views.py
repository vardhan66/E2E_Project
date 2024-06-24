from django.shortcuts import render,redirect
from .form import LostItemForm,FoundItemForm
from .search import SearchItems
from django.http import JsonResponse
import json

def LostandFound(request):
    return render(request,'lostandfound.html')
def Lostform(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('/lostandfound/searching/id={}'.format(instance.submissionID))
    return render(request,'lostform.html',{'form':LostItemForm})
def Foundform(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save()
            print(instance.submissionID)
            return redirect('/lostandfound/searching/id={}'.format(instance.submissionID))
    return render(request,'foundform.html',{'form':FoundItemForm})


def Searching(request,id):
    return render(request,'searching.html')

def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        got = SearchItems(id)
        return JsonResponse({"status":got})