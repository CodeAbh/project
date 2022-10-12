from django.shortcuts import render

# Function initialization

def Calculator(request):
    data = {}
    try:
        # iteration on operators
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('operator')
            if opr == "+":
                c = n1+n2;
            elif opr == "-":
                c = n1-n2;
            elif opr == "*":
                c = n1*n2;
            elif opr == "/":
                c = n1/n2;
            data = {
                'n1': n1,
                'n2': n2,
                'c': c
            }
    except:
            c = "invalid operator"
    return render(request, 'index.html', data)



    