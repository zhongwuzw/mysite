from django import forms
from django.forms.widgets import Widget
class SubjectInput(forms.TextInput):
    def reder(self,name,value,attrs=None):
        return '$ %s' % super(SubjectInput,self).render(name,value,attrs)
    
    
class Contactform(forms.Form):
    subject = forms.DecimalField(decimal_places=2,widget = SubjectInput())
#     subject = SubjectInput(max_length = 100)
    email = forms.EmailField(required=False,label='Your e-mail  address')
    message = forms.CharField(widget=forms.Textarea)