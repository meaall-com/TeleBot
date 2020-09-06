#!/usr/bin/env python3
# (c) https://t.me/meaallh100
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""الرجاء الانتقال إلى my.telegram.org
تسجيل الدخول باستخدام حساب Telegram الخاص بك
انقر فوق أدوات تطوير API
إنشاء تطبيق جديد بإدخال البيانات المطلوبة
بالنسبة إلى TeleBot""")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
