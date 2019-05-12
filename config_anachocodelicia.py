#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login="anachocodelicia00",
    password="Ana@2019",
    like_per_day=1000,
    comments_per_day=60,
    tag_list=["l:213665700"], #, "chocolate", "doces","ovosdechocolate", "ovosdepascoa", "querochocolate", "queroovos", "chocolatra","ovodecolher", "amochocolate", "presentedepascoa", "presentedechocolate", "medachocolate"],
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
        ["Temos delícias para todos os gostos!", "Chocolate do jeito que você gosta... Escolha seu recheio e sua casca!","Olá! Já viu nossos doces de chocolate?!", "Olá! Visite nossa página e veja as nossas delícias!", "Gosta de chocolate? Venha nos conhecer!"],
    ]
)

bot.mainloop()