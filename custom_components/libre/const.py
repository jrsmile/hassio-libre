"""Constants for the Libre integration."""
from logging import Logger, getLogger
# This is the internal name of the integration, it should also match the directory
# name for the integration.
DOMAIN = "libre"
LOGGER: Logger = getLogger(__package__)