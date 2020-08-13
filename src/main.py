#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "ブルーアワーの君"
MAJOR, MINOR, MICRO = 0, 2, 0
COPY = "その瞬間だけ、君に会える"
ONELINE = "ブルーアワー（日の出前日の入り後の空が濃紺に染まる時間帯）にだけ会える彼女がいた"
OUTLINE = "約8000字の幻想短編。明け方のブルーアワーにだけ出会うことのできる不思議な女性に恋をした新聞配達員の男性は、彼女と何とか交流しようとするが"
THEME = "思いのすれ違い"
GENRE = "ファンタジー／恋愛／ミステリ"
TARGET = "20-40years"
SIZE = "8K"
CONTEST_INFO = "妄想コンテスト「あと５分」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ヒューマンドラマ", "男主人公", "幻想"]
RELEASED = (1, 1, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            w.plot_note("毎月十三日にだけ、新聞配達を終えてその交差点を通り掛かる$tatsuの姿をこっそり撮影していく謎の女性がいた"),
            "$tatsuの知る新聞屋の彼女とは年齢が異なっている。それは死後十五年経ってしまっているから",
            "彼女の父親はずっと引きずっているのを心配して、霊媒師を呼んだ",
            "地縛霊の世界では、その一時空だけが現実世界と繋がっている",
            w.plot_note("彼女は毎月十三日のブルーアワーの時だけ、その交差点に現れる"),
            w.plot_note("彼女はいつもこっそり$tatsuを撮影していた"),
            w.plot_note("$tatsuは彼女のことが気になっていた"),
            w.plot_note("新聞屋に戻ってそのことを話すと最近はストーカーや変質者が多いという話になる"),
            w.plot_note("その彼女をつけている男に気づいた"),
            w.plot_note("男は彼女のいる時にしか現れない"),
            w.plot_note("$tatsuは男に対して何か言ってやろうと待ち伏せした"),
            w.plot_note("しかし男は$tatsuに彼女の前から消えてくれと言う"),
            w.plot_note("男は彼女と$tatsuは住む世界が違うと説明する"),
            w.plot_note("彼女は言葉が話せない"),
            w.plot_note("$tatsuは警察に電話しようとするが繋がらない"),
            w.plot_note("男も彼女もブルーアワーの消滅と目の前から共に消えてしまった"),
            w.plot_note("男の手から落ちた手帳を見ると、そこにはある男性の死亡事故のことから彼女の素性まで、もろもろが記載されていた"),
            w.plot_note("それを読み、$tatsuは自分が幽霊だと気づく"),
            w.plot_note("翌月の十三日、$tatsuは男に頼んで彼女と話させて欲しいと言う"),
            w.plot_note("$tatsuは成長し、今は子どもまでいる$akaneに対して、ずっと憧れだったことを伝える"),
            w.plot_note("$akaneは自分が「あと五分早く電話していたら死なずに済んだ」と言うが、",
                "卒業前に告白する予定でスマートフォンにメモをしていて、交通事故に遭ったことを伝える"),
            w.plot_note("$akaneは消えゆく$tatsuに抱きしめられながら「あと五分だけブルーアワーが続けばいいのに」と思った"),
            w.plot_note("$akaneが撮影したブルーアワーの写真には、不思議な人形の光が映り込んでいた"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )


def plot_note(w: World):
    return w.writer_note("作品メモ",
            "ブルーアワーとは、日の出前と日の入り後に発生する空が濃い青色に染まる時間帯のことである。元々はフランス語のl'heure bleueに由来する。",
            "明け方のブルーアワーの時間にだけ現れる彼女がいた",
            "新聞配達員の男性は、その彼女に恋をしている",
            "彼女は毎月十三日にしか現れない",
            "彼女は徐々に成長していく",
            "彼女とは言葉を交わせないが、何か言おうとしているのは理解できる",
            "ある日、知らない女性を連れて彼女が現れた",
            "その女性は男を幽霊だと非難する",
            "実は男の方が幽霊だった",
            "男は交通事故死して地縛霊になっていた",
            "彼女は「あと五分電話するのが早ければ助かっていた」と後悔していた",
            "それを知り、その日は携帯電話を忘れて出かけていたからどちらにしても事故は防げなかったと告白する",
            "彼女の思いを知り、男は成仏した",
            "CQ：男は彼女の伝えたいことを理解できるか",
            "最終的に彼女の思いも主人公の思いも浄化して、死んだことは悲しいけれども、それだけじゃないさわやかなラストになるようにする",
            "最後には明るい話にしたい。読後感が良いものを目指す",
            )


def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "あと五分、というお題",
            "あと五分は「残り五分」という意味合いが強いが、他にも「もう五分」とか「その後で五分」とか、とらえようはある",
            "五分という文字はどこかに出す必要があるだろう",
            "メインテーマは「勘違い」",
            "勘違いによって人生は大きく変化する",
            "それが良い方向に転ぶこともあれば、悪い方向に転ぶことも",
            "勘違いというのは思い込みや早とちり",
            "あと五分だけ考える、みたいな猶予があればひょっとすれば勘違いしなくて済んだかも知れない",
            "勘違いは後悔につながる",
            "人生はいつも後悔に満ちている",
            "後悔しないと言う人だって何かしら引きずっているし、どこかで誰かに悪いことをしてしまったという罪悪感を抱えて生きている",
            "思いに囚われて、成長できない人々",
            "それは幽霊に憑かれたようなもので、彼女はずっと後悔に囚われてそこから動けなくなってしまっている",
            "この物語は彼女の解放が目的である",
            "彼女の精神の解放をする為にどうすればいいのか、を考える",
            "現代的モチーフを何か",
            "ストーカーとか、写真に映り込む個人情報とか",
            "位置情報もスマホから分かるし",
            "情報こそが正しいと思い込み、それによって間違いを犯してしまう",
            )


def chara_note(w: World):
    return w.writer_note("人物メモ",
            "主人公：新聞配達員。実は幽霊。事故死した。毎月十三日だけ出現する",
            "女性：彼といい感じだった女性。恋人未満。あと五分早く電話していればと後悔し続けている",
            "謎の男性：霊媒師。幽霊となった主人公と会話できないので、彼女が探して連れてきた。だが男の方が勘違いし、ややこしいことになる",
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            theme_note(w),
            chara_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

