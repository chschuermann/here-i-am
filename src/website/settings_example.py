from website.config.common import BaseSettings
from website.config.mixins import DevMixin, ProdMixin


class DevDefaultSite(DevMixin, BaseSettings):
    pass


class ProdDefaultSite(ProdMixin, BaseSettings):
    pass
