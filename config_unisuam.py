#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login="unisuampolofortalezace",
    password="Unisuam@2019",
    like_per_day=1000,
    comments_per_day=30,
    tag_list=["fortaleza", "ceara", "lagoadoparaiso", "terradaluz", "l:213428557"],
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
        ["Venha conhecer", "Conheça"],
        ["os melhores cursos"],
        [
            "à Distancia",
            "à DISTANCIA",
            "à Distância",
            "à DISTÂNCIA",
            "à distância",
        ],
        [".", "..", "...", "!", "!!", "!!!"],
    ]
)

bot.mainloop()