import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Api from '../../api/api';

const Channel = () => {
  const { channelId } = useParams();
  const [loading, setLoading] = useState(false);
  const [sentimentData, setSentimentData] = useState(null);

  loading;
  sentimentData;

  useEffect(() => {
    console.log('changed!', channelId);
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

  return <p>Test</p>;
};

export default Channel;
