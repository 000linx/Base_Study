<template>
    <div id="app">
        <Header />
        <div class="container">
            <Login />
        </div>
        <Footer />
    </div>
</template>

<script>
// import Header from '@/components/Header.vue'
// import Footer from '@/components/Footer.vue'
import Login from '@project/templeta/Login.vue'

export default {
    name: 'App',
    components: {
        // Header,
        // Footer,
        Login
    }
}
</script>

<style>
/* 全局样式 */
body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background-color: #f5f5f5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

#app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

/* 为确保 Header 和 Footer 正确显示 */
Header {
    margin-bottom: 20px;
}

Footer {
    margin-top: auto;
}
</style>