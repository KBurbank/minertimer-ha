"""OAuth2 implementation for MinerTimer."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.components.application_credentials import (
    ClientCredential,
    AuthImplementation,
)

from .const import CLIENT_ID, CLIENT_SECRET, DOMAIN

class MinerTimerOAuth2Implementation(
    config_entry_oauth2_flow.LocalOAuth2Implementation
):
    """OAuth2 implementation that only uses the external url."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:
        """Initialize local auth implementation."""
        self.hass = hass
        
        super().__init__(
            hass,
            DOMAIN,
            ClientCredential(CLIENT_ID, CLIENT_SECRET),
            "http://localhost:8456/callback",
        )

    @property
    def name(self) -> str:
        """Name of the implementation."""
        return "MinerTimer" 