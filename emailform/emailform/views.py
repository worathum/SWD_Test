from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name' :name,
            'email':email,
            'message':message,
        }
        message = '''ถึง คุณ {}\n\n\n{}'''.format(data['name'],data['message'])
        send_mail('Test E-mail,message',message,'',[data['email']])
        return HttpResponse("Email sent successfully")
    return render(request,'emailform/index.html',{})