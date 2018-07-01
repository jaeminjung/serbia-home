from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def stories_list(request):

    stories = Story.objects.all().order_by('-date')

    return render(request, 'stories/stories_list.html', {'stories': stories})


def stories_mylist(request):

    user = request.user
    stories = Story.objects.filter(author=user).order_by('-date')


    return render(request, 'stories/stories_mylist.html', {'stories':stories})


def stories_detail(request, p_key):

    # return HttpResponse("ahahha" + p_key)
    story = Story.objects.get(pk=p_key)

    return render(request, 'stories/stories_detail.html', {'story': story})


def stories_edit(request, p_key):
    story = Story.objects.get(pk=p_key)
    user = request.user
    story_user = story.author
    if user != story_user:
        raise forms.ValidationError("This user is not your story")

    if request.method == "POST":
        form = forms.CreateStory(request.POST, instance=story)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('stories_detail', p_key=story.pk)
    else:
        form = forms.CreateStory(instance=story)
    return render(request, 'stories/stories_edit.html', {'form': form, 'story': story})


@login_required(login_url='login_view')
def stories_create(request):
    if request.method == 'POST':
        form = forms.CreateStory(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('stories_list')
    else:
        form = forms.CreateStory()
    return render(request, 'stories/stories_create.html', {'form':form})


@login_required(login_url='login_view')
def add_comment(request, p_key):

    if request.method == "POST":
        story = Story.objects.get(pk=p_key)
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            return redirect('stories_list')
    else:
        form = forms.CommentForm()
    return render(request, 'stories/add_comment.html', {'form': form})

