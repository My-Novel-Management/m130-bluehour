# -*- coding: utf-8 -*-
'''
Stage: "Newspaper shop"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def familylike(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene('家族のような',
            w.cmd.change_stage("NewspaperShop"),
            w.plot_note("新聞屋に戻ってその女性のことを話すと最近はストーカーや変質者が多いという話になる"),
            w.plot_note("$tatsuはこの新聞販売店に中学の頃から世話になっている",
                "店主は父親とも旧知の仲で、カメラ店を営んでいたが経営不振から店を畳み、今は隣町の食品工場まで出稼ぎにいっている"),
            w.plot_note("貧しくはあったが、自分で金を稼いでなんとか大学に行く費用も貯めた"),
            w.plot_note("そんな$tatsuは店の娘である、年上の$akaneに恋心を抱いていた"),
            w.plot_note("$akaneは最近妙な男性のアプローチに困っていると話す",
                "彼氏でも作れという母親に対して$akaneは「そんなのいない」とつっぱねる"),
            )

