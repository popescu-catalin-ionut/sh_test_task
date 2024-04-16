from environs import Env
from common.dataclass import Documentation


env = Env()
env.read_env()

# general
VERSION: str = "1.0.0"

# security
SECRET_KEY: str = env.str("SECRET_KEY", '')  # Secret key used to sign JWT tokens

ALGORITHM: str = "HS256"  # Algorithm used to sign JWT tokens

ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token expiration time

# database
SQLALCHEMY_DATABASE_URL: str = env.str("SQLALCHEMY_DATABASE_URL", '')

# Documentation
documentation = Documentation(
    title="Spatially Health App",
    description="Spatially Health",
    summary="Spatially Health app. Test me.",
    version=VERSION,
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Spatially Health Popescu Catalin-Ionut",
        "url": "http://catalinp.example.com/contact/",
        "email": "catalinp@s-h.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }, )
