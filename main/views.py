from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag #for Post tags

from .models import Post, Comment 
from .forms import CreateCommentForm 
import json #json used for post searching
from django.http import JsonResponse #we return jsonresponse to our javascript

#url name 'home-page'
def home(request, tag_slug = None):
    tag = None

    if tag_slug != 'clear': #if there is a tag selected 
        try: #try to get the tag from Tag objects
            tag = Tag.objects.filter(slug = tag_slug).first() 
        except Tag.DoesNotExist:
            tag = None

    #if there is a tag we will keep its id in our session
    #if there is no tag selected or the selected tag is somehow incorrect we set the tag_id to -1
    if tag != None:
        request.session['tag_id'] = tag.id
    else:
        request.session['tag_id'] = -1
    
    tags = Tag.objects.all().values()
    return render(request, 'main/home.html', {'tags' : tags, 'tag_activated' : request.session.get('tag_id', False)})

#url name 'post-detail' - this view shows the entire blog post
def post_detail(request, slug):
    #if there is a POST request for adding a new comment
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user 
            comment.for_post = get_object_or_404(Post, slug = slug)
            comment.save()
    else:
        form = CreateCommentForm()

    post = get_object_or_404(Post, slug = slug)
    comments = Comment.objects.filter(for_post = post).all().order_by('-created_on')
    
    return render(request, 'main/post_detail.html', {'post': post, 'comments': comments, 'form': form})

#url name 'comment-delete' - this view deletes the comment of the logged in user 
#and redirects him to the post he was reading
def comment_delete(request, comment_id):
    comment = Comment.objects.filter(id = comment_id).first()
    post_slug = comment.for_post.slug
    comment.delete()

    return redirect('post-detail', slug=post_slug)

#url name 'search-posts'
#this view is used with JavaScript to return only the posts that 
#match the "search" criteria
def search_posts(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('search_value') #get the search value that the JavaScript "posted"
        
        #check if there is a tag selected by the user
        tag_id = request.session.get('tag_id', False) 
        if tag_id != False and tag_id != -1:
            tag = Tag.objects.filter(id = tag_id).first()

        #if search_str is not None we will filter Posts by looking for the phrase in the title and in the description
        if search_str != None and len(search_str.replace(" ", "")) > 0:        
            if tag_id != False and tag_id != -1:
                posts = list(Post.objects.defer('content').filter(title__icontains = search_str, tags__in = [tag]).order_by('-created_on').values() | Post.objects.defer('content').filter(description__icontains = search_str, tags__in = [tag]).order_by('-created_on').values())
            else:
                posts = list(Post.objects.defer('content').filter(title__icontains = search_str).order_by('-created_on').values() | Post.objects.defer('content').filter(description__icontains = search_str).order_by('-created_on').values())
        else:
            posts = list(Post.objects.defer('content').filter(tags__in = [tag]).order_by('-created_on').values()) if tag_id != False and tag_id != -1 else list(Post.objects.defer('content').all().values())

        #adding tags to each post & formatting for javascript
        for post in posts:
            if 'content' in post:
                del post['content']
            post['tags'] = list(Post.objects.filter(id = post['id']).first().tags.names())

        return JsonResponse(list(posts), safe = False)

#url name 'contact-page'
#rendering a simple html contact template
def contact(request):
    return render(request, 'main/contact.html')
