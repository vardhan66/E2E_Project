from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import socket
from .send_mail import SendMail
def generate_and_send_otp(user, email):
    token_generator = default_token_generator
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)
    otp = token[-6:]  # Simple example, you should implement a proper OTP system

    mail_data = {
        'email': email,
        'otp': otp
    }
    try:
        mailer = SendMail(mail_data)
        mailer.sendMail()
        return uidb64, token
    except socket.gaierror as e:
        print(f"Socket error: {e}")
        raise Exception("A network error occurred while sending the email. Please check your internet connection.")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise Exception("An error occurred while sending the email. Please try again later.")


def forgotpassword(request):
    stage = 'email'  # Initial stage

    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            try:
                user = User.objects.get(email=email)
                uidb64, token = generate_and_send_otp(user, email)
                request.session['uidb64'] = uidb64
                request.session['token'] = token
                stage = 'otp'
                messages.success(request, 'OTP has been sent to your email.')
            except User.DoesNotExist:
                stage = 'email'
                messages.error(request, 'No account found with this email address.')
            except Exception as e:
                stage = 'email'
                messages.error(request, str(e))

        elif 'otp' in request.POST:
            uidb64 = request.session.get('uidb64')
            token = request.session.get('token')
            otp = request.POST['otp']
            if token and otp and otp == token[-6:]:
                stage = 'password'
                messages.success(request, 'OTP verified successfully. Please enter a new password.')
            else:
                stage = 'otp'
                messages.error(request, 'Invalid OTP. Please try again.')

        elif 'new_password1' in request.POST and 'new_password2' in request.POST:
            uidb64 = request.session.get('uidb64')
            new_password1 = request.POST['new_password1']
            new_password2 = request.POST['new_password2']
            if new_password1 == new_password2:
                try:
                    uid = force_str(urlsafe_base64_decode(uidb64))
                    user = User.objects.get(pk=uid)
                    user.password = make_password(new_password1)
                    user.save()
                    messages.success(request, 'Password changed successfully. Please log in with your new password.')
                    return redirect('login')
                except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                    stage = 'password'
                    messages.error(request, 'An error occurred while changing the password. Please try again.')
            else:
                stage = 'password'
                messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'forgotpassword.html', {'stage': stage})