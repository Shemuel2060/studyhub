from django import forms 
from .models import Room
from django.contrib.auth.models import User

class createRoomForm(forms.ModelForm):
    """For creating a form"""
    class Meta:
        """contents"""
        model = Room # the model associated with the form.
        # Approach 1: include just selected fields
        # fields = [
        #     'host', # room creator
        #     'name', # name of room
        #     'description', # short desc about the room
        #     'topic' # topic emphasis for the room
        # ]
        # Approach 2: include all fields, but exclude some
        fields = '__all__' # includes all
        exclude = ['host', 'participants'] # excludes the listed ones.

# add other forms here...

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']