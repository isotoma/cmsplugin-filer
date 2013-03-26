from cms.models import CMSPlugin
from cmsplugin_filer_audio import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from os.path import basename
import re

class FilerAudio(CMSPlugin):
    # player settings
    audio = FilerFileField(verbose_name=_('audio file'), help_text=_('use .mp3 file'), blank=True, null=True)
    audio_url = models.CharField(_('audio url'), max_length=255, help_text=_('audio clip URL e.g. https://soundcloud.com/onusound/ghetto-priest-masters-of-deception'), blank=True, null=True)
    audio_display_title = models.CharField(_('display text'), max_length=255,help_text=_('name of audio clip that you\'d like displayed'), blank=False, null=False)
    auto_play = models.BooleanField(_('auto play'), default=settings.AUDIO_AUTOPLAY)
    loop = models.BooleanField(_('loop'), default=settings.AUDIO_LOOP)
    
    # plugin settings
    
        
    def __unicode__(self):
        if self.audio:
            name = self.audio.path
        else:
            name = self.audio_url
        return u"%s" % basename(name)

    def get_audio(self):
        if self.audio:
            return self.audio.url
        else:
            return self.audio_url

    def get_autoplay(self):
        if self.auto_play:
            return 'autoplay' 
        else:
            return ''
    
    def get_loop(self):
        if self.loop: 
            return 'loop' 
        else:
            return ''
