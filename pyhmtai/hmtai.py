import typing as t

from pyhmtai.impl.http import HmtaiHttp, AIOHmtaiHttp
from pyhmtai.data.routes.nsfw import NsfwData
from pyhmtai.data.routes.sfw import SfwData
from pyhmtai.data.exceptions import ApiNotAvailable


class PyHMTai:
    _http = HmtaiHttp()

    def nsfw_image(self, endpoint: NsfwData) -> t.Dict[str, str] | None:
        request_type = "nsfw"

        if self._http.check_api_status('nsfw') != 200:
            raise ApiNotAvailable("Api may not working, try later.")
    
        with self._http as api:
            return api.request_image(request_type, endpoint).json()

    def sfw_image(self, endpoint: SfwData) -> t.Dict[str, str] | None:
        request_type = "sfw"

        if self._http.check_api_status('sfw') != 200:
            raise ApiNotAvailable("Api may not working, try later.")

        with self._http as api:
            return api.request_image(request_type, endpoint).json()


class AIOPyHMTai:
    _http = AIOHmtaiHttp()

    async def nsfw_image(self, endpoint: NsfwData) -> t.Dict[str, str]:
        request_type = "nsfw"
        
        if await self._http.check_api_status('nsfw') != 200:
            raise ApiNotAvailable("Api may not working, try later.")
    
        async with self._http as api:
            return await api.request_image(request_type, endpoint)

    async def sfw_image(self, endpoint: SfwData) -> t.Dict[str, str]:
        request_type = "sfw"

        if await self._http.check_api_status('sfw') != 200:
            raise ApiNotAvailable("Api may not working, try later.")

        async with self._http as api:
            return await api.request_image(request_type, endpoint)
