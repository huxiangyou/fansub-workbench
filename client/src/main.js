import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import md5 from 'js-md5';
import 'element-ui/lib/theme-chalk/index.css';
import utils from '@/components/utils';

Vue.config.productionTip = false;
Vue.prototype.axios = axios;
Vue.use(ElementUI);
Vue.prototype.md5 = md5;

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
});
