"""Sensor platform for MinerTimer."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the MinerTimer sensor."""
    async_add_entities([MinerTimerPlayedTime()])


class MinerTimerPlayedTime(SensorEntity):
    """Representation of played time sensor."""

    _attr_name = "Minecraft Played Time"
    _attr_unique_id = "minertimer_played_time"
    _attr_native_unit_of_measurement = "minutes"
    _attr_icon = "mdi:clock-outline"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_native_value = 0 