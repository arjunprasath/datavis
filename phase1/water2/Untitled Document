import gdata.youtube.service

service = gdata.youtube.service.YouTubeService()
feed_url = 'http://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?v=2'
feed = service.GetYouTubeVideoFeed(feed_url)
entry = feed.entry[0] # pick most viewed video as sample entry

thumbnail = entry.media.thumbnail[0].url
    # will be an URL like: 'http://i.ytimg.com/vi/%(video_id)s/default.jpg'
    # when querying YouTube API version 2 ('?v=2' at the end of feed URL)
