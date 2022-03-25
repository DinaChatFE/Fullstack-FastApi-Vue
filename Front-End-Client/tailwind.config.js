module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: { display: ["'Inter', sans-serif"] },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [ require('@tailwindcss/line-clamp'),],
};
