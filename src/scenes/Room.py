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
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene('告白したい',
            w.cmd.change_stage("Room"),
            w.plot_note("$tatsuは何とか卒業までに告白したいと考える"),
            "新聞販売店と交差点、自室以外は出さない。地縛霊であることを徐々に感じさせるためにどこかに違和感を置いておく",
            "$tatsuの知る新聞屋の彼女とは年齢が異なっている。それは死後十五年経ってしまっているから",
            # NOTE: omit
            )


def sameday(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("目覚めたら同じ日",
            w.cmd.change_stage("Room"),
            w.plot_note("翌日、また五分遅れたと思って目覚めたが、日にちが三月十三日のままだった"),
            ta.be("目覚めた"),
            ta.do("時刻を見るといつも通り、きっちり五分遅れだ"),
            ta.do("慌てて準備をしがてら、小さなテレビの電源を入れると昨日と同じニュースを流していた"),
            ta.do("何かがおかしいと感じて、携帯電話の日時を確かめる"),
            ta.do("それは三月十三日のままだった"),
            )


def thinking_her(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("ブルーアワーの君について",
            w.cmd.change_stage("Room"),
            w.plot_note("その上彼女はブルーアワーが終わるとともにその存在が突然目の前から消えてしまうのだ"),
            w.plot_note("彼女と交流できない、もどかしい日々が続く"),
            ta.be(),
            ta.think("交差点の彼女、ブルーアワーの君について考えていた"),
            ta.think("何故かいつもブルーアワーの時だけあの交差点に現れる彼女"),
            ta.do("あれから気になって、何度も時間外に交差点に行ってみたが、そこに彼女の姿はなかった"),
            ta.do("きっちり三月十三日のブルーアワーにだけ現れる"),
            ta.do("天気が悪くブルーアワーにならない日には現れない"),
            ta.think("この不思議な現象が続くのも、彼女に出会ってからだった"),
            ta.think("彼女はどこかで見覚えがあるような気がしたが、思い出せない"),
            )


def passed_seasons(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("過ぎ去る季節",
            w.cmd.change_stage("Room"),
            w.plot_note("日付はずっと三月十三日から動かず、それなのに周囲の季節は移り変わっていく"),
            ta.be(),
            ta.do("部屋で一人、カレンダーを見つめていた"),
            ta.do("床に置いた新聞は、日付が三月十三日",
                "今日だ"),
            ta.think("並んでいる新聞が全て三月十三日のものばかりだった"),
            ta.do("丁寧に新聞を重ねて、縛る"),
            ta.do("大量の三月十三日の同じ記事の新聞が縛られ、それが部屋の片隅に積み上がっていた"),
            ta.do("しかし窓の外を見れば、遠くの桜並木はすっかり枯れ果て、そこに雪が積もっている",
                "春は過ぎ去り、夏も超えて、秋から冬になる"),
            ta.think("一体何が起こっているんだろう"),
            ta.think("そう思いながらも、$Sは同じ毎日を過ごすことを続けていた"),
            )
