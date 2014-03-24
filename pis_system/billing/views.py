from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
from pis_system.forms import *
from pis_system.models import *
def billing(request):
#    students = Student.objects.order_by('stud_id')
    userid = request.POST.get('userID')
    passwords = request.POST.get('password')
    if request.session.get('is_logged_in', False):
        user = {'name': request.session['name'], 'id': request.session['userID']}
#        item_search = ItemSearch()
        return render(
                        request, 
                        './billing/home.html',
                        {
                            'system_name': 'Enrolment System', 
                            'user': user, 
#                            'students': students,
#                           'item_search': item_search
                        }
                      )
    
    if request.method == 'POST':
        
        try:
            username = Employee_Account.objects.get(emp_id = userid)

        except Employee_Account.DoesNotExist:
            username = None

        if username is None:
            form=LogInForm()
            return render(request,'login.html',{'form': form,'system_name': 'Billing System',
                                                'cover_url':'static/images/billing_cover.jpg'}
                          )

        else:
            usrname = Employee.objects.get(emp_id=userid)
            students=Student.objects.get_queryset()
            if username.password == passwords:
                request.session['is_logged_in'] = True
                request.session['userID'] = str(username.emp_id)
                request.session['password'] = username.password
                request.session['name'] = usrname.firstname+' '+usrname.mi+' '+usrname.lastname
                user = {'name': request.session['name'], 'id': request.session['userID']}
                #item_search = ItemSearch()
                return render(request,'./billing/home.html',{'system_name': 'Enrolment System','user': user,'students': students,})
    else:
            form=LogInForm()
            return render(
                            request,
                            'login.html',
                            {
                                'form': form, 'system_name': 'Billing System',
                                'cover_url': 'static/images/billing_cover.jpg'
                            }
                          )

def search_student(request):
    context = RequestContext(request)
    search = request.GET.get('_search')
    type = request.GET.get('_type')
    students = Student.objects.all()
    size=len(students)
    total=0
    for x in students:
        if type == 'stud_id':
            if search in  x.stud_id:
              total=total+1
        elif type == 'lastname':
            if search in  x.lastname:
              total=total+1
        elif type == 'firstname':
            if search in  x.firstname:
              total=total+1

    return render_to_response('billing/studentlist.html', {'students': students , 'input':search, 'type_input': type,
                                                           'total':total, 'size':size}, context)

def get_student(request):
    context = RequestContext(request)
    getstud = request.GET.get('_stud')
    students=Student.objects.get(stud_id = getstud)
    words=str(students.image_path)
    lis = words.split("/")
    path=''
    for x in lis:
    	 if x != 'templates':
           path=path+'/'+x

    return render_to_response('billing/billing_stub.html', {'student': students, 'path': path }, context)

def get_bill(request):
    stud = request.GET.get('_bill')
    student_id=Student_Bill_Account.objects.get(stud_id = stud )
    student_bill = '<li><strong>ajshdkjashdjkashdjahd'+str(student_id.balance)+'</strong></li>'

    return  HttpResponse (student_bill)
