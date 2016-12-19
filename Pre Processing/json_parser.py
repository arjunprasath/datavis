import json
import random
import pafy
import requests

views_arr = [643, 173, 185, 643, 1017, 280, 528, 1633, 2117, 2222, 1253, 614, 349, 410, 379, 554, 803, 2722, 960, 185, 173, 14422, 188, 382, 231, 192, 201, 385, 807, 581, 581, 807]
views_arr.sort();
json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'
with open('GAPVideoData.JSON') as json_data:

  decoded = json.load(json_data)
  mylists = decoded['mylists']
    # Access data

terms = ['IMMIGRANT', 'XENOPHOBIA','RACISM', 'PRISON' , 'POLICING','GENDER', 
'EDUCATION', 'HEALTH', 'HOUSING', 'LGBTQ', 'IMMIGRATION', 'JUSTICE', 'SUPAFRIENDS', 'STUDENTS']
words = []
for term in terms:
  word = {"term": term, "score": 0.5, "timestamps": [], "dates": [{}], "totalviews":0 }
  words.append(word)


subtalks = []
v= []
i = 0
frameno =0
for playlist in mylists:
    
  for item in playlist['items']:
    url = "https://www.youtube.com/watch?v="+item['snippet']['resourceId']['videoId']
    try:
      video = pafy.new(url)
      v.append(video.viewcount)
    except:
      print "some error with video"

    title = item['snippet']['title']
    pubdate = item['snippet']['publishedAt']
    desc = item['snippet']['description']
    for w in words:

      if w['term'].lower() in desc.lower():
        w['timestamps'].append(frameno)
        #w['totalviews'] = views_arr.index(video.viewcount)+1
        

        w['dates'].append({pubdate,frameno})
        
    frameno = frameno + 1
    subtalk = {"youtubeId" : item['snippet']['resourceId']['videoId'],
          "maxTime": 2402,
          "transcriptDelay": 0,
          "thumbnailRatio": 1.843
    }
    subtalks.append(subtalk)
    
    
    # frame_filename = 'frame'+str(frameno-1)+'.jpg'
    # with open(frame_filename, 'wb') as handle:
    #   response = requests.get(item['snippet']['thumbnails']['high']['url'], stream=True)
    #   if not response.ok:
    #     print response
    #   for block in response.iter_content(1024):
    #     if not block:
    #       break
    #     handle.write(block)
            
print len(subtalks)
print words
print v
#with open('GAP.json', 'w') as writedata:
# json.dump(subtalks,writedata)

 


