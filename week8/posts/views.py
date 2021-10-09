from datetime import datetime

from django.shortcuts import render, redirect

from .models import Post


def new(request):
    return render(request, 'form.html')


def create(request):
    title = request.POST['title']
    content = request.POST['content']
    created_by = request.POST['created_by']
    Post.objects.create(
        title=title,
        content=content,
        created_by=created_by,
        created_at=datetime.now(),
    )
    # return render(request, 'form.html')
    return redirect('/')


def list(request):
    post_all = Post.objects.all()  # Post 모델의 전체 데이터 조회
    context = {'post_all': post_all}  # 응답의 context 데이터 생성
    # 요청에 응답 함수, 'list.html'은 파일명이며 templates 폴더에 존재해야 함
    return render(request, 'list.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)  # Post 모델의 특정 데이터 조회
    context = {'post': post}
    return render(request, 'detail.html', context)


def delete(request, id):
    context = {}
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('list')
    else:
        context.update(post=post)
        return render(request, 'confirm_delete.html', context)


def update(request, id):
    context = {'title': '글 수정', 'submit_text': '수정하기'}
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        created_by = request.POST['created_by']

        post.title = title
        post.content = content
        post.created_by = created_by
        post.save()
        return redirect('detail', id)
    else:
        # print('dfdfd')
        # print(context)
        context.update(post=post)
        # print(context)
        return render(request, 'form.html', context)
