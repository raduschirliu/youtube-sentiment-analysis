import React from 'react';
import {
  LineChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  Line,
} from 'recharts';

const SentimentDetails = ({ videos }: { videos: any[] }) => {
  return (
    <div className="sentiment-container">
      <h4>
        Sentiment data from the last {videos.length} videos, based on the top{' '}
        {videos[0].comments.length} comments
      </h4>
      <LineChart width={800} height={600} data={videos}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis label="Video" />
        <YAxis label="Polarity" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="average_polarity" stroke="#8884d8" />
        <Line type="monotone" dataKey="median_polarity" stroke="#82ca9d" />
      </LineChart>

      <LineChart width={800} height={600} data={videos}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis label="Video" />
        <YAxis label="Subjectivity" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="average_subjectivity" stroke="#8884d8" />
        <Line type="monotone" dataKey="median_subjectivity" stroke="#82ca9d" />
      </LineChart>
    </div>
  );
};

export default SentimentDetails;
