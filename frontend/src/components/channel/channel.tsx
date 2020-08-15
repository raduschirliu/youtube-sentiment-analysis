import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Api from '../../api/api';
import { CircularProgress } from '@material-ui/core';
import ChannelDetails from '../channel-details/ChannelDetails';
import SentimentDetails from '../sentiment-details/SentimentDetails';

const Channel = () => {
  const { channelId } = useParams();
  const [loading, setLoading] = useState(false);
  const [sentimentData, setSentimentData] = useState<any>(null);
  console.log(sentimentData);

  useEffect(() => {
    setLoading(true);

    Api.getSentiment(channelId)
      .then((res: any) => {
        setSentimentData(res);
        console.log(res);
      })
      .catch((err: any) => {
        setSentimentData(null);
        console.error(err);
      })
      .finally(() => setLoading(false));
  }, [channelId]);

  return loading || !sentimentData ? (
    <CircularProgress />
  ) : (
    <div className="channel-container">
      <ChannelDetails channel={sentimentData.channel} />
      <SentimentDetails videos={sentimentData.videos} />
    </div>
  );
};

export default Channel;
