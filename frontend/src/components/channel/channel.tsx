import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Api from '../../api/api';
import { CircularProgress } from '@material-ui/core';

const Channel = () => {
  const { channelId } = useParams();
  const [loading, setLoading] = useState(false);
  const [sentimentData, setSentimentData] = useState(null);
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

  return loading ? <CircularProgress /> : <p>Loaded</p>;
};

export default Channel;
