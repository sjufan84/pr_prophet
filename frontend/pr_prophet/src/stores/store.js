// store.js
import { reactive } from 'vue'

export const store = reactive({
  // Set the initial state of the store to a list of messages
  chat_history: []
})