from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN


class DLNASyncFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a DLNA Sync config flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if self._async_current_entries():
            # There is already a DLNA Sync config entry
            return self.async_abort(reason="single_instance_allowed")

        # Present the user with a form to enter the media file path and MIME type
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=DLNASyncFlowHandler.schema())

        # Save the user's input as options for the component
        return self.async_create_entry(title="DLNA Sync", data=user_input)

    @staticmethod
    @callback
    def schema():
        """Return the schema for the user form."""
        return vol.Schema(
            {
                vol.Required("media_path"): str,
                vol.Required("mime_type"): vol.In(
                    [
                        "audio/mp3",
                        "audio/flac",
                        "audio/wav",
                        "audio/x-m4a",
                        "video/mp4",
                        "video/avi",
                        "video/x-matroska",
                    ]
                ),
            }
        )
