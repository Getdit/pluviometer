from django import forms
from core.models import Alert
from accounts.models import Profile


class AlertForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ['name', 'description', 'formula', 'devices']

class AssignUserProjectForm(forms.Form):
    email = forms.EmailField()

    def clean_profile(self):
        email = self.cleaned_data['email']
        profile = Profile.objects.filter(owner__email=email)
        if not profile.exists():
            raise forms.ValidationError("User does not exist")
        return profile.first()

class AssignDeviceProjectForm(forms.Form):
    mac = forms.CharField()

    def clean_profile(self):
        self.errors
        return self.cleaned_data['mac']