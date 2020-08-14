import React, { ChangeEvent, useState } from 'react';
import { TextField, Button, CircularProgress } from '@material-ui/core';

import './Landing.css';
import Api from '../../api/api';
import { useHistory } from 'react-router-dom';

const Landing = () => {
  const history = useHistory();
  const [channelName, setChannelName] = useState('');
  const [loading, setLoading] = useState(false);

  const search = () => {
    setLoading(true);

    Api.getChannelId(channelName)
      .then((res) => {
        if (!res.channelId) {
          console.error('Something went wrong');
          return;
        }

        setLoading(false);
        history.push(`/channel/${res.channelId}`);
      })
      .catch((err: any) => {
        console.error(err);
        setLoading(false);
      });
  };

  return (
    <div className="landing-container">
      <TextField
        label="Channel name"
        variant="outlined"
        value={channelName}
        onChange={(e: ChangeEvent<HTMLInputElement>) =>
          setChannelName(e.target.value)
        }
      />
      <Button variant="outlined" color="primary" onClick={() => search()}>
        Search
      </Button>

      {loading && <CircularProgress />}
    </div>
  );
};

export default Landing;
