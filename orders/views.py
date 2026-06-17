from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .decorators import role_required
from accounts.models import User
from .models import Table


@role_required([User.ROLE_CHOICES.WAITER])
def tables_view(request):
    return render(request, "orders/tables.html")
    tables = Table.objects.all()

    return render(request, "orders/tables.html", {
        'tables': tables
    })