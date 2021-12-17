---
id: dDDiCBu9TvHsRjiGgtoA3
title: Week of December 17, 2021
desc: ''
updated: 1639772414556
created: 1639253713452
---

# log4j

[Fastly](https://www.fastly.com/blog/digging-deeper-into-log4shell-0day-rce-exploit-found-in-log4j) has a good explanation of the log4j vulnerability that allowed easy remote code execution by attackers. Lots of hugs to all the engineers who were on-call this week.

In a nutshell, if you somehow log a specific type of URL, the library was looking up the URL and dynamically loading code that the URL might be sending back. It's a pretty crazy exploit, it's very weird to me that a logging library is ever looking up URLs. That just seems like the *last* thing you'd expect a logging library to do.

The [GitHub pull request](https://github.com/apache/logging-log4j2/pull/608) fixing it was really interesting. There was a [comment](https://github.com/apache/logging-log4j2/pull/608#issuecomment-990065982) that stood out to me.

>It is very surprising that this critical security issue does not seem to have received due attention. It was reported to Apache half a month ago, but it was not fixed until five days ago. Even today, it has not released a new stable version to solve it.

I don't think it's surprising. It's definitely not ideal, but it's not surprising. The fact that open source is massively underfunded is basically a meme at this point. I always like linking this [xkcd comic](https://xkcd.com/2347/) because it's just so true.

I worked on open-source software for years with MetaBrainz, which is probably much better funded than most other open-source projects, but even still, going from MetaBrainz to Stripe was such culture shock to me, because the engineering resources that were available was just on another level. Things can get prioritized, it's not just one developer wearing ten hats, doing development, code review, releases, support. It's very easy to miss things even if you're working full time, and most of open-source is developed by people in their free time, outside of their regular job.

Luckily, the main developer of log4j now has [hundreds of supporters](https://github.com/sponsors/rgoers), but that's just log4j, there are probably so many core infrastructural open source projects that have near zero engineering resources behind them. If you use and like something open-source, you should try to support the creators and donate.


# Things of interest

I read this great blog post this week: https://lyncredible.com/2020/04/06/reflecting-on-my-ic-path-part-i/

>I finally realized that careers are not like schools. In schools, grades are leading indicators. At the start of every school year, you level up, learn some new lessons and work on some new projects. In careers however, getting a good grade and finishing a year does not guarantee a level up into the next grade. Instead, I should treat leveling as a lagging indicator. The change has to start with my mindset and my behavior. After all, most every tech company requires you to already perform at the next level before leveling you up.

-------------------

ListenBrainz released an [Year in Music](https://listenbrainz.org/user/iliekcomputers/year-in-music/) report for 2021. This is one project that I always wanted to build in my years of working on ListenBrainz. Sadly, I wasn't involved because it's hard for me to manage time, but I'm still really happy to see it built. Also, no real surprise that no meeting wednesday is the day I listened to the most music on average.

----------------------

I'm reading [a book by Stephen Webb](https://www.amazon.in/gp/product/B00XVTG1NC/ref=ppx_yo_dt_b_d_asin_title_o01?ie=UTF8&psc=1) on the Fermi Paradox and was introduced to the absolutely mind-boggling idea of a [Dyson Sphere](https://en.wikipedia.org/wiki/Dyson_sphere). It's so amazing to think how people even imagine this kind of stuff and it also shows just how much scope for technological progress there exists in the world.

-----------------

Stripe announced an [increase in carbon removal commitments](https://stripe.com/newsroom/news/fall-21-carbon-removal-purchases) this week. The work that the Climate team does is probably my favorite thing at Stripe, it makes me proud to work here. It's very cool that Stripe will be the first customer for 3 of the 4 carbon removal projects.
