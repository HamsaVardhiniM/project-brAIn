import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="********",
    client_secret="************",
    user_agent="***********",
)

keywords = ['depressed', 'sad', 'hate myself', 'life sucks', 'depression', 'kill myself']

titles = []
texts = []
for keyword in keywords:
    posts = reddit.subreddit('all').search(query=keyword, limit=100)
    for post in posts:
        titles.append(post.title)
        texts.append(post.selftext)

data_frame = {'Title': titles, 'Text': texts}
df = pd.DataFrame(data_frame)
df.to_csv('reddit_posts.csv', index=False)
print(df)


