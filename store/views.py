from django.shortcuts import render , redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth import authenticate , login , logout
from .forms import *
from text.models import *

def cart(request):
	products = Product.objects.all()
	data = cartData(request)
	star = Star.objects.all()
	cat = Category.objects.all()
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'star':star, 'cat':cat}

	return render(request, 'cart.html', context)

def getvar(request):
	var = request.POST['option']
	print(var)
	return JsonResponse({
		'msg':'ok' , 'var':var
	}) 

def home(request):
	t = HomePageHeadLine.objects.get(id=1)
	return render(request, 'index.html', {'t':t })
def logout_user(request):
    logout(request)
    return redirect('home')

def shop(request):
	products = Product.objects.all()
	new = Product.objects.filter(category__name='جدید')
	data = cartData(request)
	star = Star.objects.all()
	cat = Category.objects.all()
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	sort_by = request.GET.get("sort", "l2h") 
	if sort_by == "l2h":
		products = Product.objects.all().order_by("price")
	elif sort_by == "h2l":
		products = Product.objects.all().order_by("-price")
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'star':star, 'cat':cat, 'new':new}
	return render(request, 'shop.html', context )

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	if request.user.is_authenticated:
		customer = request.user.customer
	else:
		customer = None	

	form = OrderForm()
	form.fields['items'].initial = items 
	form.fields['complete'].initial = True
	form.fields['customer'].initial = customer
	form.fields['transaction_id'].initial = datetime.datetime.now().timestamp()


	

	context = {'items':items, 'order':order, 'cartItems':cartItems , 'form':form}
	if request.method == 'POST':

		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({
				'msg':'success'
			})

		else:
			return JsonResponse({
				'msg':'err'
			})	
	return render(request, 'c2.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	option = data['option']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'post':
		
		orderItem.option = option


	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse( {'msg': 'success'} , safe=False)
from django.db.models import Q
def searchProduct(request):
	if request.method == 'GET':
		data = cartData(request)
		star = Star.objects.all()
		cat = Category.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		query= request.GET.get('q')
		if query is not None:
			lookups= Q(name__icontains=query) | Q(info__icontains=query)
			products= Product.objects.filter(lookups).distinct()
			context={'products': products,'items':items, 'order':order, 'cartItems':cartItems , 'star':star}
			print(products)		 
			return render(request, 'shop.html', context)
		else:
			return redirect('shop')
	else:
		return redirect('shop')

def searchProductByCat(request):
	if request.method == 'GET':
		data = cartData(request)
		star = Star.objects.all()
		cat = Category.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']
		query= request.GET.get('q')
		if query is not None:
			lookups= Q(category__name=query)
			products= Product.objects.filter(lookups).distinct()
			context={'products': products,'items':items, 'order':order, 'cartItems':cartItems , 'star':star}
			print(products)		 
			return render(request, 'shop.html', context)
		else:
			return redirect('shop')
	else:
		return redirect('shop')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()  
            return JsonResponse({'msg': 'Success'})
    return render(request , 'contact.html', {})


def test(request):
	products = Product.objects.all()
	data = cartData(request)
	star = Star.objects.all()
	cat = Category.objects.all()
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	sort_by = request.GET.get("sort", "l2h") 
	if sort_by == "l2h":
		products = Product.objects.all().order_by("price")
	elif sort_by == "h2l":
		products = Product.objects.all().order_by("-price")
	

	context = {'items':items, 'order':order, 'cartItems':cartItems ,'products':products , 'star':star, 'cat':cat}


	return render(request, 'test.html', context)
from django.contrib.auth.forms import UserCreationForm
def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'Err'})
def login_user(request):
	if request.method == "POST" :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'Err'})


def profile(request):
	return render(request, 'profile.html', {})
def about(request):
	honors = Honor.objects.all()
	projects = Project.objects.all()
	return render(request, 'about.html', {'honors':honors, 'projects':projects})
def updateprofile(request):
	if request.method == "POST":
		customer = Customer.objects.get(id=request.user.customer.id)
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid:
			form.save()
			return JsonResponse({'msg':'Success'})
		else:
			return JsonResponse({'msg':'err'})
def sefaresh(request):
	if request.method == "POST":
		form = CustomOrderForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return JsonResponse({'msg': 'Success'})
		else:
			return JsonResponse({'msg': 'ERRRR'})

def discount(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		if request.method == "POST":
			total = order.get_cart_total
			code = request.POST['code']
			print(code)
			discode = Promotion.objects.get(description__iexact=code)
			print(discode)
			a = float(discode.discount)
			p = a / 100
			b = total * p
			print(b)
			c = total - b
			total2 = c
			print(total2)
			return JsonResponse({
				'code':code,
				'discount':b,
				'msg':total2
			})
		    
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 50000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(reverse('callback-gateway'))
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e
import logging

from django.http import HttpResponse, Http404
from django.urls import reverse

from azbankgateways import bankfactories, models as bank_models, default_settings as settings


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")

import logging
from azbankgateways import bankfactories, models as bank_models, default_settings as settings

factory = bankfactories.BankFactory()

# غیر فعال کردن رکورد های قدیمی
bank_models.Bank.objects.update_expire_records()

# مشخص کردن رکوردهایی که باید تعیین وضعیت شوند
for item in bank_models.Bank.objects.filter_return_from_bank():
	bank = factory.create(bank_type=item.bank_type, identifier=item.bank_choose_identifier)
	bank.verify(item.tracking_code)		
	bank_record = bank_models.Bank.objects.get(tracking_code=item.tracking_code)
	if bank_record.is_success:
		logging.debug("This record is verify now.", extra={'pk': bank_record.pk})


