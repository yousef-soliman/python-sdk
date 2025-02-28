import typing

from src.exception.exceptions import GeneralError
from src.open_feature_client import OpenFeatureClient
from src.provider.provider import AbstractProvider

_provider = None


def get_client(name: str = None, version: str = None) -> OpenFeatureClient:
    if _provider is None:
        raise GeneralError(
            error_message="Provider not set. Call set_provider before using get_client"
        )
    return OpenFeatureClient(name=name, version=version, provider=_provider)


def set_provider(provider: AbstractProvider):
    global _provider
    if provider is None:
        raise GeneralError(error_message="No provider")
    _provider = provider


def get_provider() -> typing.Optional[AbstractProvider]:
    global _provider
    return _provider
