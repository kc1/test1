from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from ipware.ip import get_ip
import json


def index(request):

    # https://github.com/rancavil/django-openshift-quickstart/wiki/Tutorial-How-create-an-application-with-Django-1.6-on-Openshift
    # https://github.com/jfmatth/openshift-django17

    print "index"



    return render_to_response('longform.html',context_instance=RequestContext(request))

def contact(request):

    print "contact"

    return HttpResponse(json.dumps({"success":True}), content_type="application/json")


# http://code.techandstartup.com/django/contact-form/

def send_email():
    return



