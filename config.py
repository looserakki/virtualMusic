from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAOSxIXTcYySfkWKac5GH6vOtTyUbYd2M76QHmeP0W5HzBLIMkPI8tv4bvmBChxE1cKSm3UsBmOxDXGPE0ia0gW0KTYuiWCzWXffYD2F0Jsb8SHShUGvKx81wwBWpifo086IunLkVFb0SgjU5NTPQ7_h6w2NsZxfxTIUo6YgaaZz46rda_FQj6xb_xzV8nU7MH7aryl1m6ZhlRUVd9HirsYG7PJ8-RAyCf-s6UEt3s1YVMMCYtC54gm3_qTiF3ivT7K0f4JbuiRkilveiPninfU9WLA_oAO3nLyqgXu8wQ4nTm3DvcTSZzg-1tMpBnMLy4g6-kn1BXIUleYL6FLn7vrb6crEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAGdj_UpflyimraBPr-MRHi8PtVMwKZMWr4")
BOT_NAME = getenv("BOT_NAME", "PATRICIA")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
