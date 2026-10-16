// From the live Ecwid store categories (audit 5.12 and 5.13). Names standardised.
const STORE = 'https://www.sunderlandhomegrown.co.uk/store'
export const events = [
  {
    title: 'Halloween craft workshop', date: 'Tue 20 Oct 2026', iso: '2026-10-20', time: '12:30pm to 1:30pm',
    who: 'Children aged 6 to 11', price: '£5', audience: 'children', href: `${STORE}/Workshops-c196026760`, img: 'shop-dog-pansies',
  },
  {
    title: 'Halloween lantern workshop', date: 'Mon 26 Oct 2026', iso: '2026-10-26', time: '[CONFIRM: time]',
    who: 'Children aged 6 to 11', price: '£7.50', audience: 'children', href: `${STORE}/Workshops-c196026760`, img: 'squash-polytunnel',
  },
  {
    title: 'Halloween lantern workshop', date: 'Fri 30 Oct 2026', iso: '2026-10-30', time: '[CONFIRM: time]',
    who: 'Young people aged 12 to 16', price: '£7.50', audience: 'children', href: `${STORE}/Workshops-c196026760`, img: 'veg-harvest',
  },
  {
    title: 'Junior Joiners', date: '[CONFIRM: dates]', iso: '', time: '[CONFIRM: time]',
    who: 'Two groups: ages 11 to 13 and 14 to 16', price: '£20', audience: 'children', soldOut: true, href: `${STORE}/Workshops-c196026760`, img: 'bird-box-joinery',
  },
  {
    title: 'Christmas wreath workshop', date: '13 dates, Wed 25 Nov to Fri 11 Dec 2026', iso: '2026-11-25', time: '1pm',
    who: 'Adults', price: '£20 or £25 [CONFIRM: what the difference is]', audience: 'adults', note: 'Some dates are sold out.', href: `${STORE}/Christmas-c66618691`, img: 'primroses',
  },
]

export const groups = [
  { title: 'Fruit and veg growing group', when: 'Every Monday, 10am to 12 noon', where: 'Home Grown, Thompson Park', href: 'community.html#fruit-veg' },
  { title: 'Local history and heritage group', when: 'Twice a month [CONFIRM: days]', where: 'The Park Café, Thompson Park', href: 'community.html#groups' },
  { title: 'Beekeeping', when: '[CONFIRM: when]', where: 'Home Grown, Thompson Park', href: 'community.html#groups' },
]
