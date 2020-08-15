import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;
// const REQUEST_CONFIG = {
//   'Content-Type': 'application/json',
// } as AxiosRequestConfig;

const Api = {
  getChannelId: (name: string): Promise<any> => {
    return axios
      .get(`${API_URL}/channel`, { params: { name } })
      .then((res: any) => res.data);
  },

  getSentiment: (channelId: string): Promise<any> => {
    return axios
      .get(`${API_URL}/sentiment`, { params: { channel: channelId } })
      .then((res: any) => res.data);
  },
};

export default Api;
