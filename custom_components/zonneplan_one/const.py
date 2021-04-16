"""Constants for the Zonneplan ONE integration."""

from homeassistant.const import (
    ENERGY_KILO_WATT_HOUR,
    POWER_WATT,
    VOLUME_CUBIC_METERS,
)

DOMAIN = "zonneplan_one"


"""Available sensors"""
SENSOR_TYPES = {
    # Inverter
    "highest_measured_power_value": [
        "pv_installation",
        "pv_installation.meta.highest_measured_power_value",
        "Highest yield value",
        POWER_WATT,
        "mdi:solar-power",
        False,
    ],
    "highest_power_measured_at": [
        "pv_installation",
        "pv_installation.meta.highest_power_measured_at",
        "Highest yield",
        "date",
        "mdi:calendar",
        False,
    ],
    "total_power_measured": [
        "pv_installation",
        "pv_installation.meta.total_power_measured",
        "Yield total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:solar-power",
        True,
    ],
    "last_measured_power_value": [
        "pv_installation",
        "pv_installation.meta.last_measured_power_value",
        "Last measured value",
        POWER_WATT,
        "mdi:solar-power",
        True,
    ],
    "first_measured_at": [
        "pv_installation",
        "pv_installation.meta.first_measured_at",
        "First measured",
        "date_time",
        "mdi:calendar-clock",
        False,
    ],
    "last_measured_at": [
        "pv_installation",
        "pv_installation.meta.last_measured_at",
        "Last measured",
        "date_time",
        "mdi:calendar-clock",
        True,
    ],
    "total_today": [
        "pv_installation",
        "live_data.total",
        "Yield today",
        ENERGY_KILO_WATT_HOUR,
        "mdi:solar-power",
        True,
    ],
    # P1
    "electricity_total_today": [
        "p1_installation",
        "electricity.measurement_groups.0.total",
        "Electricity today",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power",
        True,
    ],
    "electricity_last_measured_delivery_value": [
        "p1_installation",
        "p1_installation.meta.electricity_last_measured_delivery_value",
        "Electricity delivery",
        POWER_WATT,
        "mdi:power",
        True,
    ],
    "electricity_last_measured_production_value": [
        "p1_installation",
        "p1_installation.meta.electricity_last_measured_production_value",
        "Electricity production",
        POWER_WATT,
        "mdi:power",
        True,
    ],
    "electricity_last_measured_average_value": [
        "p1_installation",
        "p1_installation.meta.electricity_last_measured_average_value",
        "Electricity average",
        POWER_WATT,
        "mdi:power",
        True,
    ],
    "electricity_first_measured_at": [
        "p1_installation",
        "p1_installation.meta.electricity_first_measured_at",
        "Electricity first measured",
        "date_time",
        "mdi:calendar-clock",
        False,
    ],
    "electricity_last_measured_at": [
        "p1_installation",
        "p1_installation.meta.electricity_last_measured_at",
        "Electricity last measured",
        "date_time",
        "mdi:calendar-clock",
        True,
    ],
    "electricity_last_measured_production_at": [
        "p1_installation",
        "p1_installation.meta.electricity_last_measured_production_at",
        "Electricity last measured production",
        "date_time",
        "mdi:calendar-clock",
        True,
    ],
    "gas_total_today": [
        "p1_installation",
        "gas.measurement_groups.0.total",
        "Gas today",
        VOLUME_CUBIC_METERS,
        "mdi:gas-cylinder",
        True,
    ],
    "gas_last_measured_value": [
        "p1_installation",
        "gas.contracts.0.meta.gas_last_measured_value",
        "Gas last measured value",
        VOLUME_CUBIC_METERS,
        "mdi:gas-cylinder",
        True,
    ],
    "gas_first_measured_at": [
        "p1_installation",
        "gas.contracts.0.meta.gas_first_measured_at",
        "Gas first measured",
        "date_time",
        "mdi:calendar-clock",
        False,
    ],
    "gas_last_measured_at": [
        "p1_installation",
        "gas.contracts.0.meta.gas_last_measured_at",
        "Gas last measured",
        "date_time",
        "mdi:calendar-clock",
        True,
    ],
}