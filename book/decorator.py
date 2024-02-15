from django.shortcuts import render

def logincheck(function):
    def wrapper(request,*args, **kwargs):
        username = request.session.get('username')
        if username:
            response = function(request,*args, **kwargs)
            return response
        return render(request,'authntication/error.html')
    return wrapper


