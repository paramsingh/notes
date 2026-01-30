
Last day of March.

I tried making a secret URL to get GPT-4 to run stories. However, it's slow as shit.
Each completion takes more than the 10s timeout on vercel. So I either move it off of
vercel or get GPT-4 to be faster.

I was trying to get it to stream but it's more complex than the javascript I know.
Need to do another pass later. But it still won't solve the problem of th 10s timeout.
The interesting thing is that if I add the streams, I might be able to get rid of
the prefetch and the race conditions.
