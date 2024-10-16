from django.shortcuts import render


def get_page(request, paragraph):
    return render(request, 'page.html', context={'paragraph': paragraph})
