<template>
    <div id="login">
        <div id="login-box"></div>
        <el-input placeholder="用户名" v-model="username" />
        <el-input placeholder="密码" v-model="password" show-password />
        <el-button type="primary" @click="login">登录</el-button>
        <el-button type="text" @click="signUp">注册</el-button>
    </div>
</template>

<script>
import utils from '@/components/utils.js';
export default {
    name: 'login',
    data() {
        return {
            utils,
            username: '',
            password: '',
            result: ''
        };
    },
    methods: {
        login() {
            var passwordSalt = '';
            var newPasswordSalt = utils.salt();
            this.axios
                .get('/api/loginSalt', { username: this.username })
                .then(res => {
                    passwordSalt = res.data.passwordSalt;
                })
                .catch();
            this.axios
                .post('/api/login', {
                    username: this.username,
                    passwordHash: this.md5(
                        this.md5(this.password) + passwordSalt
                    ),
                    newPasswordSalt,
                    newPasswordHash: this.md5(
                        this.md5(this.password) + newPasswordSalt
                    )
                })
                .then(res => {})
                .catch();
        },
        signUp() {
            this.$router.push('/signUp');
        }
    }
};
</script>

<style scoped>
#login-box {
    max-width: 300px;
    padding: 12px;
    margin: 12px auto;
}
</style>
