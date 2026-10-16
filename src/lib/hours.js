// Opening times from the site footer. Times are minutes after midnight, UK time.
const WEEKDAY = { open: 600, close: 960 } // 10:00–16:00
const WEEKEND = { open: 570, close: 930 } // 09:30–15:30

const fmt = (m) => {
  const h = Math.floor(m / 60), min = m % 60
  const h12 = ((h + 11) % 12) + 1
  return `${h12}${min ? ':' + String(min).padStart(2, '0') : ''}${h < 12 ? 'am' : 'pm'}`
}
const DAY_NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
const slot = (day) => (day === 0 || day === 6 ? WEEKEND : WEEKDAY)

/** Where is the garden centre right now? Uses Europe/London regardless of the visitor's clock. */
export function openStatus(now = new Date()) {
  const parts = Object.fromEntries(
    new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23' })
      .formatToParts(now).map((p) => [p.type, p.value]),
  )
  const day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(parts.weekday)
  const mins = Number(parts.hour) * 60 + Number(parts.minute)
  const today = slot(day)
  if (mins >= today.open && mins < today.close) {
    const left = today.close - mins
    return { open: true, text: `Open now`, detail: `Closes at ${fmt(today.close)}${left <= 60 ? `, in ${left} minutes` : ''}` }
  }
  if (mins < today.open) return { open: false, text: 'Closed right now', detail: `Opens today at ${fmt(today.open)}` }
  const next = (day + 1) % 7
  return { open: false, text: 'Closed right now', detail: `Opens tomorrow (${DAY_NAMES[next]}) at ${fmt(slot(next).open)}` }
}
