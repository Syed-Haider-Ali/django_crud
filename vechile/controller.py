from utils.reusable_classes import BaseAPIController
from .serializer import *
from .filters import *


class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter

class MakeController(BaseAPIController):
    serializer_class = MakeSerializer
    filterset_class = MakeFilter