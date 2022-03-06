module.exports = {
  env: {
    browser: true,
    es2022: true,
  },
  extends: [
    'plugin:react/recommended',
    'airbnb-typescript',
    'airbnb',
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 13,
    sourceType: 'module',
    project: './tsconfig.json',
    tsconfigRootDir: __dirname,
  },
  plugins: [
    'react',
    '@typescript-eslint',
  ],
  rules: {
    'react/jsx-no-constructed-context-values': 'off',
    'jsx-a11y/label-has-associated-control': 'off',
    'react/function-component-definition': [
      'error',
      {
        namedComponents: 'arrow-function',
        unnamedComponents: 'arrow-function',
      },
    ],
    'react/jsx-filename-extension': ['warn', { extensions: ['.js', '.jsx', '.ts', '.tsx'] }],
  },
  settings: {
    'import/resolver': 'webpack',
  },
};
