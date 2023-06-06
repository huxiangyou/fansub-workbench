<template>
    <div id="signUp">
        <el-input placeholder="用户名" v-model="username" />
        <el-input placeholder="密码" v-model="password" show-password />
        <el-button type="primary" @click="signUp">注册</el-button>
        <el-button type="text" @click="login">登录</el-button>
    </div>
</template>

<script>
export default {
    name: 'signUp',
    data() {
        return {
            username: '',
            password: '',
            result: ''
        };
    },
    methods: {
        signUp() {
            this.axios
                .post('/api/signUp', { text: this.text })
                .then(res => {})
                .catch();
        },
        login() {
            this.$router.push('/login');
        }
    }
};
</script>

<style scoped>
#signUp {
    max-width: 300px;
    padding: 12px;
}
</style>
