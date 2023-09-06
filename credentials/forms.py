from django import forms

class MyForm(forms.Form):
    department = forms.CharField(max_length=100)
    course = forms.ChoiceField(choices=[], required=False)
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])

