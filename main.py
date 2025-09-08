import sys, json
from src.appleMusic.api import AppleMusicAPI
from src.print import error
from src.parse import getTrackIdFromUrl
import src.formatter

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		error('有効なトラックURLを渡してください')
	API = AppleMusicAPI()
	try:
		trackId = getTrackIdFromUrl(sys.argv[1])
		if trackId is None:
			error('有効なトラックURLを渡してください')
		rawLyrics = API.getSyllableLyricAsTTML(trackId)
		with open('./raw-lyric.xml', 'w', encoding='utf-8') as f:
			f.write(rawLyrics)
			f.close()
		with open('./lyrics.json', 'w', encoding='utf-8') as f:
			lyrics = src.formatter.parseSpotify(rawLyrics)
			json.dump({'lyric' : lyrics}, f, ensure_ascii=False, indent=4)
			f.close()
	except Exception as e:
		error(str(e))