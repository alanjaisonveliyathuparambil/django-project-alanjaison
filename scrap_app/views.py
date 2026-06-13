from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, PickupRequestForm
from .models import PickupRequest, ScrapMaterial, Transaction, Notification


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')


# CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# SCRAP PRICES PAGE
def scrap_prices(request):

    materials = ScrapMaterial.objects.filter(
        is_active=True
    )

    return render(
        request,
        'scrap_prices.html',
        {'materials': materials}
    )


# REGISTER
def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)

            return redirect('home')

    else:
        form = UserRegistrationForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')


# USER DASHBOARD
@login_required
def user_dashboard(request):

    requests = PickupRequest.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'user_dashboard.html',
        {'requests': requests}
    )


# PICKUP REQUEST
@login_required
def request_pickup(request):

    if request.method == 'POST':

        form = PickupRequestForm(request.POST)

        if form.is_valid():

            pickup = form.save(commit=False)
            pickup.user = request.user
            pickup.save()

            return redirect('user_dashboard')

    else:
        form = PickupRequestForm()

    return render(
        request,
        'request_pickup.html',
        {'form': form}
    )


# MY REQUESTS
@login_required
def my_requests(request):

    requests = PickupRequest.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_requests.html',
        {'requests': requests}
    )


# MY TRANSACTIONS
@login_required
def my_transactions(request):

    transactions = Transaction.objects.all()

    return render(
        request,
        'my_transactions.html',
        {'transactions': transactions}
    )


# NOTIFICATIONS
@login_required
def notifications(request):

    notices = Notification.objects.filter(
        user=request.user
    )

    return render(
        request,
        'notifications.html',
        {'notices': notices}
    )


# COLLECTOR DASHBOARD
@login_required
def collector_dashboard(request):
    return render(
        request,
        'collector_dashboard.html'
    )


# ASSIGNED PICKUPS
@login_required
def assigned_pickups(request):
    return render(
        request,
        'assigned_pickups.html'
    )


# UPDATE COLLECTION
@login_required
def update_collection(request):
    return render(
        request,
        'update_collection.html'
    )


# ADMIN DASHBOARD
@login_required
def admin_dashboard(request):
    return render(
        request,
        'admin_dashboard.html'
    )


# MANAGE SCRAP
@login_required
def manage_scrap(request):
    return render(
        request,
        'manage_scrap.html'
    )


# MANAGE REQUESTS
@login_required
def manage_requests(request):
    return render(
        request,
        'manage_requests.html'
    )


# MANAGE COLLECTIONS
@login_required
def manage_collections(request):
    return render(
        request,
        'manage_collections.html'
    )


# MANAGE TRANSACTIONS
@login_required
def manage_transactions(request):
    return render(
        request,
        'manage_transactions.html'
    )


# MANAGE USERS
@login_required
def manage_users(request):
    return render(
        request,
        'manage_users.html'
    )


# REPORTS
@login_required
def reports(request):
    return render(
        request,
        'reports.html'
    )

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')

def help_page(request):
    return render(request, 'help.html')