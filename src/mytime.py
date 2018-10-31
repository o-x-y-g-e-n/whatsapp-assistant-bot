from datetime import datetime

def time_generator():
	str = datetime.now().strftime('%Y-%m-%d %A')
	return str

