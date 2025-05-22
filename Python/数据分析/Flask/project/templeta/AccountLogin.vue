<template>
    <div class="account-login">
        <el-form ref="accountForm" :model="accountForm" :rules="rules" label-position="top">
            <el-form-item label="用户名/手机号" prop="username">
                <el-input v-model="accountForm.username" placeholder="请输入用户名或手机号"></el-input>
            </el-form-item>

            <el-form-item label="密码" prop="password">
                <el-input v-model="accountForm.password" type="password" placeholder="请输入密码" show-password></el-input>
            </el-form-item>

            <div class="form-footer">
                <div class="remember-box">
                    <el-checkbox v-model="accountForm.rememberMe">记住我</el-checkbox>
                </div>
                <div class="forgot-password">
                    <a href="#">忘记密码？</a>
                </div>
            </div>

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
            accountForm: {
                username: '',
                password: '',
                rememberMe: false
            },
            rules: {
                username: [
                    { required: true, message: '请输入用户名或手机号', trigger: 'blur' },
                    { min: 5, max: 20, message: '长度在 5 到 20 个字符', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '请输入密码', trigger: 'blur' },
                    { min: 6, max: 16, message: '长度在 6 到 16 个字符', trigger: 'blur' }
                ]
            },
            loading: false
        }
    },
    methods: {
        handleSubmit() {
            this.$refs.accountForm.validate((valid) => {
                if (valid) {
                    this.loading = true;
                    // 这里添加登录逻辑，如API请求
                    console.log('账号密码登录请求:', this.accountForm);
                    // 模拟API延迟请求
                    setTimeout(() => {
                        this.loading = false;
                        this.$message.success('登录成功！');
                        // 这里可以添加跳转逻辑
                    }, 1500);
                }
            });
        }
    }
}
</script>

<style scoped>
.account-login {
    max-width: 100%;
}

.form-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.submit-btn {
    width: 100%;
    margin-top: 10px;
}

.forgot-password a {
    color: #409eff;
    text-decoration: none;
}

.forgot-password a:hover {
    text-decoration: underline;
}
</style>