import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "11903116"))
API_HASH = getenv("API_HASH", "54d2190b04386eb083badd96c70fe36a")
BOT_TOKEN = getenv("BOT_TOKEN", "6243574805:AAE7QR_jXqJ1JZt9awu9ekqVxj0M6Nr4y50")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rajputt123:956981@cluster0.ssjtqq1.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-100181035612"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐑𝐀𝐨𝐧𝐞𝐗")
OWNER_ID = list(map(int, getenv("OWNER_ID", "2033800689").split()))
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/RAoneXchannel")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/RAoneXgroup")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "59006")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "10998")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SPARTENX-OP/VirusMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/RAoneX_01")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "BQCG3ZjOzD1LAuzr6s_2Tib9NWMNshW5TEyOC2jqjTytKUqHh2AkqtYzzRbNL0D4SKmmjhYFybvQxV3-ulyzQJaxM5an6vtwVjnx8IoxaOKh9vP_s2ZmrL9MR-B90_GMJo8alAQ9qXrfTfqUxsI9VKDxBSMBx6_p8H1ETwGNAFuYoVced4xo6sgHy3UOaaOZ-1LivLnVtXJMw34_pbxsdfoZCyzeAQd3Ioj_awHop7d0VHNn5Nkphi3ed5BWO8u2HLHanL8LrDtuKMsPForEzuu3oJmMUPYhvwmaCHHEWs_yRvIwcLPJ3GNI3fUEZGIz8qM9EwgYfMbxZUh4eRaC8TZSAAAAAS1bwYYA")
STRING2 = getenv("STRING_SESSION2", "BQA1muknndLJl7JDqRO1llbcD6op-Bdw3EsfNFCfSAWGsPqu7OzVNpGza3QOTiB7PvUQNFKZfiCgwYuGqtYud34U0CRwBS4TyNI9oqKk1kPBWaW0VQHuRDMpxQRv_lL-QrgcQxeTOUFJqTghLPtH1uxdRFWSt-FHAciy1pDoxvcN8ZfxB0SJy1iOxZ2G567Kj6xjcgCInbcQ8GPznfnnmCCpjC7rKcPuXo4KJnFMhxm7oq-eSqGCn_TJGKsrir8gbtPJRvuJLhmmt39tJmTpROE9ClVi9jcZ6XTk7Mo1dtsJ3Yacjaa2ITTHvQIxcXVFNvnhuE8cfZFPlKq2npjv0qNKAAAAAUBo6MgA")
STRING3 = getenv("STRING_SESSION3", "BQCwruFGMBNtE7WwW8ptu9O6nQr_12mN6qR52a3lEQ2LaQ6niCRaKl8g1pZOrSLjS9h3ygCCYbcDCogEqOEFMESw6YaJek7smSkLBAmFF4s7v_byduZ8dan1DbFNg1RmeQDd3vHsetZBzZOmBAYlvVIq156uj228MwNQjZh5-iOyX2ofmfxTbB_6uOmaGQJzj84_lJRaWxf2lTdt_0CqROwIZvR31ztYXb8opCxELctorINgfH5a7M3OEL4gnxiZMgIB_xVNEf0FD6YrlcjgAWut7N_3mEMgO4DpKB4F9Mtn8LmSnBfKfenIu7S1AE58VqjnGcmRMgu_Nv7rc6OgTi7MAAAAATVKMpwA")
STRING4 = getenv("STRING_SESSION4", "BQA9A3bqvOWaSuCruLkP71Wro_lJjeUtSz-SyYMC2oYRSf0-28Hk0KcXMTs1RovzFTB7G0iBcGej27lBZw-RzQa5aSPdXkPszzruCdwLzAv5Ux5nd6Sw7zPcJt18S9WE_-Iaurz0hZLAOJklaJvaw6AP6YnvNLn4jjMmCs4bSod8jzX49zi9u4fQrTOgneyy5MKmxeQI0mmGdtX-9hsub-atiP5GDyKLFYnhw5N0mPgAUABCyQXLIUWYhL5DEaGg5bTXQpbBxCD21Ar9h2qUl_9fs6inhvhUfJo1c3Xb2dMw8cuFf9_gOburmhaIqffaLUAl9Uor6Z-DZo1BSuK6PfY4AAAAATc34M0A")
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "viruslogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://i.postimg.cc/Kvmnc6ZF/photo-2022-12-25-02-35-34.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
