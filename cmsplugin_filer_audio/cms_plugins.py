import os
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filer_audio import settings
from cmsplugin_filer_audio.models import FilerAudio
from cmsplugin_filer_audio.forms import AudioForm
from filer.settings import FILER_STATICMEDIA_PREFIX

class FilerAudioPlugin(CMSPluginBase):
    module = 'Filer'
    model = FilerAudio
    name = _("Audio")
    form = AudioForm

    render_template = "cmsplugin_filer_audio/audio.html"
    text_enabled = True

    general_fields = [
        ('audio', 'audio_url'),
        'audio_display_title',
        'auto_play',
        'loop',
    ]
    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(FilerAudioPlugin)
