from django import forms
from django.forms.models import inlineformset_factory

from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course,  # Parent
                                      Module,  # Child
                                      fields=['title', 'description'],  # fields
                                      extra=2,  # Number of child forms
                                      can_delete=True)  # Add del checkbox
