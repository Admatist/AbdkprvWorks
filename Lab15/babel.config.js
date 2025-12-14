// babel.config.js

module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current', // Нацеливаем Babel на текущую версию Node.js
        },
      },
    ],
  ],
};