from django.shortcuts import render_to_response, get_object_or_404
from servers.models import Server

def index(request):
  server_list = Server.objects.all()
  return render_to_response('servers/index.html', { 'server_list': server_list })

def detail(request, server_id):
  s = get_object_or_404(Server, pk=server_id)
  return render_to_response('servers/detail.html', { 'server': s })

def job_detail(request, server_id, build):
  s = get_object_or_404(Server, pk=server_id)
  return render_to_response('servers/build.html', { 'server': s, 'build': s.build(build) })
