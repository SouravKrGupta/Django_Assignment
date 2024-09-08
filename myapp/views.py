from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.contrib.auth import logout as auth_logout

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        category = request.POST['category']
        user = User(name=name, phone=phone, email=email, password=password, category=category)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def index_view(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        return render(request, 'index.html', {'username': user.name})
    return redirect('login')

def get_categories(request):
    categories = User.objects.values_list('category', flat=True).distinct()
    return JsonResponse(list(categories), safe=False)

def search_users(request):
    query = request.GET.get('query', '')
    users = User.objects.filter(name__icontains=query) | User.objects.filter(category__icontains=query)
    users = users.values('name', 'phone', 'email')
    return JsonResponse(list(users), safe=False)

def logout_view(request):
    if 'user_id' in request.session:
        request.session.flush()  # Clear the session data
    return redirect('login')  