from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from books.forms import Contactform
from reportlab.pdfgen import canvas
from cStringIO import StringIO
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
    
def message_test(request):
    request.user.message_set.create(message = "Your playlist was added successfully.")
    return render_to_response("contact/thanks.html",context_instance = RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/contact/thanks/")
        else:
            form = UserCreationForm()
            return render(request,"registration/register.html",{'form':form})
#             return render_to_response("registration/register.html",{'form':form},context_instance=RequestContext(request))
    form = UserCreationForm()
    return render(request,"registration/register.html",{'form':form})
#     return render_to_response("registration/register.html",{'form':form},context_instance=RequestContext(request))    

def hello_pdf(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=hello.pdf'
    
    temp = StringIO()
    p = canvas.Canvas(temp)
    
    p.drawString(100,100,"Hello world")
    
    p.showPage()
    p.save()
    response.write(temp.getvalue())
    return response

def contact(request):
    errors = []
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email','zhongwuzw@sina.com'),
                      ['zhongwuzw@qq.com'],
                      )
            return HttpResponseRedirect('/contact/thanks')
#         else:
    form = Contactform()
    return render_to_response('contact_form.html',{'form':form},context_instance=RequestContext(request))
           # form = Contactform()
         #   assert False
            
            
"""   if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail')
        if not errors:
            send_mail(
                      request.POST['subject'],
                      request.POST['message'],
                      request.POST.get('email','zhongwuzw@sina.com'),
                      ['zhongwuzw@qq.com'],
                      )
            return HttpResponseRedirect('/contact/thanks/')
        return render_to_response('contact_form.html',{'errors':errors,
                                                       'subject':request.POST.get('subject',''),
                                                       'message':request.POST.get('message',''),
                                                       'email':request.POST.get('email',''),},context_instance=RequestContext(request))
"""
def contactemail(request):
 #   if request.POST['next']:
    if request.POST.get('next'):
        return HttpResponseRedirect(request.POST['next'])
    form = Contactform()
    return render_to_response('contact_form.html',{'form':form},context_instance=RequestContext(request))

@login_required
def congratulations(request):
    return render_to_response('Hello.html')

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
                                  {'books':books,'query':q})
    else:
        return render_to_response('search_form.html',{'error':True})
    