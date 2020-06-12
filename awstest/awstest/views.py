from django.shortcuts import render
from django.http.response import HttpResponse
import logging
import traceback

logger = logging.getLogger(__name__)

def index(request):
    try:
        return render(request, "index.html")
    except:
        logging.error("".join(traceback.format_list()))
