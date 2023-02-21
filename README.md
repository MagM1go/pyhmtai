# PyHMTai
Simple python port of HMtai

# Examples
```python
from pyhmtai import PyHMTai, AIOPyHMTai

sync_api = PyHMTai()
async_api = AIOPyHMTai()

sync_api.nsfw_image(endpoint="ass")
await async_api.nsfw_image(endpoint="ass")
```
