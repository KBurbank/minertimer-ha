"""The MinerTimer integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from homeassistant.components.application_credentials import (
    ClientCredential,
    async_import_client_credential,
)

from .const import DOMAIN, CLIENT_ID, CLIENT_SECRET
from .oauth2 import MinerTimerOAuth2Implementation

PLATFORMS = ["sensor", "number"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up MinerTimer from a config entry."""
    implementation = MinerTimerOAuth2Implementation(hass)
    await hass.auth.auth_providers[0].async_register_implementation(implementation)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True 