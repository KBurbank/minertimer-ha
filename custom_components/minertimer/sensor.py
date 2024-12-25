"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities([MinerTimerSensor()])

class MinerTimerSensor(SensorEntity):
    """Representation of a MinerTimer sensor."""

    _attr_name = "MinerTimer Played Time"
    _attr_native_unit_of_measurement = "minutes"
    _attr_unique_id = "minertimer_played_time"

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._state = 0

    @property
    def native_value(self) -> float:
        """Return the state of the sensor."""
        return self._state 