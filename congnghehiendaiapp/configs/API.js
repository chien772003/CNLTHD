import axios from "axios";

const BASE_URL = 'http://10.17.20.6:8000//';

export const endpoints = {
    'categories': '/categories/',
    'courses': '/courses/',
    'login': '/o/token/',
    // 'registerGV':
};

export const authAPI = (accessToken ) => axios.create({
    baseURL: BASE_URL,
    headers: {
        'Authorization': `Bearer ${token}`
    }
})

export default axios.create({
    baseURL: BASE_URL
});
