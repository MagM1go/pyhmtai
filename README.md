# PyHMTai
Simple python port of HMtai

# Examples
```python
from pyhmtai import PyHMTai, AIOPyHMTai
from pyhmtai.internal.routes import NsfwData, SfwData

sync_api = PyHMTai()
async_api = AIOPyHMTai()

nsfw = NsfwData
sfw = SfwData

sync_api.nsfw_image(endpoint=nsfw.ass)
await async_api.sfw_image(endpoint=sfw.wave)
```
