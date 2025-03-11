from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Shop, Employee
def home(request):
    return render(request, 'index.html')
# ================= CUSTOMER VIEWS ===================
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def add_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        purchases = request.POST['purchases']
        feedback = request.POST['feedback']
        Customer.objects.create(name=name, phone=phone, purchases=purchases, feedback=feedback)
        return redirect('customer_list')
    return render(request, 'add_customer.html')

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        customer.name = request.POST['name']
        customer.phone = request.POST['phone']
        customer.purchases = request.POST['purchases']
        customer.feedback = request.POST['feedback']
        customer.save()
        return redirect('customer_list')
    return render(request, 'edit_customer.html', {'customer': customer})

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_list')

# ================= SHOP VIEWS ===================
def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops.html', {'shops': shops})

def add_shop(request):
    if request.method == "POST":
        name = request.POST['name']
        owner = request.POST['owner']
        category = request.POST['category']
        contact = request.POST['contact']
        rent = request.POST['rent']
        Shop.objects.create(name=name, owner=owner, category=category, contact=contact, rent=rent)
        return redirect('shop_list')
    return render(request, 'add_shop.html')

def edit_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    if request.method == "POST":
        shop.name = request.POST['name']
        shop.owner = request.POST['owner']
        shop.category = request.POST['category']
        shop.contact = request.POST['contact']
        shop.rent = request.POST['rent']
        shop.save()
        return redirect('shop_list')
    return render(request, 'edit_shop.html', {'shop': shop})

def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    shop.delete()
    return redirect('shop_list')

# ================= EMPLOYEE VIEWS ===================
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        position = request.POST['position']
        salary = request.POST['salary']
        shop_id = request.POST['shop']
        shop = get_object_or_404(Shop, id=shop_id)
        Employee.objects.create(name=name, position=position, salary=salary, shop=shop)
        return redirect('employee_list')
    shops = Shop.objects.all()
    return render(request, 'add_employee.html', {'shops': shops})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        employee.name = request.POST['name']
        employee.position = request.POST['position']
        employee.salary = request.POST['salary']
        shop_id = request.POST['shop']
        employee.shop = get_object_or_404(Shop, id=shop_id)
        employee.save()
        return redirect('employee_list')
    shops = Shop.objects.all()
    return render(request, 'edit_employee.html', {'employee': employee, 'shops': shops})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')
