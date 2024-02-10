import praw
import pandas as pd


reddit=praw.Reddit(
    client_id="2T00FLDD971SKRCRdnf69A",
    client_secret="qzhyq_GmuMvFarrIkHNyFEScXxSFAw",
    user_agent="brAIn by u/hamsatwin",)




keywords=['depressed','sad','hate myself','life sucks','depression','kill myself']

subreddit=reddit.subreddit('all')
posts=subreddit.search(keywords,limit=100)
titles=[]
texts=[]
for keyword in keywords:
    posts=reddit.search(query=keyword,limit=100)
    for post in posts:
        titles.append(post.title)
        texts.append(post.selftext)


data_frame={'Title':titles,'Text':texts}
df=pd.DataFrame(data_frame)
print(df)
  


