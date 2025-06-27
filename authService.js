// src/authService.js
import API from './api';

export const registerUser = async (userData) => {
  try {
    const response = await API.post('/register', userData);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Registration failed' };
  }
};

export const loginUser = async (userData) => {
  try {
    const response = await API.post('/login', userData);
    const { access_token } = response.data;
    localStorage.setItem('token', access_token);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Login failed' };
  }
};
