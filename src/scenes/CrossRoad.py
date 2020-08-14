# -*- coding: utf-8 -*-
'''
Stage: "Crossroad"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def bluehour_photo(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene('ブルーアワーの写真',
            w.cmd.change_camera("tatsu"),
            w.cmd.change_stage("CrossRoad"),
            w.cmd.change_time("earlymorning"),
            "交差点：ブルーアワーの空と町並みを写真に。彼女に気づく",
            w.plot_note("$tatsuは明け方の新聞配達を終えて、交差点に差し掛かる",
                "そこで空が紺色になり、街が青く染め上げられる様を目にした",
                "ブルーアワーだ"),
            w.plot_note("$tatsuは一眼レフを構えてシャッターをゆっくり切る",
                "その視線の先に、同じようにカメラを構える女性を見つけた"),
            w.plot_note("あと五分だけ",
                "そう思っているうちに魔法の時間は消えてしまう",
                "彼女の姿も消えてしまった"),
            )


def looping(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("繰り返すブルーアワー",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("何日経っても三月十三日から動かず、$tatsuは同じ日を繰り返していた"),
            w.plot_note("いつも配達を終えて、毎朝ブルーアワーに遭遇し、ブルーアワーの君と内心で呼ぶことにした彼女を見る"),
            )


def changing_her(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("変化していく彼女",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("ただ数日して、彼女が徐々に変化していくのに気づいた",
                "最初は髪型が違うな、程度だったが、徐々に季節外れの服装をするようになり、",
                "それに伴って自分の周囲の季節もズレ始めた"),
            )


def sliding_season(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("ズレゆく季節",
            w.cmd.change_stage("CrossRoad"),
            )


def cannot_talk(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("話せない彼女",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("$tatsuはある日、彼女と話してみようと決断する",
                "いざ話しかけてみると彼女は喜んだような表情になるが、口がぱくぱくするばかりで何も聞こえなかった"),
            w.plot_note("話せないのだと分かり、それでも何とか彼女が伝えたいことを読み取ろうとメモを渡してみたりするが、",
                "どうもうまくいかない"),
            )


def strange_man(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("奇妙な男",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("ある日、彼女を監視している別の男の存在に気づいた"),
            w.plot_note("彼女と口論している男を見て、$tatsuは助けようとした",
                "だがブルーアワーが終わると同時に二人の姿は目の前から消えてしまう"),
            )


def strange_awake(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("奇妙な目覚め",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("その日を境に、更に$tatsuの世界はゆがみ始める"),
            w.plot_note("目覚めると朝ではなく新聞配達の途中で、空はまだその時間帯ではないのにブルーアワーに染まっている"),
            )


def closing_world(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("閉鎖世界",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("しかし交差点に彼女の姿はなく、ただあの男がずっと立って睨みつけている"),
            w.plot_note("$tatsuは男に彼女をどうしたのか訊いたが、男は「もう彼女には近づくな」と言った"),
            w.plot_note("$tatsuは男を通報しようとしたが、電話が繋がらない"),
            w.plot_note("新聞販売店に戻ろうとするが、交差点を抜けられない"),
            w.plot_note("男の仕業だと思ったが、男は「これが本来の姿だ」と言う"),
            )


def truth(w: World):
    ta, akane = w.get("tatsu"), w.get("akane")
    return w.scene("真実",
            w.cmd.change_stage("CrossRoad"),
            w.plot_note("それを思い出した瞬間に、世界があの日に戻る"),
            w.plot_note("自転車に乗りながらガラケーを手に、ショートメールでどうやって思いを伝えるか悩んでいた"),
            "SMSの文字数、料金はそれぞれの携帯会社、またその機種や契約種により変わる。最小は５０文字でよかある制限は７０文字だったが、2019年にドコモなどでは６７０文字まで拡張されたりした",
            w.plot_note("そこに狭い路地の交差点に猛スピードで飛び出してくるバン"),
            w.plot_note("そこで$tatsuの人生は終わった",
                "けれど彼の意識だけは卒業式までに$akaneに告白をするという思いだけをこの世界にとどまらせた"),
            w.plot_note("$akaneが「ブルーアワーにだけは本当に魔法が使えるような気がする」と言ったことを思い出す"),
            w.plot_note("気づくとブルーアワーの世界に、$tatsuと$akaneの二人だけがいた"),
            w.plot_note("ブルーアワーが終わるまでの僅かな間だけ、男の力をつかって特別に言葉のやり取りができるようにしたと言われる"),
            w.plot_note("スマートフォンと携帯電話で、メッセージのやりとりをする。短いメッセージ"),
            w.plot_note("$akaneはその日に自分が「あと五分早く返事をしていたら死なないで済んだかも知れない」という思いを抱えて生きていた"),
            w.plot_note("$tatsuは成長し、今は子どもまでいる$akaneに対して、ずっと憧れだったことを伝える"),
            w.plot_note("$akaneは自分が「あと五分早く電話していたら死なずに済んだ」と言うが、",
                "卒業前に告白する予定でスマートフォンにメモをしていて、交通事故に遭ったことを伝える"),
            w.plot_note("$akaneは消えゆく$tatsuに抱きしめられながら「あと五分だけブルーアワーが続けばいいのに」と思った"),
            "ブルーアワーの意味合いをもっと際立たせるように",
            "写真モチーフをもっと使う",
            )
