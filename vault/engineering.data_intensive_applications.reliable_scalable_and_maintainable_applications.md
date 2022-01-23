---
id: 665411d4-e320-4768-b3b6-a5c0c5d1eeb1
title: Chapter 1 - Reliable, Scalable and maintainable applications
desc: ''
updated: 1642957231415
created: 1616351795299
---

Chapter 1 of [[engineering.data_intensive_applications]]

* Data systems don't fit into clear categories now, redis is used for queues, kafka has database like durability guarantees.
* Application code is responsible for making sure data remains consistent between any number of data systems the application might not be using.
* Each application made from smaller data systems is a new data system. You're also a data system designer.
* Lots of tricky questions: ensure correctness, design a good API, reliability, performance.
* Many factors influence design: skills and experience of people, timescale for delivery etc.
* Three concerns that are most important in systems:
  * Reliability
  * Scalability
  * Maintainability

### Reliability

* Application should performs the function that the user expected
* Should tolerate the user making mistakes.
* Performance should be good enough
* Should prevent unauthorized access and abuse
* Things that can go wrong are called _faults_.
* _Failures_ are when the system as a whole stops providing the required service to the user.
* Fault tolerance doesn't mean being tolerant of ALL faults.
* It's best to try to design a system that prevents faults from causing failures, i.e it tolerates faults.
* You also want to prevent certain types of faults like security issues.

#### Hardware faults

* Hard disk crashes, power faults etc.
* Usually, add redundancy to mitigate this issue.

#### Software errors

* Hardware failures are generally not related, but correlated software bugs can cause the entire system to go down.
* Systematic errors can be avoided by thorough testing, carefully thinking about assumptions and interactions in the system.

#### Human errors
* Humans are unreliable.
* Make it easy to do the right thing.
* Decouple experimentation by providing a sandbox environment.
* Test thoroughly.
* Allow quick and easy recovery from human errors.
* Set up detailed and clear monitoring.
