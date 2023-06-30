from django import forms
from core.models import Alert, Device, Location
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

class UpdateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ["mac", "model", "location", "latitude", "longitude"]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "description", "alert_instructions", "address", "latitude", "longitude", "radius"]

class CreateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ["project", "last_call"]