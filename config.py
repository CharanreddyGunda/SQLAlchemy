
from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class config:
        env_file = ".env" # Specify the location of the .env file


settings = Settings() # This will load the variables from the .env file
