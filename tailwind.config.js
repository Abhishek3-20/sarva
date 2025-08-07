module.exports = {
    content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
      "./courses/templates/**/*.html",
      "./users/templates/**/*.html"
    ],
    theme: {
      extend: {
        fontFamily: {
          sans: ['Inter', 'sans-serif'],
        },
      },
    },
    plugins: [
      require('@tailwindcss/typography'),
      require('@tailwindcss/forms'),
      require('@tailwindcss/aspect-ratio'),
      require('@tailwindcss/line-clamp'),
      require('daisyui'),
    ],
    daisyui: {
      themes: ["light", "dark", "cupcake"],
    },
  }