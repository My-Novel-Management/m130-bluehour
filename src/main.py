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
MAJOR, MINOR, MICRO = 0, 1, 0
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
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
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
            chara_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

