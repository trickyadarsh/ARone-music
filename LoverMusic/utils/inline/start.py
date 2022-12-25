from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from LoverMusic import app
def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⁣𓆩𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽𓆪",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝗦𝗘𝗧𝗧𝗜𝗡𝗚", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗔𝗟𝗟 𝘂𝗽𝗱𝗮𝘁𝗲", url=f"https://t.me/Lover_Music_Support"),
            InlineKeyboardButton(
                text="𝗺𝗮𝗶𝗻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗚", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/shubhamsah1"):
    buttons = [
        [
            InlineKeyboardButton(
                text="𓆩𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽𓆪",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                    text="𓊈𝗥𝗔𝗼𝗻𝗲𓊉", url=f"https://t.me/shubhamsah1"}"
                
        ],
        [
            InlineKeyboardButton(text="𝗔𝗟𝗟 𝘂𝗽𝗱𝗮𝘁𝗲", url=f"https://t.me/Lover_Music_Support"),
            InlineKeyboardButton(
                text="𝗺𝗮𝗶𝗻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗚", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
    
     ]
    return buttons
