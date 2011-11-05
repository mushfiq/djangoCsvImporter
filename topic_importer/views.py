from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.template import RequestContext
from topic_importer.models import movie_topic
from utils import csv_to_list,handle_uploaded_file

def index(request):
    print request
    return HttpResponse("Topic Importer app")


def test(request):
    print settings.DIRNAME
    tes_list = csv_to_list(settings.DIRNAME+"/topic_importer/file.csv")
    for t in tes_list:
        if(len(t) >0):
            data_insert = movie_topic(movie_name=t[0],imdb_id=t[1])
            try:
                data_insert.save()
                msg =  "inserted!"

            except e:
                msg = "unable to insert :("
               
    return render_to_response('index.html',
            { 'msg':msg },
            context_instance=RequestContext(request),
            )
    #return HttpResponse("sucess!")

    

def file_upload(request):
    print settings.STATIC_ROOT

    if request.method == 'POST':
        try:
            if(handle_uploaded_file(request.FILES['myfile']) == "true"):
                msg = "success"
                return render_to_response('index.html',
                        { 'msg':msg },
                context_instance=RequestContext(request),
                )
            else:
                 return render_to_response('error.html', context_instance=RequestContext(request))
        except Exception, e:
            print e

    return render_to_response(
        'index.html',
            {'settings.STATIC_ROOT':settings.STATIC_ROOT}, context_instance=RequestContext(request))


