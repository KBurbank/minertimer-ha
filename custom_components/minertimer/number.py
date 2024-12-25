"""Platform for number integration."""
from __future__ import annotations

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the number platform."""
    async_add_entities([MinerTimerLimit()])

class MinerTimerLimit(NumberEntity):
    """Representation of a MinerTimer limit control."""

    _attr_name = "MinerTimer Time Limit"
    _attr_native_unit_of_measurement = "minutes"
    _attr_native_min_value = 0
    _attr_native_max_value = 240
    _attr_native_step = 15
    _attr_unique_id = "minertimer_limit"

    def __init__(self) -> None:
        """Initialize the number."""
        self._value = 60

    @property
    def native_value(self) -> float:
        """Return the current value."""
        return self._value

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._value = value 