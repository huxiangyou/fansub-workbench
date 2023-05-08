// https://eslint.org/docs/user-guide/configuring

module.exports = {
    root: true,
    parserOptions: {
        parser: 'babel-eslint'
    },
    env: {
        browser: true,
        node: true
    },
    extends: [
        'plugin:vue/essential',
        'eslint:recommended',
        '@vue/prettier'
    ],
    plugins: [
        'vue'
    ],
    rules: {
        'array-callback-return': 'error',
        'eqeqeq': ['error', 'allow-null'],
        'generator-star-spacing': 'off',
        'indent': ['warn', 4],
        'no-async-promise-executor': 'off',
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-empty': ['error', { allowEmptyCatch: true }],
        'no-multi-spaces': 1,
        'no-multiple-empty-lines': ['warn', { max: 1 }],
        'no-redeclare': 'error',
        'no-unneeded-ternary': 'error',
        'no-unused-vars': 'off',
        'prettier/prettier': ['warn', {
            singleQuote: true,
            trailingComma: 'none',
            printWidth: 80
        }],
        'semi': ['warn', 'always'],
        'quotes': ['warn', 'single'],
        'spaced-comment': ['error', 'always', { 'exceptions': ['-', '+', '/'] }],
        'valid-jsdoc': 'off',
        'vue/valid-v-for': 'off',
    }
}
