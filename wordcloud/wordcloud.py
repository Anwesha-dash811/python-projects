#pip install wordcloud
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


frnd_df = pd.read_csv('friends.csv')
frnd_df #to display the dataset
from wordcloud import WordCloud , ImageColorGenerator


comment_words = '' 
  
# iterate through the csv file 
for val in frnd_df.NAME: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
      
    comment_words += " ".join(tokens)+" "
wordcloud = WordCloud(width = 400, height = 400, background_color ='white', 
                min_font_size = 10).generate(comment_words)                  
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()






