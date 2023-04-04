import logging
import time
import voluptuous as vol
from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import STATE_IDLE, STATE_PAUSED, STATE_PLAYING
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import Dict, Any
from upnp_ssdp import SSDP
from upnp_client import Device
from upnp_client.upnp import DIDLLite
from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)


class DLNASyncMediaPlayer(MediaPlayerEntity):
    """DLNA Sync media player for Home Assistant."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        """Initialize the DLNA Sync media player."""
        self.hass = hass
        self.entry = entry
        self._state = STATE_IDLE
        self._media_path = entry.data["media_path"]
        self._mime_type = entry.data["mime_type"]
        self._devices = []

    async def async_added_to_hass(self):
        """Handle when the entity is added to Home Assistant."""
        await super().async_added_to
