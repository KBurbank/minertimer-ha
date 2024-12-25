"""Number platform for MinerTimer."""
from __future__ import annotations

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the MinerTimer number."""
    async_add_entities([MinerTimerLimit()])


class MinerTimerLimit(NumberEntity):
    """Representation of time limit control."""

    _attr_name = "Minecraft Time Limit"
    _attr_unique_id = "minertimer_time_limit"
    _attr_native_min_value = 0
    _attr_native_max_value = 240
    _attr_native_step = 15
    _attr_native_unit_of_measurement = "minutes"
    _attr_icon = "mdi:timer-outline"

    def __init__(self) -> None:
        """Initialize the number."""
        self._attr_native_value = 60

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._attr_native_value = value 