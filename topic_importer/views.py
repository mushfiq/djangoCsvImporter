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
    tes_list = csv_to_list("/home/caveman/Desktop/NewsCred_Django_App/imdb.csv")
    for t in tes_list:
        if(len(t) >0):
            data_insert = movie_topic(movie_name=t[0],imdb_id=t[1])
            try:
                data_insert.save()
                print "inserted!"
            except e:
                print e

    return HttpResponse("sucess!")

def file_upload(request):
    print settings.STATIC_ROOT

    if request.method == 'POST':
        try:
            if(handle_uploaded_file(request.FILES['myfile']) == "true"):
                return render_to_response('base.html',context_instance=RequestContext(request))
            else:
                 return render_to_response('error.html', context_instance=RequestContext(request))
        except Exception, e:
            print e


    return render_to_response(
        'index.html',
            {'settings.STATIC_ROOT':settings.STATIC_ROOT}, context_instance=RequestContext(request))
        


   
        #print request

    #return HttpResponse("Inside file upload view!")


