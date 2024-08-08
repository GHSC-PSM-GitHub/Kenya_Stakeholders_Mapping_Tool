from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record, Functionalarea, Rolename

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import models


class DateInput(forms.DateInput):
    input_type = 'date'

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record 
        fields = ['stakeholder_name', 'physical_location', 'Primary_contact_tel', 
                  'year_of_registration', 'partner_category', 'stakeholder_type', 
                  'county', 'functionalarea', 'rolename', 'registration_type','entry_level','budget', 'partnership_framework',  
                  'contact_email', 'notes', 'activity_reference']
        widgets = {
            'year_of_registration': DateInput(),
        }
        # fields = ['stakeholder_name', 'stakeholder_type', 'county', 'functionalarea', 'rolename', 'hiv', 'malaria', 'fp', 'mnch', 'emms', 'contact_email', 'notes', 'activity_reference']
   
    functionalarea = forms.ModelChoiceField(queryset=Functionalarea.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_rolenames/", "hx-target": "#id_rolename"}))
    widgets = {
            'county': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Render as a select dropdown with multiple selections
        }
    rolename = forms.ModelChoiceField(queryset=Rolename.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "functionalarea" in self.data:
            functionalarea_id = int(self.data.get("functionalarea"))
            self.fields["rolename"].queryset = Rolename.objects.filter(functionalarea_id=functionalarea_id)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['rolename'].queryset = Rolename.objects.none()
 
    #     if 'functionalarea' in self.data:
    #         try:
    #             functionalarea_id = int(self.data.get('functionalarea'))
    #             self.fields['rolename'].queryset = Rolename.objects.filter(functionalarea_id=functionalarea_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty rolename queryset
    #     elif self.instance.pk:
    #         self.fields['rolename'].queryset = self.instance.functionalarea.rolename_set.order_by('name') 

#  for James

#     functionalarea = forms.ModelChoiceField(queryset=Functionalarea.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "record/", "hx-target": "#id_rolename"}))
#     rolename = forms.ModelChoiceField(queryset=Rolename.objects.none())

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         if "functionalarea" in self.data:
#             functionalarea_id = int(self.data.get("functionalarea"))
#             self.fields["rolename"].queryset = Rolename.objects.filter(functionalarea_id=functionalarea_id)



#for Paul

             
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['rolename'].queryset = Rolename.objects.none()
 
    #     if 'functionalarea' in self.data:
    #         try:
    #             functionalarea_id = int(self.data.get('functionalarea'))
    #             self.fields['rolename'].queryset = Rolename.objects.filter(functionalarea_id=functionalarea_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty rolename queryset
    #     elif self.instance.pk:
    #         self.fields['rolename'].queryset = self.instance.functionalarea.rolename_set.order_by('name')


# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['stakeholder_name', 'physical_location', 'Primary_contact_tel', 
                  'year_of_registration', 'partner_category', 'stakeholder_type', 
                  'county', 'functionalarea', 'rolename', 'registration_type','entry_level','budget', 'partnership_framework',  
                  'contact_email', 'notes', 'activity_reference']
        widgets = {
            'year_of_registration': DateInput(),
        }
        # fields = ['stakeholder_name', 'stakeholder_type', 'county', 'functionalarea', 'rolename', 'hiv', 'malaria', 'fp', 'mnch', 'emms', 'contact_email', 'notes', 'activity_reference']



class cascadeForm(forms.Form):
    functionalarea = forms.ModelChoiceField(queryset=Functionalarea.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_rolenames/", "hx-target": "#id_rolename"}))
    rolename = forms.ModelChoiceField(queryset=Rolename.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "functionalarea" in self.data:
            functionalarea_id = int(self.data.get("functionalarea"))
            self.fields["rolename"].queryset = Rolename.objects.filter(functionalarea_id=functionalarea_id)
