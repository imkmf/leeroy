from django.shortcuts import render_to_response
from servers.models import Server

def index(request):
  server_list = Server.objects.all()
  return render_to_response('servers/index.html', { 'server_list': server_list })
