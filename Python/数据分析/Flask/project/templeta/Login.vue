<template>
    <div class="login-container">
        <div class="login-box">
            <h1 class="login-title">用户登录</h1>

            <div class="login-tabs">
                <button :class="{ active: activeTab === 'account' }" @click="activeTab = 'account'">账号密码登录</button>
                <button :class="{ active: activeTab === 'verification' }"@click="activeTab = 'verification'">验证码登录</button>
                <button :class="{ active: activeTab === 'qrcode' }" @click="activeTab = 'qrcode'">二维码登录</button>
            </div>

            <div class="login-content">
                <AccountLogin v-if="activeTab === 'account'"></AccountLogin>
                <VerificationLogin v-if="activeTab === 'verification'"></VerificationLogin>
                <QRCodeLogin v-if="activeTab === 'qrcode'"></QRCodeLogin>
            </div>
        </div>
    </div>
</template>

<script>
    import AccountLogin from '@/project/templeta/AccountLogin.vue'
    import VerificationLogin from '@/project/templeta/VerificationLogin.vue'
    import QRCodeLogin from '@/project/templeta/QRCodeLogin.vue'

    export default {
        components: {
            AccountLogin,
            VerificationLogin,
            QRCodeLogin
        },
        data() {
            return {
                activeTab: 'account'  // 默认显示账号密码登录
            }
        }
    }
</script>

<style scoped>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f5f5f5;
    }

    .login-box {
        width: 400px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        padding: 30px;
    }

    .login-title {
        text-align: center;
        margin-bottom: 30px;
        color: #333;
    }

    .login-tabs {
        display: flex;
        margin-bottom: 25px;
    }

    .login-tabs button {
        flex: 1;
        padding: 10px;
        background-color: transparent;
        border: none;
        cursor: pointer;
        font-size: 14px;
        color: #666;
    }

    .login-tabs button.active {
        color: #409eff;
        border-bottom: 2px solid #409eff;
        font-weight: bold;
    }

    .login-content {
        margin-top: 20px;
    }

    button:active {
        opacity: 0.8;
    }

    </style>