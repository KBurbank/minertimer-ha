"""Config flow for MinerTimer."""
from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_entry_oauth2_flow

from .const import DOMAIN, CLIENT_ID, CLIENT_SECRET
from .oauth2 import MinerTimerOAuth2Implementation

async def async_get_auth_implementation(
    hass: HomeAssistant, 
    auth_domain: str,
    credential: dict[str, Any],
) -> MinerTimerOAuth2Implementation:
    """Return auth implementation."""
    return MinerTimerOAuth2Implementation(hass)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MinerTimer."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize flow."""
        self._auth_implementation: MinerTimerOAuth2Implementation | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({}),
            )

        self._auth_implementation = MinerTimerOAuth2Implementation(self.hass)

        return self.async_create_entry(
            title="MinerTimer",
            data={
                "auth_implementation": DOMAIN,
                "implementation": self._auth_implementation,
            },
        ) 