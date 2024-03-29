from django.shortcuts import render
from .forms import UserForm
from .models import User

def registeruser(request):
    if request.method == 'POST':
        print(request.POST) 
        form = UserForm(request.POST)
        if form.is_valid():
            # create user using form
            
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            # return redirect('registeruser')
            
            # create a user using create method
            first_name=form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.role=User.CUSTOMER
            user.save()
            print('user is created')
        else:
            print(form.non_field_errors)
            print(form.errors)
    else:
        form =UserForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/registeruser.html', context)