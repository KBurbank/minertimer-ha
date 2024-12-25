"""OAuth2 implementation for MinerTimer."""
from homeassistant.core import HomeAssistant
from homeassistant.auth.providers import oauth2 as ha_oauth2
from homeassistant.components.application_credentials import (
    ClientCredential,
    AuthImplementation,
)

from .const import CLIENT_ID, CLIENT_SECRET, DOMAIN

class MinerTimerOAuth2Implementation(ha_oauth2.AbstractOAuth2Implementation):
    """OAuth2 implementation that only uses the external url."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:
        """Initialize local auth implementation."""
        self.hass = hass
        self._client_id = CLIENT_ID
        self._client_secret = CLIENT_SECRET

    @property
    def name(self) -> str:
        """Name of the implementation."""
        return "MinerTimer"

    @property
    def domain(self) -> str:
        """Domain that is providing the implementation."""
        return DOMAIN

    @property
    def client_id(self) -> str:
        """Return client ID."""
        return self._client_id

    @property
    def client_secret(self) -> str:
        """Return client secret."""
        return self._client_secret

    @property
    def authorize_url(self) -> str:
        """Return the authorize url."""
        return f"{self.hass.config.api.base_url}/auth/authorize"

    @property
    def token_url(self) -> str:
        """Return the token url."""
        return f"{self.hass.config.api.base_url}/auth/token" 