import time
from django.http import Http404
from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

def index(request):
    # main index page
    # can use the Django models objects here if we like
    template = loader.get_template('propinfo/index.html')
    context = {} # can add info here to be put into the template by tag name
    return HttpResponse(template.render(context, request))


def detail(request): # , program_id):
    # show the detail view from a POST request
    # GET vs POST:  https://www.w3schools.com/tags/ref_httpmethods.asp
    # and we are not yet using Django Forms but could:  https://docs.djangoproject.com/en/3.2/topics/forms/

    # get the program_id the user gave on the page
    program_id = request.POST["id"]

    # get prop info from the DB

    # !!! THIS IS JUST A HACK TILL WE CONNECT UP THE DB) !!!

    if str(program_id) == "525":
        template = loader.get_template('propinfo/detail.html')
        context = {
            'proposal_id': 525,
            'request_date': time.strftime('%a %b %d %H:%M:%S %Z %Y', time.localtime()),
            'proposal_title': 'Catching an AGN in the Act: A New Accretion Regime for 1ES 1927+654',
            'proposal_type': 'GO',
            'proposal_pi': 'Tony R.',
            'proposal_pi_inst': 'Space Telescope Science Institute',
            'proposal_cycle': 25,
            'proposal_allocation': '2 orbits',
            'proposal_proprietary_period': '6 months',
            'proposal_pc_info': { 'name': 'Tony R.', 'email': 'his_email@stsci.edu', 'tele': '410-123-1234' },
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('propinfo/not_found.html')
        context = {
            'prop_id': program_id,
        }
        return HttpResponse(template.render(context, request))
