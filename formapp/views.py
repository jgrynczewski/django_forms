from django.shortcuts import render, redirect

from formapp.models import Message


def contact1(request):
    if request.method == "GET":
        return render(
            request,
            'formapp/contact1.html',
        )

    elif request.method == "POST":
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        category = data.get('category')
        subject = data.get('subject')
        body = data.get('body')

        Message.objects.create(
            name=name,
            email=email,
            category=category,
            subject=subject,
            body=body
        )

        return redirect('contact1')
