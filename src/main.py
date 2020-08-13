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
MAJOR, MINOR, MICRO = 0, 4, 0
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
def ep_strange_lady(w: World):
    return w.episode("奇妙な女性",
            w.plot_setup("$tatsuは学校に行きながら新聞配達をしている学生だった"),
            w.plot_setup("毎月十三日のブルーアワーの時、新聞配達を終えて帰る交差点に現れる謎の女性がいることに気づく"),
            w.plot_setup("彼女はスマートフォンでこっそり$tatsuの姿を撮影していた"),
            w.plot_setup("$tatsuは新聞屋の娘に恋心を抱いていて、卒業して大学に行く前に告白しようと考えていた"),
            w.plot_note("新聞屋に戻ってその女性のことを話すと最近はストーカーや変質者が多いという話になる"),
            w.plot_note("$akaneも最近妙な男性のアプローチに困っていると話していた"),
            "新聞販売店と交差点、自室以外は出さない。地縛霊であることを徐々に感じさせるためにどこかに違和感を置いておく",
            "$tatsuの知る新聞屋の彼女とは年齢が異なっている。それは死後十五年経ってしまっているから",
            w.plot_turnpoint("$tatsuは日付が卒業式前で止まったままだと気づく"),
            "スマートフォンの日付が三月十三日から動かない",
            "卒業式は三月十四日",
            "地縛霊の世界では、その一時空だけが現実世界と繋がっている",
            outline="毎月十三日だけその交差点に現れる謎の女性がいた")


def ep_stopping_time(w: World):
    return w.episode("静止した時間の中で",
            w.plot_develop("彼女に会ってからずっと時間が進まずに、$tatsuは卒業前の時空に閉じ込められてしまう"),
            w.plot_develop("彼女は言葉が話せず、何を伝えたがっているのか理解できない"),
            w.plot_develop("彼女と意思疎通をしようと色々と工夫するが、彼女の返信はいつもブルーアワーで消えてしまう"),
            w.plot_note("その彼女を監視している別の男の存在に気づく"),
            w.plot_note("彼女と口論している男を見て、$tatsuは助けようとした",
                "だがブルーアワーが終わると同時に二人の姿は目の前から消えてしまう"),
            w.plot_note("次の十三日、$tatsuは男をその交差点で待ち伏せしていた"),
            w.plot_turnpoint("彼女をつけていた知らない男はもう彼女に近づくなと言ってきた"),
            "彼女の父親はずっと引きずっているのを心配して、霊媒師を呼んだ",
            outline="彼女の存在に気づいてから、時間がゆがみ始めた")


def ep_ghost_talk(w: World):
    return w.episode("幽霊の君と",
            w.plot_resolve("自分が幽霊だったと知り、交通事故に遭った日のことを全て思い出す"),
            w.plot_note("男は彼女と$tatsuは住む世界が違うと説明する"),
            w.plot_note("男は霊媒探偵と名乗り、調査手帳に挟んだ新聞の切り抜き記事を見せて$tatsuに説明する"),
            w.plot_note("$tatsuは十年前に交通事故で亡くなっていた"),
            w.plot_note("$akaneはその日に自分が「あと五分早く返事をしていたら死なないで済んだかも知れない」という思いを抱えて生きていた"),
            w.plot_note("男の力でスマートフォンを通じて、現実世界の$akaneと通話できるようにしてもらう"),
            w.plot_note("$tatsuは成長し、今は子どもまでいる$akaneに対して、ずっと憧れだったことを伝える"),
            w.plot_note("$akaneは自分が「あと五分早く電話していたら死なずに済んだ」と言うが、",
                "卒業前に告白する予定でスマートフォンにメモをしていて、交通事故に遭ったことを伝える"),
            w.plot_note("$akaneは消えゆく$tatsuに抱きしめられながら「あと五分だけブルーアワーが続けばいいのに」と思った"),
            "ブルーアワーの意味合いをもっと際立たせるように",
            "写真モチーフをもっと使う",
            outline="ブルーアワーの君の真実が明らかになり、幽霊だと知った$tatsuは彼女の思いを昇華させ、成仏していった")


def ch_main(w: World):
    return w.chapter('main',
            ep_strange_lady(w),
            ep_stopping_time(w),
            ep_ghost_talk(w),
            w.symbol("（了）"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "人生とは勘違いと後悔の連続である",
            "「あと五分」という言葉には「あと五分あれば何とかなったのに」というような人間の基本的な願望を見ることができる",
            "現実はどれほど時間があろうとできなかったことはできないし、足りないものは足りないままで、",
            "〜しなければという後悔は、多くの人が経験し、人生のどこかにシミを作っている",
            "本作はその「五分」という時間の失敗をずっと引きずっている女性と、",
            "いつも「あと五分早く起きられない」という日常を持っていた男性とが、",
            "ブルーアワーのみに起こる不思議な現象によって互いの心の楔を取り去っていくという、",
            "人生の希望譚である",
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

# characters
def chara_note(w: World):
    return w.writer_note("人物メモ",
            "主人公：新聞配達員。実は幽霊。事故死した。毎月十三日だけ出現する",
            "女性：彼といい感じだった女性。恋人未満。あと五分早く電話していればと後悔し続けている",
            "謎の男性：霊媒師。幽霊となった主人公と会話できないので、彼女が探して連れてきた。だが男の方が勘違いし、ややこしいことになる",
            )


def chara_tatsu(w: World):
    return w.chara_note("$tatsuの履歴書",
            "真面目だがあまり儲かっていない自営業の家に生まれる",
            "小さい頃から家計を助けるためと牛乳配達や新聞配達をこなす",
            "高校は父親の知人の新聞販売店に住み込みで、定時制に通う",
            "そこの娘だった歳上の$akaneに恋心を抱いていた",
            "高校卒業の前日、酔っぱらいの帰宅途中の車に交差点でぶつけられて事故死する",
            "地縛霊となったことに気づかないまま、何度も最後の一年だけを繰り返している",
            )


def chara_akane(w: World):
    return w.chara_note("$akaneの履歴書",
            "祖父の代からの新聞販売店に生まれる",
            "一人娘としてあれこれと好きなものを買い与えられ、お姫様的に育てられる",
            "気立てがよく、新聞配達の若い子たちともバーベキューをしたりして楽しんでいた",
            "$tatsuとは歳が近かったこともあり、また彼の勤勉な態度に感化され、密かに憧れを抱いたりする対象だった",
            )


def chara_gado(w: World):
    return w.chara_note("$gadoの履歴書",
            "神社の神主の子として生まれる",
            "三人兄弟の次男で、長男が神主を次ぐことが決まっていたが、無理やり親により神道系大学に行かされる",
            "それとは別に幼い頃からミステリ系の小説を読み、謎解きに興味を持つようになる",
            "学生時代は他人の揉め事を解決する星のめぐり合わせがあり、何度か霊的な事件の解決にかかわった",
            "長男が不慮の事故で亡くなったが、$gado本人が後継者とはならず、弟が神社を継ぐ",
            "$gadoは学生時代からの貯金と、投資で当てた資金を元手として事務所を立ち上げ、そこで色々な霊的問題を引き受けることにした",
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
            chara_tatsu(w),
            chara_akane(w),
            chara_gado(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

