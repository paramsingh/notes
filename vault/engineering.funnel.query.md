---
id: a0241f76-d02d-47b3-9324-23417efe24e1
title: Query
desc: ''
updated: 1642957276628
created: 1620851928356
---

select email, count(c.id) as cnt
  from tblboard b
  join tblcard c
    on b.id = c.boardid
group by email
order by cnt desc;
