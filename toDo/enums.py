from enum import Enum
from django.utils.translation import ugettext_lazy as _


class StatusList(Enum):
    COMPLETED = "COMPLETED"
    TODO = "TO-DO"
    ONGOING = "ONGOING"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.TODO), _('TO-DO')),
            (str(cls.ONGOING), _('ONGOING')),
            (str(cls.COMPLETED), _('COMPLETED')),
        )
