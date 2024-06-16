import axios from "axios";

const BASE_URL = 'http://192.168.1.41:8000/';

export const endpoints = {
    'categories': '/categories/',
    'courses': '/courses/',
    
}

export const authAPI = (token) => {
    return axios.create({
        baseURL: BASE_URL,
        timeout: 10000,
        headers: {

            'Authorization': `Bearer ${token}`
        }
    })
}

export default axios.create({
    baseURL: BASE_URL
});