# Apple Music Lyrics Exporter

本ツールを使用すると、Apple Music から曲の歌詞を取得することができます。1曲ごとの抽出に対応しており、アルバム単位での一括抽出には対応していません

## 免責事項

**※歌詞の取得には、有効なApple Music サブスクリプションが必要です**

**※本ツールは、有効なサブスクリプションを契約している実行者が、自身の家庭内でのみ歌詞情報を利用することを想定しており、実行に際するいかなる責任も、bbshin817は負わないものとします。**

## 実行
1.	Chromeの開発者ツール等を使用して、[.music.apple.com](https://music.apple.com/) ドメインのCookieに保存されている media-user-token を、main.pyと同じディレクトリに`media-user-token`として保存してください。

	```
	.
	├── src/
	│   ├── appleMusic/
	│   └── ...
	├── main.py
	└── media-user-token
	```

2.	コンソールで次のように実行すると、歌詞が.json形式で./outputsへ保存されます

	```
	$ python main.py "https://music.apple.com/jp/song/..."
	```

## 出力される歌詞の内容と形式
**Spotify JSON Lyrics (非公式名称)** として出力され、次の内容を含みます。

- 歌詞の全文と、タイミングミリ秒
- 音節単位の分割情報と、タイミングミリ秒

	```jsonc
	/* 例: 夏の影 / Mrs. GREEN APPLE */
	"lyric": [
        {
            "startTimeMs": 1201,
            "words": "吹いた",
            "syllables": [
                {
                    "startTimeMs": 1201,
                    "numChars": 2,
                    "endTimeMs": 1764
                },
                {
                    "startTimeMs": 1764,
                    "numChars": 1,
                    "endTimeMs": 2505
                }
            ],
            "endTimeMs": 2505
        },
		{
            "startTimeMs": 2537,
            "words": "そよ風が",
            "syllables": [
                {
                    "startTimeMs": 2537,
                    "numChars": 2,
                    "endTimeMs": 3093
                },
                {
                    "startTimeMs": 3093,
                    "numChars": 1,
                    "endTimeMs": 3574
                },
                {
                    "startTimeMs": 3574,
                    "numChars": 1,
                    "endTimeMs": 4492
                }
            ],
            "endTimeMs": 4492
        }
	]
	```