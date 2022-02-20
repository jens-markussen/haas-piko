"""The Kostal piko integration."""

import logging

from .piko import Piko

from homeassistant.const import (
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_HOST,
    CONF_MONITORED_CONDITIONS,
)

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle


from .const import SENSOR_TYPES, MIN_TIME_BETWEEN_UPDATES, DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Add an Kostal piko entry."""
    # Add the needed sensors to hass
    piko = Piko(
        entry.data[CONF_HOST], entry.data[CONF_USERNAME], entry.data[CONF_PASSWORD]
    )
    entities = []

    for sensor in entry.data[CONF_MONITORED_CONDITIONS]:
        entities.append(PikoSensor(piko, sensor, entry.title))
    async_add_entities(entities)


class PikoSensor(Entity):
    """Representation of a Piko inverter sensor."""

    def __init__(self, piko, sensor_type, name):
        """Initialize the sensor."""
        self._sensor = SENSOR_TYPES[sensor_type][0]
        self._name = name
        self.type = sensor_type
        self.piko = piko
        self._unit_of_measurement = SENSOR_TYPES[self.type][1]
        self._icon = SENSOR_TYPES[self.type][2]
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{} {}".format(self._name, self._sensor)

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement this sensor expresses itself in."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return icon."""
        return self._icon

    @property
    def unique_id(self):
        """Return unique id based on device serial and variable."""
        return "{} {}".format("piko", self._sensor)

    @property
    def device_info(self):
        """Return information about the device."""
        return {
            "identifiers": {(DOMAIN, "piko")},
            "name": self._name,
            "manufacturer": "Kostal"
        }

    def update(self):
        """Update data."""
        if data is not None:
            if self.type == "current_power":
                return self.piko.get_current_power()
            elif self.type == "total_energy":
                return self.piko.get_total_energy()
            elif self.type == "daily_energy":
                return self.piko.get_daily_energy()
            else:
                return None
