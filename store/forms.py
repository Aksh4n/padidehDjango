from django import forms
from .models import  *
import datetime

# Create your forms here.

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ()
		feilds = '__all__'
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class']= 'form-control'
		self.fields['last_name'].widget.attrs['class']= 'form-control'
		self.fields['phone'].widget.attrs['class']= 'form-control'	
		self.fields['city'].widget.attrs['class']= 'form-select'
		self.fields['state'].widget.attrs['class']= 'form-select'
		self.fields['address'].widget.attrs['class']= 'form-control'	
		self.fields['postal_code'].widget.attrs['class']= 'form-control'
		self.fields['email'].widget.attrs['class']= 'form-control'
		self.fields['items'].widget.attrs['class']= 'visually-hidden'	
		self.fields['complete'].widget.attrs['class']= 'visually-hidden'
		self.fields['transaction_id'].widget.attrs['class']= 'visually-hidden'
		self.fields['customer'].widget.attrs['style']= 'display:none;'



class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ()
		feilds = ['subject', 'name', 'email', 'message']
		
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))
class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
        
		exclude = ('user',)
		feilds = ['name', 'last','email','phone']
		name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
		last = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
		email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
		phone = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))
class CustomOrderForm(forms.ModelForm):
	class Meta:
		model = CustomOrder
		exclude = ()
		feilds = ['phone', 'name', 'email', 'message','image']
