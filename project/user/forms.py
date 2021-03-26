from django import forms
from .models import BlogUser
from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(forms.Form):  # forms.Form을 상속받아요.
    email = forms.EmailField(
        error_messages={    # 입력하지 않을시 생성되는 오류 메시지
            'required': '이메일을 입력해주세요'
        },
        max_length=64,
        label='이메일'
    )
    name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요'
        },
        label='사용자 이름'
    )
    phonenumber = forms.CharField(
        error_messages={
            'required': '전화번호를 입력해주세요'
        },
        label='사용자 연락처'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput,  # 추측컨데 비밀번호 입력 요건을 갖춘 입력방식이 될듯함.
        label='비밀번호'            # 라벨 이름을 표기함.
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인'
    )

    def clean(self):  # validation을 진행하는 메서드
        cleaned_data = super().clean()  # 부모 클래스에서 갖고 있던 clean을 상속 받아요.
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        phonenumber = cleaned_data.get('phonenumber')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:  # 비밀번호 입력란 2개가 입력되어야하고
            if password != re_password:  # 2개가 입력되었지만 서로 다른 경우 오류 메시지를 출력하도록함.
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')

        if BlogUser.objects.filter(email=email):
            self.add_error('email', '이미 가입된 이메일 입니다.')
        if BlogUser.objects.filter(phonenumber=phonenumber):
            self.add_error('email', '이미 가입된 연락처 입니다.')

        if not(email and name and phonenumber and password and re_password):
            self.add_error('email', '모든 값이 전부 입력되어야만 합니다.')

        else:
            user = BlogUser(
                email=email,
                name=name,
                phonenumber=phonenumber,
                password=make_password(password),
            )
            user.save()  # db저장


class LoginForm(forms.Form):  # forms.Form을 상속받아요.
    email = forms.EmailField(
        error_messages={    # 입력하지 않을시 생성되는 오류 메시지
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.Textarea,  # 추측컨데 비밀번호 입력 요건을 갖춘 입력방식이 될듯함.
        label='비밀번호'            # 라벨 이름을 표기함.
    )

    def clean(self):  # validation을 진행하는 메서드
        cleaned_data = super().clean()  # 부모 클래스에서 갖고 있던 clean을 상속 받아요.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print(email, password)

        if email and password:  # 비밀번호 입력란 2개가 입력되어야하고
            try:
                user = BlogUser.objects.get(email=email)
            except BlogUser.DoesNotExist:
                self.add_error('email', '존재하지 않는 아이디입니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
