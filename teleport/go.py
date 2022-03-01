# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    go.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aisner <aisner@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 06:01:21 by aisner            #+#    #+#              #
#    Updated: 2022/02/28 09:43:31 by aisner           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
from pyrogram import Client
from pyrogram import filters

# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "@PASTEL21"
PHONE_NR = '79873155897'

API_ID = 17458144
API_HASH = "c1de59310d3863bbe357b11241af88be"

app = Client( ACCOUNT, phone_number=PHONE_NR, api_id=API_ID, api_hash=API_HASH )

### CHAT ID

# Variables
SOURCE_CHAT_A =   -1001432211169
TARGET_CHAT_A =     788572973
# ~~~~~~~~~~~~~~~~~~~~~~ #

# Commands
@app.on_message(filters.chat(SOURCE_CHAT_A))
def copy_to_channel(client, message):
    message.copy(  chat_id=TARGET_CHAT_A  ) 
    print(message)

app.run()