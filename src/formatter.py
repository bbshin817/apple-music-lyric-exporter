# from decimal import Decimal

def parseDuration(duration: str) -> int:
    parts = duration.split(":")
    if len(parts) == 2:
        minutes = int(parts[0])
        seconds = float(parts[1])
    else:
        minutes = 0
        seconds = float(parts[0])

    total_ms = int((minutes * 60 + seconds) * 1000)
    return total_ms

def toSpotifyJson(dict):
	divs = dict['tt']['body']['div']
	lyrics = []
	divIndex = 0
	for div in divs:
		if isinstance(div['p'], list):
			for p in div['p']:
				words = ''
				syllables = []
				for span in p['span']:
					words += span['#text']
					syllables.append({
						'startTimeMs' : parseDuration(span['@begin']),
						'numChars' : len(span['#text']),
						'endTimeMs' : parseDuration(span['@end'])
					})
				lyrics.append({
					'startTimeMs' : parseDuration(p['span'][0]['@begin']),
					'words' : words,
					'syllables' : syllables,
					'endTimeMs' : parseDuration(p['span'][len(p['span']) - 1]['@end'])
				})
		else:
			words = ''
			syllables = []
			for span in div['p']['span']:
				words += span['#text']
				syllables.append({
					'startTimeMs' : parseDuration(span['@begin']),
					'numChars' : len(span['#text']),
					'endTimeMs' : parseDuration(span['@end'])
				})
			lyrics.append({
				'startTimeMs' : parseDuration(div['p']['span'][0]['@begin']),
				'words' : words,
				'syllables' : syllables,
				'endTimeMs' : parseDuration(div['p']['span'][len(div['p']['span']) - 1]['@end'])
			})
		if (divIndex < len(divs) - 1):
			lyrics.append({
				'startTimeMs' : parseDuration(div['@end']),
				'words' : '',
				'syllables' : [],
				'endTimeMs' : parseDuration(divs[divIndex + 1]['@begin'])
			})
		else:
			lyrics.append({
				'startTimeMs' : parseDuration(div['@end']),
				'words' : '',
				'syllables' : [],
				'endTimeMs' : parseDuration(dict['tt']['body']['@dur'])
			})
		divIndex += 1
	return {
		'lyric' : lyrics
	}