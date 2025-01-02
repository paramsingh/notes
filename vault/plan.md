---
id: njqts253mv1fp9o0jkcw1fe
title: param.plan
desc: ''
updated: 1735806527204
created: 1734181349831
---

_inspired by (but not exactly) [john carmack's plan](https://github.com/ESWAT/john-carmack-plan-archive)_

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