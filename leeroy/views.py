from django.shortcuts import render_to_response

def root(request):
    return render_to_response('leeroy/root.html')

