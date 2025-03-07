---
id: njqts253mv1fp9o0jkcw1fe
title: param.plan
desc: ''
updated: 1738077473064
created: 1734181349831
---

_daily notes inspired by (but not exactly) [john carmack's plan](https://github.com/ESWAT/john-carmack-plan-archive)_

# 2025-01-28

- i'm gonna work on a single review button today
- goal is to write as much of the code with ai as possible to ship quickly

# 2025-01-26

- i start with the intention to write an actual feature for the blunderfest app
but then fall into the rabbithole of sharing code as much as possible with the
frontend app and then suddenly it's two hours with nothing to show for it
but a bunch of refactoring and errored out code.
- [[blunderfest.what-it-needs]]

# 2025-01-13

- it's 4 am right now, woke up at 2:30 am and haven't slept since.
- simple solution to fix sleep is to stay awake until ~8 in the evening tonight
- writing a [[blog|blog.great-by-choice]] about [[books.great-by-choice]]
- shipped a version: https://newsletter.param.codes/p/great-by-choice
- why am i doing everything except writing code for blunderfest?


# 2025-01-12

- in the us, can't sleep. will just remain awake until the evening and see if i can sleep then.
- did some clean up of blunderfest
- creating a `@blunderfest/core` package that i can share code with was a good idea.
- am i weird for travelling so many miles to san francisco for work and then doing nothing but
staying in the hotel room on the laptop?
--

# 2025-01-06

- office has started
- i need to figure out how to reuse code between the webapp and the phone app
for game review. i don't want to rewrite the entire thing but maybe that is what is needed actually?
- need claude rn

---

# 2025-01-05


- watched [[films.whisper-of-the-heart]].
- disappointing that i won't be able to ship the app after the holidays but excited that at least i'm working on it.
- i am obsessed with getting blunderfest to be more successful.
- first we ship the app to myself, make it addictive to myself and then go from there.
- seperated the api client into a new package, blunderfest is becoming a real monorepo at this point lmao
- average dev doing a refactor instead of building the damn feature.
- watched [[films.my-neighbour-totoro]]


---

# 2025-01-04

- ran 10k slow, supposed to be easy but my heart rate did get into 160s by the middle of it
- need to build more stamina, should maybe keep running this pace until hr starts staying in 150
- unsure if i'll be able to sit for much time today with apartment viewings etc

---
## 2025-01-03

what do i need to do to ship the app

1. user must be able to sign up and sign in
2. there needs to be an onboarding flow so that they can add lichess username etc.
3. game review must work


#1 is near done, i need to figure out how to integrate sign up into the stuff
#2 is less complicated than game review, so most probably i should focus on making game review work first.

first a haircut, then we get back to this.

during haircut some reading [[books.great-by-choice]].

7:30 pm

haircut etc done, now to get back to coding.

- ig we start by creating a game review page and then adding a chessboard.
- will just use a hardcoded game for now.
- okay game review page created, and a button added that takes the user there when
logged in
- game review page now has a chess board rendering (that's admittedly a little slow).

---

## 2025-01-02

- need to finish sign in etc today.
- the sign in flow is weird, it seems to be starting, but not ending correctly
- there is an allowlist of redirect urls for mobile apps on the clerk dashboard but it won't let me add anything to it
- i'm pretty sure it's a bug in the oauth thing, sad that clerk doesn't have prebuilt expo components i can use here.
- seems to work normally in this video: https://www.youtube.com/watch?v=xp4fd78Hh5A so i'm not sure what i'm doing wrong
- lmfao the bug was that ClerkProvider need to be actually at the top level, and I had TamaguiProvider above it.
- diff looks like this

```diff
   return (
-    <TamaguiProvider config={tamaguiConfig}>
-      <ClerkProvider publishableKey={publishableKey}>
+    <ClerkProvider publishableKey={publishableKey} tokenCache={tokenCache}>
+      <TamaguiProvider config={tamaguiConfig}>
         <ClerkLoaded>
           <Slot />
         </ClerkLoaded>
-      </ClerkProvider>
-    </TamaguiProvider>
+      </TamaguiProvider>
+    </ClerkProvider>
   );
```

- ok now that sign in works, i guess i should move on to the main focus to actually building functionality.
- need to understand how to make api requests.
- ran 8 km to make up for only running 2 km on tuesday.

---

## 2025-01-01

- sign in is _working_ on the app (for some definition of working).
- need to build a sign out for better devexp
- reading [[books.great-by-choice]]
- some notes:
    - 10xers have a few qualities
    - discipline
    - belief in empirical evidence
    - paranoia
    - ambition

quote:

>10Xers then bring this idea to life by a triad of core behaviors: fanatic discipline, empirical creativity, and productive paranoia. Animating these three core behaviors is a central motivating force, Level 5 ambition.

---

## 2024-12-31

- trying to get sign in stuff working
- claude capacity issues pita


## 2024-12-16

- no run today
- travel back to blr, took a good photo
- renewed the domain for blunderfest
- also bought blunderfest.com

## 2024-12-15

- no run yet, but hoping to run in the evening
- aus 301/3, rohit needs to retire

## 2024-12-14

- run 5k
- figure out where to go next with blunderfest
- potential ideas
    - app

notes:
* https://x.com/iliekcomputers/status/1867984093440602224