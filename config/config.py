import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "19893481"))
API_HASH = getenv("API_HASH", "695b2e447b8aeb79966ff572210b0bc1")
BOT_TOKEN = getenv("BOT_TOKEN", "5625397650:AAH90ledMbxHZSiXUJtqC9U2vJpv2TKr68U")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rajputt123:956981@cluster0.ssjtqq1.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001810356172"))
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


STRING1 = getenv("STRING_SESSION", "BQCwruFGMBNtE7WwW8ptu9O6nQr_12mN6qR52a3lEQ2LaQ6niCRaKl8g1pZOrSLjS9h3ygCCYbcDCogEqOEFMESw6YaJek7smSkLBAmFF4s7v_byduZ8dan1DbFNg1RmeQDd3vHsetZBzZOmBAYlvVIq156uj228MwNQjZh5-iOyX2ofmfxTbB_6uOmaGQJzj84_lJRaWxf2lTdt_0CqROwIZvR31ztYXb8opCxELctorINgfH5a7M3OEL4gnxiZMgIB_xVNEf0FD6YrlcjgAWut7N_3mEMgO4DpKB4F9Mtn8LmSnBfKfenIu7S1AE58VqjnGcmRMgu_Nv7rc6OgTi7MAAAAATVKMpwA")
STRING2 = getenv("STRING_SESSION2", "BQAVTycFtw-QtfzAosD-Qrk9qllOEc_rExUV7K0cnn_ZYTfLNMvLTxbo3S5ygAVsz4dzg17guHGmNIiu29ZPFJra5xnyhiCBgqDCydWum0McH0idD4eQgFxeMtTcXB_XaJnDSlKALgrvDFebQKz7EjSyjNwsN8Rol-9R9YI3PPHHWNLQlTv1D2CTauy_kyVcWpk0f_wZDqEz5B3E8WrLn_I-_4EuUO34f7fLoeuIatLWPXCqPgQuoHjr2CgJwgOXBLOR7Km3Hqu8LEpedQ_v-QgPikAs7DULmekZ_TQRwwLuUkqHqbG5nBd_6VCq3K3i44R1NPTwXwXz8_LneepjVMTSAAAAAS1bwYYA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
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
