#! python3
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------
#   File        : landing/views.py
#   Description : view for website landing page
#
# Copyright © 2020, Jordan Williams
# ---------------------------------------------------------------------------


from django.http import HttpResponse
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'landing.html'
