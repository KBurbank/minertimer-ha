"""Config flow for MinerTimer."""
from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.core import callback
import logging

from .const import DOMAIN, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

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

    @property
    def client_id(self):
        """Return the client id."""
        return CLIENT_ID

    @property
    def client_secret(self):
        """Return the client secret."""
        return CLIENT_SECRET

    @property
    def redirect_uri(self):
        """Return the redirect URI."""
        return REDIRECT_URI

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        
        return await self.async_step_pick_implementation()

    @callback
    def async_get_options_flow(config_entry):
        """Get options flow."""
        return OptionsFlowHandler(config_entry) 