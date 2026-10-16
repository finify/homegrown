import forms from '@tailwindcss/forms'
/**
 * Brand tokens for Sunderland Home Grown.
 * Colours are sampled from the Home Grown roundel: the three leaves
 * (leaf green, gold, berry) held in a hand, set on a deep forest green.
 *
 * Contrast pairs checked to WCAG 2.2 AA (see README):
 *   forest on ground 11.7:1 · soft on ground 8.6:1 · forest on gold 6.8:1
 *   white on berry 6.1:1   · white on forest 12.6:1 · forest on leaf 4.9:1
 * Never set white text on leaf green or gold.
 */
export default {
  content: ['./*.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      colors: {
        ground: '#F6F7F2', // page background (polytunnel white)
        stone: '#ECEEE6', // one tone step from ground, for surfaces
        ink: '#14231A', // running text
        soft: '#3F4A42', // secondary text, still AA
        forest: { DEFAULT: '#173A22', 700: '#1F4D2E', 900: '#0E2615' },
        leaf: { DEFAULT: '#3DB82A', pale: '#E3F2DC' },
        gold: { DEFAULT: '#E9B82B', pale: '#FBF0CB' },
        berry: { DEFAULT: '#934F4E', pale: '#F3E4E2' },
        hand: '#C5AB86',
      },
      fontFamily: {
        sans: ['"Atkinson Hyperlegible Next"', '"Atkinson Hyperlegible"', 'system-ui', 'sans-serif'],
      },
      fontSize: {
        // Five steps only: small, body, lead, title, display
        sm: ['0.9375rem', { lineHeight: '1.5' }],
        base: ['1.125rem', { lineHeight: '1.6' }],
        lead: ['clamp(1.375rem, 1.9vw, 1.75rem)', { lineHeight: '1.35' }],
        title: ['clamp(2rem, 3.8vw, 3.5rem)', { lineHeight: '1.04', letterSpacing: '-0.025em' }],
        display: ['clamp(2.75rem, 6.6vw, 6.25rem)', { lineHeight: '0.98', letterSpacing: '-0.035em' }],
      },
      borderRadius: {
        // The leaf: two opposite corners rounded, two sharp. One shape, every scale.
        leaf: '1.5rem 0.25rem',
        'leaf-lg': '3rem 0.375rem',
      },
      maxWidth: { page: '88rem' },
    },
  },
  plugins: [forms],
}
