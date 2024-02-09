from django import forms 
from .models import Room

class createRoomForm(forms.ModelForm):
    """For creating a form"""
    class Meta:
        """contents"""
        model = Room # the model associated with the form.
        fields = [
            'host', # room creator
            'name', # name of room
            'description', # short desc about the room
            'topic' # topic emphasis for the room
        ]

# add other forms here...