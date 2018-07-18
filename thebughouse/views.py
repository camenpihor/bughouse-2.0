import os

import mammoth
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, forms as auth_forms, login, logout, models as auth_models
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect

from .models import Post


def home(request):
    return_variables = {'page_name': 'Home'}
    return render(request, 'base.html', return_variables)


def archive(request):
    return_variables = {'page_name': 'Archive'}
    all_posts = Post.objects.all().order_by('-created_at_utc')
    return_variables['all_posts'] = all_posts
    return render(request, 'archive.html', return_variables)


def authors(request):
    return_variables = {'page_name': 'Authors'}
    return render(request, 'base.html', return_variables)


def post(request, year, author, title):
    return_variables = {'page_name': 'Post'}
    try:
        blog_post = Post.objects.get(url=f"post/{year}/{author}/{title}")
        return_variables['post'] = blog_post
        return render(request, 'post.html', return_variables)
    except ObjectDoesNotExist:
        raise Http404


@staff_member_required(login_url='user/sign-in', redirect_field_name=None)
def control(request, action):
    return_variables = {'page_name': 'Control', 'action': action}

    if request.method == 'POST':
        form = request.POST

        if action == 'create':
            file = request.FILES['file']
            html = mammoth.convert_to_html(file).value
            post = Post.objects.create(author=form['author'], title=form['title'], html=html,
                                       content_warnings=form['content_warnings'])
            return_variables['success_message'] = 'Created'
            return_variables['post'] = post

        elif action == 'delete':
            try:
                post = Post.objects.get(url=form['url'])
                post.delete()
                return_variables['success_message'] = 'Deleted'
            except ObjectDoesNotExist:
                return_variables['error_message'] = 'Could not find post'

    return render(request, 'control.html', return_variables)


@staff_member_required(login_url='user/sign-in', redirect_field_name=None)
def discussion(request):
    return_variables = {'page_name': 'Discussion'}
    return render(request, 'discussion.html', return_variables)


def user(request, form_type):
    return_variables = {'page_name': 'User', 'form_type': form_type}
    if request.method == 'POST':
        form = request.POST

        if form_type == 'sign-in':
            user = authenticate(request=request, username=form['username'], password=form['password'])
            if user:
                login(request, user)
            else:
                return_variables['error_message'] = 'Invalid crededentials'
                return render(request, 'user.html', return_variables)

        elif form_type == 'sign-up':
            try:
                user = auth_models.User.objects.create_user(form['username'], form['email'], form['password'])
                user.save()
                login(request, user)
            except IntegrityError:
                return_variables['error_message'] = 'Username or email already used'
                return render(request, 'user.html', return_variables)

        elif form_type == 'forgot-password':
            reset_form = auth_forms.PasswordResetForm(form)
            if reset_form.is_valid():
                reset_form.save(from_email=os.environ['EMAIL_HOST_USER'], request=request)

        # if any of the user actions is successful
        return redirect('thebughouse:home')

    elif request.user.is_authenticated:
        if form_type == 'sign-out':
            logout(request)
            return redirect('thebughouse:home')
        else:
            raise Http404
    return render(request, 'user.html', return_variables)
