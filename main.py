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
		with open('./lyrics.json', 'w', encoding='utf-8') as f:
			lyrics = API.getSyllableLyricAsDictXml(trackId)
			lyrics = src.formatter.toSpotifyJson(lyrics)
			json.dump(lyrics, f, ensure_ascii=False, indent=4)
	except Exception as e:
		error(str(e))