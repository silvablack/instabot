#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login="raposo_sounet",
    password="n3g4tlv4",
    like_per_day=1000,
    comments_per_day=60,
    tag_list=["l:213665700", "propaganda", "publicidade", "l:213665700", "marketing","bar", "l:213665700", "restaurante", "houseshow", "l:213665700", "mkt", "publicidadeemarketing", "digitalinfluence"],
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60 * 60,
    unfollow_per_day=300,
    unfollow_break_min=12,
    unfollow_break_max=27,
    log_mod=0,

    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[
        ["Olá!", "Oi!"],
        ["Esteja no mundo Digital", 'Visite meu perfil e eu posso ajudar você a ter muito mais seguidores para seu negócio', "Já pensou em ter muita visibilidade na internet??"],
        [".", "..", "!", "!!"],
        ["#sounet #mundodigital"],
    ]
)

bot.mainloop()