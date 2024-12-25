"""Config flow for MinerTimer."""
from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.core import callback
import logging
import voluptuous as vol

from .const import DOMAIN
from .oauth2 import MinerTimerOAuth2Implementation

class OAuth2FlowHandler(
    config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN
):
    """Config flow for OAuth2."""

    DOMAIN = DOMAIN
    VERSION = 1

    @property
    def logger(self):
        """Return logger."""
        return logging.getLogger(__name__)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if not user_input:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({}),
            )

        implementation = MinerTimerOAuth2Implementation(self.hass)
        await self.hass.async_add_executor_job(
            self.hass.auth.auth_providers[0].async_register_implementation,
            implementation
        )

        return await self.async_step_pick_implementation()

    @callback
    def async_get_options_flow(config_entry):
        """Get options flow."""
        return OptionsFlowHandler(config_entry) 