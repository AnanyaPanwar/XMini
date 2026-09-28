from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserRegistrationForm, XForm
from .models import X


def index(request):
    return redirect("x_list")


def x_list(request):
    query = request.GET.get("q", "").strip()

    xs = X.objects.select_related("user").all()

    if query:
        xs = xs.filter(
            Q(text__icontains=query)
            | Q(user__username__icontains=query)
        )

    return render(
        request,
        "x_list.html",
        {
            "xs": xs,
            "q": query,
        },
    )


@login_required
def x_create(request):
    if request.method == "POST":
        form = XForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()

            messages.success(
                request,
                "Your post was published.",
            )

            return redirect("x_list")

    else:
        form = XForm()

    return render(
        request,
        "x_form.html",
        {
            "form": form,
        },
    )


@login_required
def x_edit(request, x_id):
    x = get_object_or_404(
        X,
        pk=x_id,
        user=request.user,
    )

    if request.method == "POST":
        form = XForm(
            request.POST,
            request.FILES,
            instance=x,
        )

        if form.is_valid():
            if request.POST.get("photo-clear") == "on":
                x.photo.delete(save=False)
                x.photo = None

            x = form.save(commit=False)
            x.user = request.user
            x.save()

            messages.success(
                request,
                "Your post was updated.",
            )

            return redirect("x_list")

    else:
        form = XForm(instance=x)

    return render(
        request,
        "x_form.html",
        {
            "form": form,
            "x": x,
        },
    )


@login_required
def x_delete(request, x_id):
    x = get_object_or_404(
        X,
        pk=x_id,
        user=request.user,
    )

    if request.method == "POST":
        if x.photo:
            x.photo.delete(save=False)

        x.delete()

        messages.success(
            request,
            "Your post was deleted.",
        )

        return redirect("x_list")

    return render(
        request,
        "x_delete.html",
        {
            "x": x,
        },
    )


def register(request):
    if request.user.is_authenticated:
        return redirect("x_list")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Your account has been created.",
            )

            return redirect("x_list")

    else:
        form = UserRegistrationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )


def user_profile(request, username):
    profile_user = get_object_or_404(
        User,
        username=username,
    )

    xs = (
        X.objects
        .filter(user=profile_user)
        .select_related("user")
    )

    return render(
        request,
        "user_profile.html",
        {
            "profile_user": profile_user,
            "xs": xs,
        },
    )