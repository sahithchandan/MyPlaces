# Create your views here.
from mynotes.models import Note,User_Registration
import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.utils import simplejson
import string, random
from django.contrib.auth.models import User

class JSONResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super(JSONResponse, self).__init__(args, kwargs)
        self.status_code = 200
        self['Content-Type'] = 'application/json'

def home(request):
    return render_to_response("home.html", {}, context_instance=RequestContext(request))
    

def add_note(request):
    if request.method == "POST":
        try:
            userObj = User_Registration.objects.get(uuid = request.POST["uid"])
            Note.objects.create(title=request.POST["title"],description=request.POST["dec"],
                    created_by=userObj,created_on=datetime.datetime.today(),
                    latitue=request.POST["latitude"], longitude = request.POST["longitude"])
            status = 'sucess'
        except:
            status = 'error'
    dataarray = {'status':status}
    return JSONResponse(simplejson.dumps(dataarray))
    
    
def user_registration(request):
    if request.method == "POST":
        try:
            data = request.POST["data"]
            data = simplejson.dumps(data)
            name = data["name"]
            email = data["email"]
            first_name, last_name = name.split(" ")
            password = generate_password()
            userObj = User(username=email,password=password,first_name=first_name,last_name=last_name,email=email)
            userObj.save()
            User_Registration.objects.create(user = userObj,first_name=first_name,last_name=last_name,uuid=data["uuid"])
            status = 'success'
        except:
            status = 'error'
    dataarray = {'status':status}
    return JSONResponse(simplejson.dumps(dataarray))
    

def generate_password():
    choices = string.letters + string.digits
    rand_letter = lambda : random.choice(choices)
    return "".join([rand_letter() for el in range(8)])