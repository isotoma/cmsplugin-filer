from django import forms
from cmsplugin_filer_audio.models import FilerAudio

class AudioForm(forms.ModelForm):
    
    class Meta:
        model = FilerAudio
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
