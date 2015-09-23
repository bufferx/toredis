__import__('pkg_resources').declare_namespace(__name__)

version = '0.1.4'
version_info = (0, 1, 4)

from toredis.client import Client
from toredis.pipeline import Pipeline
from toredis.pool import ClientPool
