---
id: 489506b0-a92b-4025-8a8a-7cfef877aae2
title: Threat Modeling
desc: ''
updated: 1642958540432
created: 1616192041148
---

A threat model is a living artifact that helps us reason about the security of a system.

Threat modeling helps define system appropriate security requirements and helps
find security issues that might not be found otherwise. For example, it is impossible
for automated tools to realize that some flow needs authorization.

A threat model should contain the following things:

* Some form of system diagram -- Anything will do as long as long as it helps us understand the system.
* List of viable threats -- Viable is key here, because there could be an infinite number of possible threats.
* List of prioritized mitigations done or planned
* List of assumptions made

The questions you should ask yourself while threat modeling are:
* What are you building?
* What can go wrong?
* What should you do about the things that can go wrong?
* Did you do a decent job of analysis?

There are methods that can be used to come up with threats, for the second question:

* [[STRIDE|engineering.security.stride]]
* Abuser stories
* Threat Lists ([CAPEC](https://samate.nist.gov/BF/Enlightenment/CAPEC.html))
* Vulnerability Lists ([OWASP Top 10](https://owasp.org/www-project-top-ten/) etc)
