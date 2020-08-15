# youtube-sentiment-analysis

![Heroku Status](https://heroku-badge.herokuapp.com/?app=youtube-sentiment-analysis)
![Netlify Status](https://api.netlify.com/api/v1/badges/2277635f-9f54-4614-a87b-2b28a0627106/deploy-status)


A web app which looks at the most popular comments from a YouTube channel's most recent videos,
and displays visualizations of the sentiment changes.  
Demo availible [here](https://rs-youtube-sentiment-analysis.netlify.app/).

### Frontend
The frontend is built using React, TypeScript, and MaterialUI. More information about building
and deploying can be found in the [frontend](https://github.com/raduschirliu/youtube-sentiment-analysis/tree/master/frontend) folder.

### Backend
The backend is a REST API built using Python, Flask, and TextBlob/NLTK for the sentiment analysis. More information
about building and deploying can be found in the [backend](https://github.com/raduschirliu/youtube-sentiment-analysis/tree/master/backend) folder.