import React from 'react';

const ChannelDetails = ({ channel }: { channel: any }) => {
  return (
    <div className="details-container">
      <h4>{channel.snippet.title}</h4>
      <p>{channel.snippet.description}</p>
      <p>{channel.statistics.subscriberCount} subscribers</p>
    </div>
  );
};

export default ChannelDetails;
