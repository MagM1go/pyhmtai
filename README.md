# PyHMTai
Simple python port of HMtai

# Examples
```python
from pyhmtai import PyHMTai, AIOPyHMTai
from pyhmtai.internal.routes import NsfwData, SfwData

sync_api = PyHMTai()
async_api = AIOPyHMTai()

sync_api.nsfw_image(endpoint=NsfwData.ass)
await async_api.sfw_image(endpoint=SfwData.ass)
```
