__version__ = "1.0.0"
__author__ = "Robert Singer"
__author_email__ = "robertgsinger@gmail.com"


class NotSet(object):
    pass


from .decorators import hook
from .mixins import LifecycleModelMixin
from .hooks import *

from .models import LifecycleModel
