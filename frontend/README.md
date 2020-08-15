Frontend for the youtube-sentiment-analysis project, built using React, Typescript, and ReCharts.

![Netlify Status](https://api.netlify.com/api/v1/badges/2277635f-9f54-4614-a87b-2b28a0627106/deploy-status)

## Building and Running
To build and run the frontend, first clone the repo and change into the frontend folder
```bash
git clone git@github.com:raduschirliu/youtube-sentiment-analysis.git
cd youtube-sentiment-analysis/frontend
```

set the neccesary environment variables (either globally or in a `.env` file in the `frontend/` folder)
```bash
REACT_APP_API_URL=https://url-to-backend.com
```

and install all dependencies through NPM
```bash
npm i
```

Then, it can be ran in development mode with
```bash
npm start
```

or, alternatively, it can be built for production with
```bash
npm run build
```