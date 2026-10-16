// Verified facts only (audit section 2). Anything unknown is marked CONFIRM in the page copy.
export const site = {
  name: 'Sunderland Home Grown CIC',
  phone: '0191 549 9444',
  phoneHref: 'tel:+441915499444',
  emails: ['deb.homegrown@aol.com', 'gary.homegrown@aol.com'],
  proposedEmail: 'hello@sunderlandhomegrown.co.uk',
  address: ['Thompson Park', 'Southwick', 'Sunderland', 'SR5 1SF'],
  facebook: 'https://www.facebook.com/sunderlandhomegrown',
  store: 'https://www.sunderlandhomegrown.co.uk/store',
  hours: [
    { days: 'Monday to Friday', time: '10am to 4pm' },
    { days: 'Saturday and Sunday', time: '9:30am to 3:30pm' },
  ],
}

export const nav = [
  { href: 'day-opportunities.html', label: 'Day opportunities', key: 'day' },
  { href: 'garden-centre.html', label: 'Garden centre', key: 'garden' },
  { href: 'whats-on.html', label: "What's on", key: 'whats' },
  { href: 'community.html', label: 'Community', key: 'community' },
  { href: 'about.html', label: 'About', key: 'about' },
  { href: 'contact.html', label: 'Contact & find us', key: 'contact' },
]

export const supporters = [
  'Sunderland City Council',
  'Coalfields Regeneration Trust',
  'Barclays',
  'National Lottery Community Fund',
  'Power to Change',
  'Youth Investment Fund',
]

export const base = import.meta.env.BASE_URL
export const img = (name) => `${base}img/${name}.jpg`
export const url = (path) => `${base}${path === 'index.html' ? '' : path}`
