from django import forms
from .models import GENDER_CHOICES, Addcourse, Payfee,Studentmodel

class AddCourseForm(forms.ModelForm):
    course = forms.CharField(max_length=200,label="Course Name")
    fee = forms.CharField(max_length=100,label="Fee")
    duratoin = forms.CharField(max_length=100,label="Duratoins")

    class Meta:
        model = Addcourse
        fields = ('course','fee','duratoin')


class FeeForm(forms.ModelForm):
    fee=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit = forms.CharField(max_length=50,label="Deposit ")

    class Meta:
        model =Payfee
        fields = ('course','deposit','panding_fee')

class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    father_name = forms.CharField(max_length=10)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    age = forms.IntegerField()
    mobile_no = forms.IntegerField()
    address = forms.CharField(max_length=200)

    class Meta:
        model = Studentmodel
        fields = ('roll_no','name','father_name','gender', 'age','mobile_no','course','address',)
