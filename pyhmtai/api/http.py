import typing as t
from abc import ABC, abstractmethod

from pyhmtai.data.routes.nsfw import NsfwData

TYPES = t.Literal["nsfw", "sfw"]

class HmtaiHttpAware(ABC):
    @abstractmethod
    def request_image(
        self, 
        request_type: t.Literal["nsfw", "sfw"],
        endpoint: NsfwData
    ) -> t.Dict[str, str]:
        ...

    @abstractmethod
    def check_api_status(
        self,
        request_type: t.Literal["nsfw", "sfw"]
    ) -> str:
        ...

class AIOHmtaiHttpAware(ABC):
    @abstractmethod
    async def request_image(
        self,
        request_type: t.Literal["nsfw", "sfw"],
        endpoint: NsfwData
    ) -> t.Dict[str, str]:
        ...

    @abstractmethod
    async def check_api_status(
        self,
        request_type: t.Literal["nsfw", "sfw"]
    ) -> str:
        ...
