**Postmortem Readme - 0x19 Web Stack Debugging**

# Background Context

In the fast-paced world of tech, failures are inevitable. Bugs, traffic spikes, security hiccups - you name it. 
But the key is to learn from these mishaps, and that's where postmortems come into play. 
They're not just summaries; they're golden opportunities to grow and ensure the same mistakes don't haunt you twice.

## Resources

Before diving in, here are some resources to get you in the postmortem mood:

- [Incident Report, also referred to as a Postmortem](https://en.wikipedia.org/wiki/Post-mortem_(computing))
- [The importance of an incident postmortem process](https://blog.pagerduty.com/why-you-need-incident-postmortems/)
- [What is an Incident Postmortem?](https://www.blameless.com/blog/incident-postmortem)

## Tasks

### 0. **My First Postmortem**

You've got the chance to be a postmortem rockstar! Whether it's a real outage or a creative concoction, spill the beans on the issue you faced. Be clear, concise, and dive into the nitty-gritty.

#### Requirements:

**Issue Summary:**
- **Duration:**
  - *Start Time:* 2023-03-15 14:30 SAST
  - *End Time:* 2023-03-15 18:45 SAST
  - *Duration:* Approximately 4 hours and 15 minutes

- **Impact:**
  - The IoT app took an unplanned siesta in South Africa.
  - Users stared at screens, wondering if their data was on vacation.
  - Around 35% of our South African users embraced an unexpected "zen moment."

- **Root Cause:**
  - Blame it on the server: Flask API decided to play hard to get, rejecting love letters (data) from our ESP32 devices due to a strict security diet.

**Timeline:**
- **Detection:**
  - *Time:* 2023-03-15 14:30 SAST
  - *How:* Monitoring system screamed louder than a rock concert as data transmission dropped faster than a hot potato.

- **Actions Taken:**
  - Played detective in server logs, looking for clues like it's a crime scene.
  - Suspected a network bottleneck, thinking our data got stuck in traffic.
  - Called in the network team to untangle the spaghetti of connections.

- **Misleading Paths:**
  - First, we interrogated the ESP32 devices, suspecting a rebellion.
  - Accused the DHT11 and MQ135 sensors of spreading fake news.
  - Even considered a DDoS attack, thinking our app became the hottest party in town.

- **Escalation:**
  - We yelled for backup, bringing in the DevOps and Networking heroes to join our quest for truth.

- **Resolution:**
  - Turns out, our Flask server was on a diet—too strict! We loosened its security belt, and voila, data started flowing again.
  - Applied the fix faster than you can say "Flask and ESP32 got their love story back."

**Root Cause and Resolution:**
- **Root Cause:**
  - Flask API's security settings were like a bouncer at a fancy club, turning away our ESP32 devices at the door.

- **Resolution:**
  - We gave the bouncer a pep talk, adjusted the settings, and suddenly the club was rocking again.
  - Tested it more thoroughly than your grandma tests soup temperature.

**Corrective and Preventative Measures:**
- **Improvements/Fixes:**
  - Upgraded our monitoring system to scream louder than a rock concert in your living room.
  - Implemented automatic server configuration checks to catch misbehaving settings before they misbehave.

- **Tasks:**
  - Conducted a thorough review of server configurations, making sure it's not secretly on a diet.
  - Set up automated tests for server configurations, because manual testing is so last season.
  - Updated our documentation with more "do this, not that" tips to prevent future oopsie-daisies.

### 1. **Make People Want to Read Your Postmortem (Advanced)**
We get it; postmortems can be a snooze-fest. But not yours! Sprinkle some humor, toss in a pretty diagram, or anything 
that'll make your postmortem the talk of the town.

**Pro Tip:** Laughter is the best medicine, even in the tech world.

Now, dive into the [Postmortem Fiesta](https://docs.google.com/document/d/1eC3b1ftWi9JjyLEwb6s5N3TeCIJRgWp2/edit?usp=sharing) and let 
the debugging tales unfold! 🚀
