from django.forms.models import inlineformset_factory
from .models import Course, Module


ModuleFormSet = inlineformset_factory(Course,  # Parent
                                      Module,  # Child
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)
