from django.shortcuts import render, redirect

from expenses_tracker_app.web_expenses_tracker_app.forms import ProfileCreateForm, ProfileEditForm, ExpenseCreateForm, \
    ExpenseEditForm, ExpenseDeleteForm
from expenses_tracker_app.web_expenses_tracker_app.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def home_page(request):
    profile = get_profile()

    if not profile:
        return redirect('create_profile')

    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)

    context = {
        'expenses': expenses,
        'budget': profile.budget,
        'budget_left': budget_left,
    }

    return render(request, 'core/home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = ExpenseCreateForm()
    else:
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ExpenseEditForm(instance=expense)
    else:
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ExpenseDeleteForm(instance=expense)
    else:
        expense.delete()
        return redirect('home page')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expense/expense-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'hide_nav_links': True,
    }
    return render(request, 'core/home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    count_expenses = Expense.objects.count()

    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'count_expenses': count_expenses,
    }

    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    if request.method == 'POST':
        expenses.delete()
        profile.delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')
