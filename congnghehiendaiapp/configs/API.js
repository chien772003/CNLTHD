import axios from "axios";

const BASE_URL = 'http://192.168.1.8:8000/';

export const endpoints = {
    'categories': '/categories/',
    'courses': '/courses/',
    'login': '/o/token/',
    'registerGV':'/users/register-teacher/'
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
