from utils.reusable_classes import BaseAPIController
from .serializer import *
from .filters import *
import openpyxl

from utils.response_messages import *
from utils.reusable_methods import *
from .models import *


class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter

class MakeController(BaseAPIController):
    serializer_class = MakeSerializer
    filterset_class = MakeFilter
