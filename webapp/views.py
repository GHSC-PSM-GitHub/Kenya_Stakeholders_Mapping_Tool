from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm, cascadeForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record, Functionalarea, Rolename

from django.http import HttpResponseForbidden, HttpResponseServerError

from django.contrib import messages
from django import forms

from django.http.response import JsonResponse



# - Homepage 

def home(request):

    return render(request, 'index.html')


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()
  
    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
       

        form = CreateRecordForm(request.POST)

        if form.is_valid():
         
            record=form.save(commit=False)
            selected_counties = request.POST.getlist('county')
            counties_all=",".join(selected_counties)
          
            # counties=form.cleaned_data.get('county')
            # record.county=','.join(counties)
            # record.save()
            record.user=request.user
            record.county=counties_all

            record.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}
 

    return render(request, 'webapp/create-record.html',context)


# - Update a record 

@login_required(login_url='my-login')
def update_record(request, pk):


    # def dispatch(self, request, *args, **kwargs):
    #     handler = super(login_required, self).dispatch(request, *args, **kwargs)
    #     # Only allow editing if current user is owner
    #     if self.object.author != request.user:
    #         return HttpResponseForbidden(u'You can only edit records created by you!.')
    #     return handler

    # def get_success_url(self):
    #     return redirect('dashboard', args=[self.object.pk])
    
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)




    if request.method == 'POST':
    

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)
    is_owner = all_records.user == request.user

    context = {'record':all_records,'is_owner': is_owner}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")

def index(request):
     form=cascadeForm()
     return render(request, 'webapp/index.html', {"form1": form})

def load_rolenames(request):
    functionalarea_id = request.GET.get("functionalarea")
    rolenames = Rolename.objects.filter(functionalarea_id=functionalarea_id)
    return render(request, 'webapp/rolename_dropdown.html', {"rolenames": rolenames})





# # AJAX
# def load_rolenames(request):
#     Functionalarea_id = request.GET.get('Functionalarea_id')
#     rolenames = Rolename.objects.filter(Functionalarea_id=Functionalarea_id).all()
#     return render(request, 'webapp/rolename_dropdown_list_options.html', {'rolenames': rolenames})
    # print({'rolenames': rolenames})
    # return JsonResponse(list(rolenames.values('id', 'name')), safe=False)


#for J
# def load_rolenames(request):
#     functionalarea_id = request.GET.get("functionalarea")
#     rolenames = Rolename.objects.filter(functionalarea_id=functionalarea_id)
#     return render(request, "create-record.html", {"rolenames": rolenames})

# without Jquery
# def load_rolenames(request):
#     functionalarea_id = request.GET.get("functionalarea")
#     rolenames = Rolename.objects.filter(functionalarea_id=functionalarea_id)
#     return render(request, "webapp/rolename_dropdown_list_options.html", {"rolenames": rolenames})




