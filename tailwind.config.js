module.exports = {
  content: [
    './templates/**/*.html',
    './static/src/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        educademy: {
          "primary": "#EDAFB8",   // soft pink
          "secondary": "#F7E1D7", // pale blush
          "accent": "#DEDBD2",    // warm beige
          "neutral": "#4A5759",   // charcoal
          "base-100": "#B0C4B1",  // sage green bg
        },
      },
      "light",
      "cupcake",
      "corporate",
      "synthwave",
      "valentine",
      "dark",
    ],
  },
}
