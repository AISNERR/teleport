# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aisner <aisner@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/26 06:39:57 by aisner            #+#    #+#              #
#    Updated: 2022/02/26 06:39:58 by aisner           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pyrogram import filters


@app.on_message(filters.sticker)
def my_handler(client, message):
    print(message)