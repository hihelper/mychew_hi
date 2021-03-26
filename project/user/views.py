from django.shortcuts import render, redirect
from django.views.generic.edit import FormView  # form을 활용할수 있게 해주는 클래스에요
from .forms import RegisterForm, LoginForm


from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'index.html', {})


class RegisterView(FormView):
    template_name = 'register.html'
    # template_name이라고 하면 html파일이조? 이게 부모인 FormView에서 가져온거에요.
    form_class = RegisterForm  # 위의 임포트든 된것을 form_class의 값으로 할당해줌.
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)

# 작동이 안됨... ㅠㅠ 모르겠어


# def logout(request):
#     if request.session.get('user'):
#         del(request.session['user'])

#     return redirect('/')
def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')
