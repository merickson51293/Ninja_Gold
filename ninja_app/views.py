from django.shortcuts import render, redirect
import random
from datetime import datetime



def ninja_gold(request):
    if "gold" not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render(request, "gold.html")

def process(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST['place'] == "farm":
            randy=round(random.random()*10+10)
            request.session['gold']+=randy
            request.session['activities'].append(f"You visited the farm and gained {randy} gold")
        if request.POST['place'] == "cave":
            randy= round(random.random()*5+5)
            request.session['gold']+=randy
            request.session['activities'].append(f"You visited the cave and gained {randy} gold")
        if request.POST['place'] == "house":
            randy= round(random.random()*2+3)
            request.session['gold']+=randy
            request.session['activities'].append(f"You visited the house and gained {randy} gold")
        if request.POST['place'] == "casino":
            randy=round(random.random()*100+-50)
            request.session['gold']+=randy
            if randy>0:
                request.session['activities'].append(f"You visited the casino and gained {randy} gold")
            else:
                request.session['activities'].append(f"You visited the casino and lost {randy} gold")
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')