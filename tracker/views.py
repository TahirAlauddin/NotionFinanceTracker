from .models import FinancialRecord

from django.contrib.auth.decorators import login_required
from .notion_service import get_financial_data, save_financial_data
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout



@login_required
def dashboard_view(request):
    records = FinancialRecord.objects.filter(user=request.user).order_by('-date')
    return render(request, 'dashboard.html', {'records': records})


@login_required
def sync_notion_data(request):
    data = get_financial_data()
    if data:
        save_financial_data(request.user, data)  # Save data to database
        return JsonResponse({"status": "success", "message": "Data synced successfully!"})
    else:
        return JsonResponse({"status": "error", "message": "Failed to fetch data from Notion. Check console for details."})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import FinancialRecordForm

@login_required
def create_record_view(request):
    if request.method == 'POST':
        form = FinancialRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('dashboard')
    else:
        form = FinancialRecordForm()
    return render(request, 'create_record.html', {'form': form})

@login_required
def update_record_view(request, pk):
    record = get_object_or_404(FinancialRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FinancialRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FinancialRecordForm(instance=record)
    return render(request, 'update_record.html', {'form': form})

@login_required
def delete_record_view(request, pk):
    record = get_object_or_404(FinancialRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('dashboard')
    return render(request, 'delete_record.html', {'record': record})
