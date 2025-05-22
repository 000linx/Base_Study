<template>
    <div class="verification-login">
        <el-form ref="verificationForm" :model="verificationForm" label-position="top">
            <el-form-item label="手机号" prop="phone">
                <el-input v-model="verificationForm.phone" placeholder="请输入手机号"></el-input>
            </el-form-item>

            <el-form-item label="验证码">
                <div class="verification-row">
                    <el-input v-model="verificationForm.code" placeholder="请输入验证码" style="width: 160px;"></el-input>
                    <el-button type="primary" class="get-code-btn"
                        :disabled="isCounting || verificationForm.phone === ''" @click="handleGetCode">
                        {{ isCounting ? `${countdown}秒后重试` : '获取验证码' }}
                    </el-button>
                </div>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" class="submit-btn" @click="handleSubmit" :loading="loading">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            verificationForm: {
                phone: '',
                code: ''
            },
            isCounting: false,
            countdown: 60,
            timer: null,
            loading: false
        }
    },
    methods: {
        handleGetCode() {
            // 这里添加获取验证码逻辑，如API请求
            console.log('获取验证码请求:', this.verificationForm.phone);

            if (!/^1[3-9]\d{9}$/.test(this.verificationForm.phone)) {
                this.$message.error('请输入正确的手机号码');
                return;
            }

            this.isCounting = true;
            this.timer = setInterval(() => {
                this.countdown--;
                if (this.countdown <= 0) {
                    clearInterval(this.timer);
                    this.isCounting = false;
                    this.countdown = 60;
                }
            }, 1000);

            // 模拟API延迟请求
            setTimeout(() => {
                this.$message.success('验证码已发送，请注意查收！');
            }, 1000);
        },

        handleSubmit() {
            // 这里添加验证码登录逻辑，如API请求
            console.log('验证码登录请求:', this.verificationForm);
            this.loading = true;

            // 模拟API延迟请求
            setTimeout(() => {
                this.loading = false;
                this.$message.success('登录成功！');
                // 这里可以添加跳转逻辑
            }, 1500);
        }
    },
    beforeDestroy() {
        if (this.timer) {
            clearInterval(this.timer);
        }
    }
}
</script>

<style scoped>
.verification-row {
    display: flex;
    align-items: center;
}

.get-code-btn {
    margin-left: 10px;
}

.submit-btn {
    width: 100%;
    margin-top: 10px;
}
</style>