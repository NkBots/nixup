# MIT License

# Copyright (c) 2023 Rahul Thakor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import os


SUDO_USERS = [1953040213, 5144980226, 874964742,
              839221827, 5294965763, 5317652430, 5141357700]
TOTAL_TASKS = []
DONT_SEND_TASK = '''Please don't send new task until the previous one has been completed.

There will be time gap between two tasks which will be same as time consumed by previous task.

If you don't want to receive time gap, please consider to upgrade /plan'''


class Config(object):
    WEBHOOK = os.environ.get("BOT_TOKEN", False)
    # get a token from @BotFather
    BOT_TOKEN = "6209873095:AAEd3Lsewz2XYfWrUB0HlpowXhfL0y5whNA"

    # Get these values from my.telegram.org
    API_ID = 15004995
    API_HASH = "0209b6aa79a68ac5a101c9aeac18e8dd"

    # No need to change
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    ADL_BOT_RQ = {}
    CHUNK_SIZE = 128
    TG_MAX_FILE_SIZE = 2147483648
    HTTP_PROXY = ""
    PROCESS_MAX_TIMEOUT = 3700

    # TG Ids
    LOG_CHANNEL = -1001492018811
    OWNER_ID = 5294965763

    # bot username without @
    BOT_USERNAME = "AdvanceUrlUploaderBot"

    # auth users
    AUTH_USERS = [OWNER_ID]
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # File /video download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # TASKS = {}

    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "None")
    # If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."

    # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "None")
    # If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # Chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # Proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    OWNER_ID = int(os.environ.get("OWNER_ID", "12356"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x)
                      for x in os.environ.get("AUTH_USERS", "0").split()})
    AUTH_USERS.append(OWNER_ID)