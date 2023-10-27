<template>
    <div class="chat-container">
      <button @click="toggleChat" class="chat-button">
        {{ isChatOpen ? 'Close Chat' : 'Open Chat' }}
      </button>
      <div v-if="isChatOpen" class="chat-box">
        <div class="chat-window">
          <div v-for="(message, index) in store.messages" :key="index" :class="message.role">
            {{ message.content }}
          </div>
        </div>
        <div class="chat-input">
          <input v-model="inputMessage" @keyup.enter="sendMessage" />
          <button @click="sendMessage">Ask the Prophet</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { store } from '../stores/store.js';
  import axios from 'axios';
  
  const isChatOpen = ref(false);
  const inputMessage = ref('');
  
  const toggleChat = () => {
    isChatOpen.value = !isChatOpen.value;
  };
  
  const sendMessage = async () => {
    try {
      const response = await axios.post('http://localhost:8000/get_response', { message: inputMessage.value });
      console.log('Message sent:', response);
      store.messages.push({ role: 'user', content: inputMessage.value });
      store.messages.push({ role: 'assistant', content: response.data.message });
      inputMessage.value = '';
    } catch (error) {
      console.error('An error occurred while sending the message:', error);
    }
  };
  </script>
  
  <style scoped>
  
  .chat-window {
    /* general styles for the chat window */
    height: 85%;
    overflow-y: auto;
  }
  
  .user {
    text-align: left;
    color: blue;
  }
  
  .assistant {
    text-align: right;
    color: green;
  }
  
  .chat-input {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
  }
    
  .chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
  }
  
  .chat-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    font-size: 24px;
    cursor: pointer;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    transition: background-color 0.3s;
  }
  
  .chat-button:hover {
    background-color: #0056b3;
  }
  
  .chat-box {
    width: 300px;
    height: 400px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    overflow: hidden;
  }
  </style>
  
  