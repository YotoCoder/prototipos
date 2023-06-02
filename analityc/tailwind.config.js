/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['templates/admin/*.html'],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
  prefix: '_',
  daisyui: {
    themes:
    ["light",
    "dark",
    "cupcake",
    "bumblebee",
    "emerald",
    "corporate",
    "synthwave",
    "retro",
    "cyberpunk",
    "valentine",
    "halloween",
    "garden",
    "forest",
    "aqua",
    "lofi",
    "pastel",
    "fantasy",
    "wireframe",
    "black",
    "luxury",
    "dracula",
    "cmyk",
    "autumn",
    "business",
    "acid",
    "lemonade",
    "night",
    "coffee",
    "winter",
  ],
  },
}
