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
#        'image',
        'auto_play',
        'loop',
    ]
#    color_fields = [
#        'bgcolor',
#        'textcolor',
#        'seekbarcolor',
#        'seekbarbgcolor',
##        'loadingbarcolor',
#        'buttonoutcolor',
#        'buttonovercolor',
#        'buttonhighlightcolor',
#    ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]
#    if settings.VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS:
#        fieldsets += [
#            (_('Color Settings'), {
#                'fields': color_fields,
#                'classes': ('collapse',),
#            }),
#        ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

#    def icon_src(self, instance):
#        return os.path.normpath(u"%s/icons/video_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))
plugin_pool.register_plugin(FilerAudioPlugin)
