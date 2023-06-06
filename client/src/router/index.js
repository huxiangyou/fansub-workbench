import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'HelloWorld',
            component: () => import('@/components/HelloWorld')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('@/components/login')
        },
        {
            path: '/signUp',
            name: 'signUp',
            component: () => import('@/components/signUp')
        }
    ]
});
