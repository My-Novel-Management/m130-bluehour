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
            ta.come("#新聞配達から戻ってくる$S"),
            dad.be(),
            akane.be(),
            ta.do("坂道を下り、幾つか交差点を経由して大通りから一本脇道に入ると、日日新聞の看板が見えてくる",
                "$Sはブレーキの効きが最近甘くなってきている自転車を何とか店の前の駐輪スペースに滑り込むとスタンドを立ててその場に固定する",
                "既に販売店の名前入りの白いバンは戻ってきていて、中からは楽しげな店主とその娘さんの笑い声が響いていた"),
            dad.talk("それが泥棒の正体が自分ちの猫だったっていうんだから、幽霊幽霊騒いでたのも酷い近所迷惑だったって話さ……おう、おかえり"),
            ta.talk("あ、はい", "配達終わりました"),
            akane.talk("$tatsu君、おつかれさん"),
            ta.do("がらりと音をさせて引き戸を開けると$Sの目に真っ先に飛び込んできたのは長い黒髪を後ろで一つに縛った、大きな黒目が印象的な女性の笑顔だった",
                "軽妙な声の「おつかれさん」は彼の疲労感を一気に消し去ってくれる魔法だ",
                "$Sにとって$akaneはお世話になっている店の一人娘という以上に、",
                "自分のことを中学から知る近所のお姉さんのような大切な存在だった"),
            "$akaneの父親はここで初出だが、そこまで詳細に描かなくていい。ただ世話になっているなどの情報は追加",
            "$akaneについては詳細に描写しておく。交差点の女性と同一人物だと、あとで分かるように見た目は化粧っけがなく、髪は長いものを結んでいる",
            akane.talk("$tatsu君、今日、どうだった？", "写真、うまくいった？"),
            ta.talk("あ、ええ"),
            ta.do("途端に浮かび上がる苦笑に、$akaneは「またチャンスあるよ」と声を掛けてくれる"),
            ta.talk("でも卒業までに何とかブルーアワーのベストショットをプレゼントするって約束したのに、これじゃ"),
            akane.talk("その気持ちだけで嬉しいよ",
                "それにね、写真も大事だけど何より毎日新聞をきっちりお客様に配達してくれることにはお父さんだけじゃなく、",
                "$meも本当に感謝してるから",
                "みんなが$tatsu君くらいに真面目で熱心だったらって思うもの"),
            dad.talk("何言ってんだよ、$akane",
                "うちの配達員はみんな頑張ってるぞ",
                "人間にミスはつきもんだ",
                "そういうのをカバーするのが$meの仕事なんだからな"),
            akane.talk("分かってるわよ、父さん",
                "でもほんと、最初の一年くらいは誤配や不着があったけど、",
                "慣れてからは軒数が増えたり家が変わったり、地域変えがあったりしても、よく対応してくれたもの",
                "卒業してもずっといてくれたらって今でも思うし"),
            ta.do("卒業、という言葉が$Sの心に小さな影を落とした",
                "事務所の壁に掛かるカレンダーには三月十四日にしっかりと赤丸がされ、$tatsu君卒業と$akaneのやや丸い字で書き込みがされている"),
            ta.talk("まだ、明日の朝がありますから", "明日こそ絶対に一番のブルーアワーを撮ってみせます"),
            akane.talk("ありがとう",
                "でもどんな写真になったとしても、それが$meにとっては一番だから",
                "それだけは覚えておいてね"),
            ta.do("彼女の笑顔に曖昧に頷きを返しつつその視線を新聞の天気予報欄に移すと、明日の予報は雨だった"),
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
            ta.do("販売店に戻ってきて事務室に掛かっていたカレンダーを見ると、同じように三月十四日の卒業式に赤丸が付いたままで、",
                "まだ$Sは卒業式を終えていないようだった"),
            dad.talk("おう、どうした？", "ぼーっと新聞見て",
                "何か面白い記事でもあんのか？"),
            ta.talk("あ、いえ"),
            ta.do("首からタオルを下げた店長は新聞の日付を睨みつけていた$Sを見て小首を捻る"),
            akane.talk("もう父さんたら、$tatsu君も卒業式を控えてナーバスになってるのよ",
                "それよりどうだった？", "うまく撮れた？"),
            ta.think("それは昨日と同じ質問だった",
                "$akaneの服装も全く同じで、どういう訳か同じ一日をまた繰り返しているようだ"),
            ta.talk("なんか、うまく撮れなくて",
                "ちょっとカメラの調子が悪いみたいで"),
            akane.talk("え？　そうなの？",
                "まあ$meのお古だから、それこそ三年前の機種だものね",
                "卒業祝いにプレゼントしてあげたいところだけど"),
            ta.do("彼女の目は店長へと向かったが渋い表情をされてしまう"),
            ta.talk("大学生になったらそれこそもっと稼いで自分で一番いいの、買いますよ"),
            akane.talk("ごめんね",
                "うちも最近部数が減ってきてて色々大変みたいで"),
            dad.talk("おい$akane",
                "そんなのは昨日今日の話じゃないだろ",
                "$meだって色々考えて$yoshiのところに声掛けたりしてるんだ",
                "お前だって大学出てから社会勉強してくるっつったのに、三ヶ月で家に戻ってきて、今何してる？",
                "花嫁修業か？"),
            akane.talk("その前に恋人がいません",
                "それに事務のおばさま方にいじめられたって言ったらすぐ帰ってこいってアパート解約したのはそっちでしょ？"),
            ta.do("また始まった、と$Sは苦笑で事務室を出る"),
            ta.do("この店には$S以外にも多くのアルバイトや契約社員が勤めている",
                "それぞれ地域や時間帯も異なるので顔を合わせるのは決まった人ばかりなのだが、",
                "どういう訳か昨日から一人として見かけない",
                "既に店のバイクや原付きは返却済みで、配達用の新聞の束もほぼ無くなっている",
                "外に出れば朝の空気が路地に溢れ、",
                "周辺の家々から朝食の味噌汁や焼き魚の香りが漂ってくる"),
            ta.think("いつもの朝だ"),
            ta.think("そうとしか感じられないのにどこかがおかしい"),
            akane.talk("$tatsu君？"),
            ta.do("振り返ると$akaneがいた",
                "彼女はその結んだ長い髪の先を揺らして$Sの顔を覗き込むようにすると、いつも向けてくれる穏やかな朝日のような笑顔へと変わる",
                "それは直接見ると眩しすぎて、だからいつも$Sは俯くようにして視線を逸らすと面と向かわないように「何ですか」と返すのだ"),
            akane.talk("今日のブルーアワーは残念だったね",
                "でも、また明日があるし、もっと言えば毎日チャンスは巡ってくるから",
                "だから、期待はほどほどにして待ってるよ"),
            ta.do("そうですね、とぼそぼそ答えて、$Sは自分の自転車に跨がり、地面を蹴った"),
            )
