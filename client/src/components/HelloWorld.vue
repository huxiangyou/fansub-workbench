<template>
    <div>
        <el-input placeholder="请输入内容" v-model="text"> </el-input>
        <el-button type="primary" @click="onSubmit">测试</el-button>
        {{ result }}
    </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    data() {
        return {
            text: 'test',
            result: ''
        };
    },
    methods: {
        onSubmit() {
            this.axios
                .post('/api/test', { text: this.text })
                .then(res => {
                    this.result = res;
                })
                .catch();
            return '1';
        }
    }
};
</script>

<style scoped></style>
