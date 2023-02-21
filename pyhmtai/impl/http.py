import aiohttp
import requests
import typing as t
from contextlib import AsyncContextDecorator, ContextDecorator

from data.routes.nsfw import NsfwData
from data.routes.sfw import SfwData
from data.constants import BASE_API_URL
from api.http import HmtaiHttpAware, AIOHmtaiHttpAware

RequestTypes = t.Literal["nsfw", "sfw"]
Endpoints = t.Union[NsfwData, SfwData]

API_URL = "{base}/{req_type}/{point}"

class HmtaiHttp(HmtaiHttpAware, ContextDecorator):
    _session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def request_image(self, request_type: RequestTypes, endpoint: Endpoints) -> requests.Response:
        if request_type is not None and endpoint is not None:           
            return self._session.get(API_URL.format(base=BASE_API_URL, req_type=request_type, point=endpoint))

    def check_api_status(self, request_type: RequestTypes) -> str:
        if request_type is not None:
            return self._session.get(f"{BASE_API_URL}/{request_type}").status_code


class AIOHmtaiHttp(AIOHmtaiHttpAware, AsyncContextDecorator):
    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        return False

    async def get(self, url: str) -> aiohttp.ClientResponse:
        session = aiohttp.ClientSession()
        response_data = await session.get(url)

        return response_data


    async def request_image(self, request_type: RequestTypes, endpoint: Endpoints) -> aiohttp.ClientResponse | None:
        if request_type is not None and endpoint is not None:
            we_do_a_little_url = API_URL.format(base=BASE_API_URL, req_type=request_type, point=endpoint)
            return await self.get(url=we_do_a_little_url)

    async def check_api_status(self, request_type: RequestTypes) -> str | None:
        if request_type is not None:
            return (await self.get(f"{BASE_API_URL}/{request_type}")).status
