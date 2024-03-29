---
id: 750fbc08-13aa-4752-bb37-877740948de0
title: Alert Fatigue
desc: ''
updated: 1642957322270
created: 1616191957845
---
Notes from [this tech talk](https://vimeo.com/274820572) by Aditya Mukherjee.

# STAT framework for thinking about each alert

- Supported
- Trustworthy
  - Do I trust this alert to notify me when a problem happens?
  - Will it stay silent if things are ok?
  - Will it give me enough info to diagnose problems?
- Actionable
  - At most one decision should be required ideally, the decision to whether take an action or not.
  - Alerts that are difficult to action become alerts that are ignored. If an alert is painful or annoying to action, you'll feel fatigued next time.
  - Should try to avoid stuff like "investigate" etc, make things more optional. Decision trees, interactive tooling etc is much better.
  - If it's unclear who should be taking action, the alert is not actionable.
- Triaged
