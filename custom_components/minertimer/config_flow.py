"""Config flow for MinerTimer integration."""
from __future__ import annotations

from typing import Any

from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN


class MinerTimerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MinerTimer."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="MinerTimer", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            description_placeholders={
                "my_name": "MinerTimer"
            }
        ) 