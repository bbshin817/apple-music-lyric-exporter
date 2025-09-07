import sys
from src.print import error

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		error('有効なトラックURLを渡してください')