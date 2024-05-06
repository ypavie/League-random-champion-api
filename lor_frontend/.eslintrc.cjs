/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
<<<<<<< HEAD
    "plugin:vue/recommended",
  ],
  "rules": {
    "comma-dangle": "error",
    "quotes": [
      "error",
      "single"
    ],
    "linebreak-style": [
      "error",
      "unix"
    ],
    "array-bracket-spacing": [
      "error",
      "always"
    ],
    "semi": [
      "error",
      "always"
    ],
    "eol-last": [
      "error",
      "always"
    ],
    "indent": [
      "error",
      2
    ]
  },
  "parserOptions": {
    "parser": "babel-eslint",
    "sourceType": "module",
    "allowImportExportEverywhere": true,
    "ecmaVersion": 'latest'
=======
    '@vue/eslint-config-prettier/skip-formatting'
  ],
  parserOptions: {
    ecmaVersion: 'latest'
>>>>>>> main
  }
}
