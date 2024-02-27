/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*.html",
    "./account/template/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

