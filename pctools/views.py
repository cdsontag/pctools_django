from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

def index(request):
    # main index page - just throw up some convenient links for us

    return HttpResponse("""
        <html>
           <body>
               <h2>Just a starter page - not intended for public use</h2>
               <ul>
                  <li><a href="https://grit.stsci.edu/observing-program-implementation/pctools/-/tree/master/">Grit</a>
                  <li><a href="https://github.com/cdsontag/pctools_django">the demo code</a>
                  <li><a href="https://www.stsci.edu/public/propinfo.html">real Program Information page</a>
                  <li><a href="propinfo">demo Program Information page</a> (in Django terms this is our propinfo "app")
               </ul>
           </body>
        </html>
    """)
