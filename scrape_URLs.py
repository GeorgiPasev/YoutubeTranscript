import yt_dlp

def get_youtube_video_urls(channel_videos_url):
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_videos_url, download=False)
        video_urls = []
        for entry in info.get('entries', []):
            if (entry.get('ie_key') == 'Youtube' and           # Only normal videos
                'shorts/' not in entry.get('url', '') and
                entry.get('duration', 61) >= 60):              # Filter out shorts by duration
                video_urls.append(f"https://www.youtube.com/watch?v={entry['id']}")
        return video_urls

channel_url = "" # https://www.youtube.com/@.../videos
all_videos = get_youtube_video_urls(channel_url)
print('"' + '",\n"'.join(all_videos) + '"')