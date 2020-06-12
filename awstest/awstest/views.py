from django.shortcuts import render
from django.http.response import HttpResponse
import logging
import logging.handlers
from django.conf import settings
import traceback

logger = logging.getLogger("error")

def index(request):
    try:
        return render(request, "index.htm")
    except:
        print("".join(traceback.format_list()))
        logging.error("".join(traceback.format_list()))
