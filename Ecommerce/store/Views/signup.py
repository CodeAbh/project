from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from store.models.customor import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Signup(View):
    def get(self, request):
            return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('number')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            "first_name": first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password, )

        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, password)

            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self,customer):
        error_message = None

        if not customer.first_name:
            error_message = "Enter First Name"
        elif len(customer.first_name) < 4:
            error_message = "First Name Must Be Greater Than 4 digit "

        elif not customer.last_name:
            error_message = "Enter Last Name "
        elif len(customer.last_name) <= 4:
            error_message = "Last Name Must Be Greater Than 4 digit "

        elif not customer.phone:
            error_message = "Enter Phone Number "
        elif len(customer.phone) < 10:
            error_message = "Enter Valid Number "

        elif not customer.email:
            error_message = "Enter Email "
        elif len(customer.email) < 5:
            error_message = "Must Be Greater Than 5 Char "
        elif customer.isExists():
            error_message = 'Email Already Exist'

        return error_message