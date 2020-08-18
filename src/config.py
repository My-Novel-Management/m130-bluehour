# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ('tatsu', 'タツヤ', 'ハシウチ,タツヤ', 20,(1,1), 'male', '高校生', "me:僕"),
            ("akane", "アカネ", "オオトリ,アカネ", 20,(1,1), "female", "謎の女性", "me:わたし"),
            ("niki", "アカネ", "ニキ,アカネ", 30,(1,1), "female", "主婦", "me:わたし"),
            ("gado", "ガドウ", "", 30,(1,1), "male", "霊媒師", "me:オレ"),
            ("dad", "アカネの父", "", 50,(1,1), "male", "新聞販売", "me:俺"),
            ("yoshi", "ヨシダ", "", 55,(1,1), "male", "不動産屋", "me:俺"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("CrossRoad", "交差点", "Tokyo"),
            ("NewspaperShop", "新聞販売店", "Tokyo"),
            ("Room", "タツヤの部屋", "Tokyo"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

