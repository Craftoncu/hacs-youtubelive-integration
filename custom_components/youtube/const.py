"""Constants for YouTube integration."""
import logging

DEFAULT_ACCESS = ["https://www.googleapis.com/auth/youtube.readonly"]
DOMAIN = "youtube"
MANUFACTURER = "Google, Inc."
CHANNEL_CREATION_HELP_URL = "https://support.google.com/youtube/answer/1646861"

CONF_CHANNELS = "channels"
CONF_ID = "id"
CONF_UPLOAD_PLAYLIST = "upload_playlist_id"
COORDINATOR = "coordinator"
AUTH = "auth"

LOGGER = logging.getLogger(__package__)

ATTR_TITLE = "title"
ATTR_LATEST_VIDEO = "latest_video"
ATTR_SUBSCRIBER_COUNT = "subscriber_count"
ATTR_DESCRIPTION = "description"
ATTR_THUMBNAIL = "thumbnail"
ATTR_VIDEO_ID = "video_id"
ATTR_PUBLISHED_AT = "published_at"

ATTR_LATEST_SUPERCHAT = "latest_superchat"
ATTR_USER_NAME = "user_name"
ATTR_USER_ID= "user_id"
ATTR_AMOUNT = "ammount"
ATTR_CURRENCY = "currency"
ATTR_MESSAGE = "message"
