from django.shortcuts import render, redirect


def biography (request):
    return render(request, "Biography.html")