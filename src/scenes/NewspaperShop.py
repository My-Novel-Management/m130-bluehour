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
    dad = w.get('dad')
    return w.scene('家族のような',
            w.cmd.change_stage("NewspaperShop"),
            w.plot_note("新聞屋に戻ってその女性のことを話すと最近はストーカーや変質者が多いという話になる"),
            w.plot_note("$tatsuはこの新聞販売店に中学の頃から世話になっている",
                "店主は父親とも旧知の仲で、カメラ店を営んでいたが経営不振から店を畳み、今は隣町の食品工場まで出稼ぎにいっている"),
            w.plot_note("貧しくはあったが、自分で金を稼いでなんとか大学に行く費用も貯めた"),
            w.plot_note("そんな$tatsuは店の娘である、年上の$akaneに恋心を抱いていた"),
            w.plot_note("$akaneは最近妙な男性のアプローチに困っていると話す",
                "彼氏でも作れという母親に対して$akaneは「そんなのいない」とつっぱねる"),
            "新聞販売店の外観から、その前に停車しているバンを見せておく",
            "新聞記事には「交通事故死」についての話が掲載されている",
            "天気予報も見せておく",
            "店内の、特に奥に事務所があり、入ったところに集配所があること",
            ta.come("新聞配達から戻ってくる$S"),
            dad.be(),
            akane.be(),
            dad.do("遅めの時間に起きてくる配達員に新聞を配っている大柄な男性"),
            "$akaneの父親はここで初出だが、そこまで詳細に描かなくていい。ただ世話になっているなどの情報は追加",
            akane.do("更にその若い子たちに笑顔で挨拶している女性"),
            akane.do("中学の頃から世話になっている店の一人娘の$akaneだった"),
            "$akaneについては詳細に描写しておく。交差点の女性と同一人物だと、あとで分かるように見た目は化粧っけがなく、髪は長いものを結んでいる",
            akane.talk("あ、おつかれさま",
                "さっき、ひょっとしてブルーアワーだった？"),
            ta.talk("あ、ええ"),
            akane.talk("どう？"),
            ta.do("$akaneに写真の方を聞かれる"),
            ta.talk("なんか、撮り逃しちゃいました"),
            akane.talk("そっかー、それは残念",
                "結局卒業式までに約束の写真、撮れそうにないか"),
            ta.talk("まだ、明日の朝がありますから", "明日は絶対に"),
            ta.do("新聞の天気予報では明日は曇りから雨だった"),
            ta.think("駄目かも知れないと思う"),
            ta.think("なんとかそれを渡して告白したいと思っていたが、どうにも難しそうだった"),
            )


def sameday2(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    dad = w.get('dad')
    return w.scene("やはり同じ三月十三日",
            w.cmd.change_stage("NewspaperShop"),
            "ここで同じ三月十三日を繰り返していると知らせると共に、違和感を抱かせる",
            "また最初のところで話せなかったこと、進学や将来、彼女への思いなどを語らせる",
            ta.be(),
            dad.be(),
            akane.be(),
            ta.do("店にやってきて新聞を確認すると三月十三日だった"),
            dad.talk("おう、どうした？", "何か面白い記事でもあったか？"),
            ta.talk("あ、いえ"),
            akane.talk("ねえ、$tatsu君は大学に行って何を勉強するの？",
                "やっぱりカメラ？"),
            ta.think("それは昨日と同じ質問だった"),
            ta.talk("経営とか社会学とか、いろいろ興味はありますけど、",
                "またここに戻ってくるのは駄目ですか？"),
            dad.talk("何だよ",
                "お前は一生新聞配達で終わりたいのか？"),
            ta.talk("新聞は、みなさんの生活を支える大事なものですから"),
            ta.talk("それに、新聞配達、大好きなんです"),
            akane.talk("よかったねー、お父さん", "跡継ぎに恵まれたよ"),
            dad.talk("何言ってんだ",
                "$meはまだまだそんな歳じゃねえよ",
                "それより$akaneはどうなんだ？",
                "将来とかちゃんと考えてんのか？"),
            akane.talk("$meはそうだな、",
                "ごく普通の幸せがあればそれで充分だよ"),
            dad.talk("何だよそりゃ"),
            )
