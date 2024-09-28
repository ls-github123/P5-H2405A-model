<template>
  <div id="app">
    <h1>Server-Sent Events Example</h1>
    <ul>
      <li v-for="(message, index) in messages" :key="index">{{ message }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: []
    };
  },
  mounted() {
    this.connectToSSE();
  },
  methods: {
    connectToSSE() {
      const eventSource = new EventSource('http://localhost:8000/sse/?ask=小米是谁');

      eventSource.onmessage = (event) => {
        this.messages.push(event.data);
       
      };

      eventSource.onerror = (error) => {
        console.error('EventSource failed:', error);
        eventSource.close();
      };
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>