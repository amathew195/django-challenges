from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'january': 'eat no meat',
    'february': 'walk daily',
    'march': 'drink water',
    'april': 'this is my goal for april',
    'may': 'this is my goal for may',
    'june': 'this is my goal for june',
    'july': 'this is my goal for july',
    'august': 'this is my goal for august',
    'september': 'this is my goal for september',
    'october': 'this is my goal for october',
    'november': 'this is my goal for november',
    'december': None,
}


def index(request):
    months = list(monthly_challenges.keys())
    context = {
        "months": months
    }
    return render(request, 'challenges/index.html', context)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {"challenge_text": challenge_text,
                   "month": month}
        return render(request, 'challenges/challenge.html', context)
    except:
        raise Http404()
