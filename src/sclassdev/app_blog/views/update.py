from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request, id):
    post = query("SELECT * FROM blog_post WHERE id = %s", [id])
    print(post)

    if not post:
        return render(request, 'app_blog/not_found.html', status=404)
    
    if request.method == 'POST':
        
        post = post[0]

        title = request.POST.get('title')
        content = request.POST.get('content')

        query("UPDATE blog_post SET title = %s, content = %s WHERE id = %s", [title, content, id])

        return redirect("/blog/read/%s/{id}")
    
    return render(request, 'app_blog/update.html', {'post':post})
