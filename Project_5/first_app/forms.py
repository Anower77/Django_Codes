from django import forms  
from django.core import validators 

# widgets = field to html input 

class contactForm(forms.Form):
    name = forms.CharField(label = "Full Name : ", help_text="Totla length must be within 70 characters", required=False, widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter you name'}))
    # file = forms.FileField()
    # email = forms.EmailField(label = "Email Name")
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type': 'datetime-local'}))
    # choice field 
    CHOICES = [('S', 'Small'), ('M', 'Meduim'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    MEALS = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEALS, widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # This is lendthy process 
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['name']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("You email must contain .com")
#     #     return valemail

    
#     # Short cuts ways / Manual ways 
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     valname = self.cleaned_data['name']
#     #     valemail = self.cleaned_data['email']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("You email must contain .com")


# custom function
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")


class StudentData(forms.Form):
    name = forms.CharField(validators = [validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])
    text = forms.CharField(widget=forms.TextInput, validators = [len_check])
    email = forms.CharField(validators = [validators.EmailValidator(message="Enter valid Email...")])
    age = forms.IntegerField(validators = [validators.MaxValueValidator(34, message="Enter higest 34 age not more"), validators.MinValueValidator(24, message="Enter minimum age 24 not less then")])
    file = forms.FileField(validators = [validators.FileExtensionValidator(allowed_extensions = ['pdf', 'png'], message="File Extension must be ended with (.pdf) (.png)")])





# Password validaton project
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self):
        cleaned_data = super().clean()
        val_name = cleaned_data.get('name')
        val_pass = cleaned_data.get('password')
        val_conpass = cleaned_data.get('confirm_password')


        # logic 
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match..!!")
        
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be 15 characters...")
        















