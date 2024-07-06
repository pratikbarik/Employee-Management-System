from django.shortcuts import render,redirect
from myapp.models import UserMaster,Leave,ApplyLeave
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']   
        try:
            obj=UserMaster.objects.get(Email=email,Password=password)
            if obj.Status=='active':
                if obj.Role=='admin':
                    request.session["name"] = obj.Name
                    request.session["phone"] = obj.Phone
                    request.session["id"] = obj.UserId
                    request.session["role"] = obj.Role
                    return render(request,'adminlanding.html',{'data':obj})
                elif obj.Role=='hr':
                    request.session["name"] = obj.Name
                    request.session["phone"] = obj.Phone
                    request.session["id"] = obj.UserId
                    request.session["role"] = obj.Role
                    return render(request,'hrlanding.html',{'data':obj})
                else:
                    request.session["name"] = obj.Name
                    request.session["phone"] = obj.Phone
                    request.session["id"] = obj.UserId
                    request.session["role"] = obj.Role
                    return render(request,'employeelanding.html',{'data':obj})
            else:
                return render(request,'login.html',{'data':'You Are Not an Active User'})
        except Exception as e:
            return render(request,'login.html',{'data':'Invalid'+str(e)})  
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        role=request.POST['role']
        password=request.POST['password']
        object=UserMaster.objects.create(Name=name,Email=email,Phone=phone,Gender=gender,Role=role,Password=password)
        object.save()
        return redirect('/login')
    return render(request,'register.html')
def admin(request):
    return render(request,'adminlanding.html')

def hr(request):
    return render(request,'hrlanding.html')

def allUser(request):
    role=request.session['role']
    if role=='admin':
        obj=UserMaster.objects.exclude(Role='admin')
        return render(request,'allUsersData.html',{'users':obj})
    elif role=='hr':
        obj=UserMaster.objects.get(Role='employee')
        return render(request,'allUsersData.html',{'users':obj})

def changeStatus(request,UserId):
    obj=UserMaster.objects.get(pk=int(UserId))
    if obj.Status=='active':
        obj.Status='inactive'
    else:
        obj.Status='active'
    obj.save()
    role=request.session['role']
    if role=='admin':
        return redirect('/allUserData')
    else:
        return redirect('/allEmployeeData')
    
def deleteUser(request,UserId):
    obj=UserMaster.objects.get(pk=int(UserId))
    obj.delete()
    role=request.session['role']
    if role=='admin':
        return redirect('/allUserData')
    else:
        return redirect('/allEmployeeData')

def editUser(request,UserId):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        role=request.POST['role']
        UserId=request.POST['UserId']
        ob=UserMaster.objects.get(pk=int(UserId))
        ob.Name=name
        ob.Email=email
        ob.Phone=phone
        ob.Role=role
        ob.Gender=gender
        ob.save()
        role=request.session['role']
        if role=='admin':
            return redirect('/allUserData')
        else:
            return redirect('/allEmployeeData')
    obj=UserMaster.objects.get(pk=int(UserId))
    return render(request,'editUser.html',{'Name':obj.Name,'Email':obj.Email,'Phone':obj.Phone,'UserId':obj.UserId,'Gender':obj.Gender,'Role':obj.Role})

def logout(request):
    request.session.flush()
    return redirect('/')

def editProfile(request,UserId):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        role=request.POST['role']
        UserId=request.POST['UserId']
        ob=UserMaster.objects.get(pk=int(UserId))
        ob.Name=name
        ob.Email=email
        ob.Phone=phone
        ob.Role=role
        ob.Gender=gender
        ob.save()
        request.session['name']=name
        request.session['phone']=phone
        request.session['id']=UserId
        request.session['role']=role
        return redirect('/myadmin')
    obj=UserMaster.objects.get(pk=int(UserId))
    return render(request,'editProfile.html',{'data':obj})

def allEmployeeData(request):
    obj=UserMaster.objects.filter(Role='employee')
    return render(request,'allEmployeeData.html',{'user':obj})

def applyLeave(request):
    if request.method=='POST':
        UserId=UserMaster.objects.get(pk=int(request.session['id']))
        LeaveId=Leave.objects.get(pk=int(request.POST['LeaveId']))
        ToDate=request.POST['todate']
        FromDate=request.POST['fromdate']
        Reason=request.POST['reason']
        obj=ApplyLeave.objects.create(UserId=UserId,LeaveId=LeaveId,ToDate=ToDate,FromDate=FromDate,Reason=Reason)
        obj.save()
        return redirect('/employeelanding',{'message':'Application Submitted Succesfully'})
    obj=Leave.objects.all()
    return render(request,'applyLeave.html',{'leaves':obj})

def employeelanding(request):
    return render(request,'employeelanding.html')