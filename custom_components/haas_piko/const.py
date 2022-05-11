"""Constants for the Kostal piko integration."""
from datetime import timedelta

from homeassistant.const import (
    POWER_WATT,
    ENERGY_KILO_WATT_HOUR
)

DOMAIN = "kostal"

DEFAULT_NAME = "Kostal piko"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

SENSOR_TYPES = {
    "current_power": ["Current power", POWER_WATT, "mdi:solar-power"],
    "total_energy": ["Total energy", ENERGY_KILO_WATT_HOUR, "mdi:solar-power"],
    "daily_energy": ["Daily energy", ENERGY_KILO_WATT_HOUR, "mdi:solar-power"],
}