# -*- coding: utf-8 -*-
'''
Stage: "$tatsuの自室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def confess_thought(w: World):
    return w.scene('告白したい',
            w.plot_note("$tatsuは何とか卒業までに告白したいと考える"),
            "新聞販売店と交差点、自室以外は出さない。地縛霊であることを徐々に感じさせるためにどこかに違和感を置いておく",
            "$tatsuの知る新聞屋の彼女とは年齢が異なっている。それは死後十五年経ってしまっているから",
            )


def sameday(w: World):
    return w.scene("目覚めたら同じ日",
            w.plot_note("翌日、また五分遅れたと思って目覚めたが、日にちが三月十三日のままだった"),
            )


def thinking_her(w: World):
    return w.scene("ブルーアワーの君について",
            w.plot_note("その上彼女はブルーアワーが終わるとともにその存在が突然目の前から消えてしまうのだ"),
            w.plot_note("彼女と交流できない、もどかしい日々が続く"),
            )


def passed_seasons(w: World):
    return w.scene("過ぎ去る季節",
            w.plot_note("日付はずっと三月十三日から動かず、それなのに周囲の季節は移り変わっていく"),
            )
