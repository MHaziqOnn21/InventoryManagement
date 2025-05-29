from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import EmployeeIDAuthenticationForm, UserRegisterForm
from django.contrib.auth import authenticate, login

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(
            user=request.user,
            # fullname=request.user.get_first_name() or request.user.username,
            employee_id=request.user.username,
            employee_email=request.user.email,
            position='',
            department='',
        )
    return render(request, 'user_admin/profile.html', {'user_profile': user_profile})

@login_required
def employee_profile(request, employee_id):
    user_profile = get_object_or_404(UserProfile, employee_id=employee_id)
    return render(request, 'user_admin/employee_profile.html', {
        'user_profile': user_profile
    })

def login_view(request):
    if request.method == "POST":
        form = EmployeeIDAuthenticationForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=employee_id, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid Employee ID or password.")
    else:
        form = EmployeeIDAuthenticationForm()
    return render(request, "user_admin/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Create User
            user = User.objects.create_user(
                username=form.cleaned_data['employee_id'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['second_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['employee_email']
            )
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                second_name=form.cleaned_data['second_name'],
                employee_id=form.cleaned_data['employee_id'],
                contact_no=form.cleaned_data['contact_no'],
                employee_email=form.cleaned_data['employee_email'],
                position=form.cleaned_data['position'],
                department=form.cleaned_data['department'],
            )

            account_type = form.cleaned_data['account_type']
            if account_type == 'editor':
                user.is_staff = True
            else:
                user.is_staff = False

            user.save()

            messages.success(request, f"Account was created for: {form.cleaned_data['first_name']}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "user_admin/register.html", {"form": form})
