from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.hostname in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
        return parse_qs(parsed.query).get('v', [None])[0]
    if parsed.hostname == 'youtu.be':
        return parsed.path.lstrip('/')
    return None

def fetch_and_save_transcripts(urls, output_file='transcripts.txt'):
    api = YouTubeTranscriptApi()
    with open(output_file, 'w', encoding='utf-8') as f:
        for url in urls:
            video_id = extract_video_id(url)
            if not video_id:
                f.write(f"Invalid URL: {url}\n\n")
                continue
            try:
                transcript = api.fetch(video_id)
                f.write(f"Transcript for {url}:\n")
                for entry in transcript:
                    f.write(entry.text + '\n')
                f.write('\n')
            except Exception as e:
                f.write(f"Failed to fetch transcript for {url}: {e}\n\n")

urls = [] # paste YouTube URLs here
fetch_and_save_transcripts(urls)