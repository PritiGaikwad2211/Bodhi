from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':' Your name'}),label='name',max_length=50,min_length=4,required=True)
    emailid=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Emailid'}),label='emailid',max_length=50,min_length=8,required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'subject'}),label='subject',max_length=50,min_length=8,required=True)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}),label='Message',max_length=200,min_length=10,required=True)
    mobileno=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Your Mb. No.'}),label='Mb. no',max_length=10,min_length=10,required=True)

    