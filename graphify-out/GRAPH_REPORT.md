# Graph Report - tiktok-live-game  (2026-09-23)

## Corpus Check
- 5 files · ~24,473 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1719 nodes · 4109 edges · 97 communities (43 shown, 53 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 224 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d511239b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- three.min.js
- applyMatrix4
- xn
- ve
- pe
- Fe
- ke
- je
- su
- n
- Ga
- .constructor
- update
- _u
- me
- .render
- ui
- gc
- vu
- li
- ie
- Pi
- Hr
- .constructor
- updateMatrixWorld
- .setAttribute
- hu
- .subVectors
- constructor
- copy
- parseObject
- ds
- rr
- xi
- rh
- server.py
- sa
- un
- .multiplyScalar
- .constructor
- Ho
- yn
- th
- .fromBufferAttribute
- so
- ol
- .fromJSON
- clone
- dr
- _h
- .dot
- al
- toJSON
- s
- ue
- dh
- nl
- fr
- fl
- add
- _deactivateAction
- he
- U
- dc
- Panjat Sengsara
- ah
- eo
- getX
- no
- .constructor
- cc
- ch
- Cl
- .normalize
- Ll
- .crossFadeFrom
- .setHSL
- .parse
- zl
- Ul
- dl
- gl
- Jo
- vc
- bh
- clampPoint
- ir
- sh
- or
- to
- Hl
- Ki
- ml
- qs
- xa
- yh

## God Nodes (most connected - your core abstractions)
1. `copy()` - 142 edges
2. `ke` - 110 edges
3. `pe` - 90 edges
4. `xn` - 89 edges
5. `li` - 62 edges
6. `Fe` - 61 edges
7. `Pi` - 53 edges
8. `constructor()` - 46 edges
9. `ve()` - 42 edges
10. `xi` - 41 edges

## Surprising Connections (you probably didn't know these)
- `run()` --calls--> `main()`  [EXTRACTED]
  app.py → server.py

## Import Cycles
- None detected.

## Communities (97 total, 53 thin omitted)

### Community 0 - "three.min.js"
Cohesion: 0.04
Nodes (13): Aa(), bu(), containsPoint(), getAverageFrequency(), getFrequencyData(), _initMemoryManager(), intersectObject(), intersectObjects() (+5 more)

### Community 1 - "applyMatrix4"
Cohesion: 0.05
Nodes (11): el(), els, noop, src, Zt(), applyMatrix4(), El(), Go (+3 more)

### Community 7 - "je"
Cohesion: 0.07
Nodes (10): expandByPoint(), expandByScalar(), getCenter(), getSize(), intersect(), isEmpty(), je, makeEmpty() (+2 more)

### Community 8 - "su"
Cohesion: 0.07
Nodes (8): connect(), disconnect(), getInput(), getOutput(), Qh, su, tu(), A()

### Community 9 - "n"
Cohesion: 0.12
Nodes (21): n(), bindSkeletons(), ia(), load(), a(), c(), loadAsync(), parse() (+13 more)

### Community 10 - "Ga"
Cohesion: 0.07
Nodes (10): Ea, equals(), Ga(), j(), q(), l(), Pn, ta (+2 more)

### Community 11 - ".constructor"
Cohesion: 0.09
Nodes (13): ee(), Gt(), jt(), kt(), qt(), $t(), te(), ce() (+5 more)

### Community 12 - "update"
Cohesion: 0.12
Nodes (22): Ot(), br(), g(), Er(), getParameter(), Ja(), i(), ka() (+14 more)

### Community 13 - "_u"
Cohesion: 0.08
Nodes (4): bind(), getValue(), subscribe_(), _u

### Community 15 - ".render"
Cohesion: 0.13
Nodes (22): Nt(), ha(), S(), T(), lr, T(), Va(), at() (+14 more)

### Community 16 - "ui"
Cohesion: 0.08
Nodes (8): ao, Ba, bc(), di, jc, kc, ui, wc

### Community 17 - "gc"
Cohesion: 0.08
Nodes (12): ac(), _c(), ec(), fc(), gc(), hc(), ic(), oc() (+4 more)

### Community 20 - "ie"
Cohesion: 0.08
Nodes (5): ie(), io, oe(), _r(), setUsage()

### Community 21 - "Pi"
Cohesion: 0.09
Nodes (7): kh, lc(), Pi, qr(), rc(), vr, Yl

### Community 22 - "Hr"
Cohesion: 0.16
Nodes (7): dispose(), Hr, jr(), i(), kr(), Xr(), Zi

### Community 23 - ".constructor"
Cohesion: 0.13
Nodes (8): ge(), qa, remove(), A(), w(), o(), E(), w()

### Community 24 - "updateMatrixWorld"
Cohesion: 0.12
Nodes (4): ar, c(), na(), updateMatrixWorld()

### Community 25 - ".setAttribute"
Cohesion: 0.18
Nodes (3): bi, p(), nc()

### Community 26 - "hu"
Cohesion: 0.11
Nodes (10): _activateAction(), _addInactiveAction(), _addInactiveBinding(), _bindAction(), clipAction(), existingAction(), hu, _lendAction() (+2 more)

### Community 27 - ".subVectors"
Cohesion: 0.14
Nodes (6): closestPointToPoint(), closestPointToPointParameter(), delta(), ii, Ji(), on()

### Community 28 - "constructor"
Cohesion: 0.19
Nodes (11): constructor(), a(), gr(), r(), o(), s(), r(), d() (+3 more)

### Community 30 - "parseObject"
Cohesion: 0.13
Nodes (14): m(), c(), l(), o(), parseObject(), c(), l(), t() (+6 more)

### Community 31 - "ds"
Cohesion: 0.19
Nodes (19): As(), bs(), ds(), fs(), gs(), hs(), ks(), Ns() (+11 more)

### Community 33 - "xi"
Cohesion: 0.10
Nodes (3): mi(), Si, xi

### Community 34 - "rh"
Cohesion: 0.16
Nodes (3): nh, rh, uh

### Community 35 - "server.py"
Cohesion: 0.21
Nodes (15): Satu jendela: server TikTok + game 3D (pywebview/WebView2). Buat .exe: jalanin…, run(), on, help_tier(), main(), on_comment(), on_follow(), on_gift() (+7 more)

### Community 36 - "sa"
Cohesion: 0.12
Nodes (10): _a(), ca(), da(), fa(), Ma(), Oa(), pa(), sa() (+2 more)

### Community 40 - "Ho"
Cohesion: 0.15
Nodes (3): Ho, le(), Oo

### Community 42 - "th"
Cohesion: 0.15
Nodes (3): eh, ih, th

### Community 45 - "ol"
Cohesion: 0.19
Nodes (3): lineTo(), moveTo(), ol

### Community 47 - "clone"
Cohesion: 0.15
Nodes (6): clone(), b(), $i(), oh, Qi(), a()

### Community 49 - "_h"
Cohesion: 0.18
Nodes (6): fh, Fo, _h, Mh, parseImages(), parseImagesAsync()

### Community 51 - "al"
Cohesion: 0.15
Nodes (3): al, Rl, wl()

### Community 52 - "toJSON"
Cohesion: 0.19
Nodes (4): bl, setColors(), toJSON(), r()

### Community 53 - "s"
Cohesion: 0.26
Nodes (9): l(), mc(), s(), B(), G(), H(), L(), O() (+1 more)

### Community 54 - "ue"
Cohesion: 0.22
Nodes (9): De(), fi(), setW(), setX(), setXY(), setXYZW(), setY(), setZ() (+1 more)

### Community 59 - "add"
Cohesion: 0.29
Nodes (3): add(), setFromCenterAndSize(), setLength()

### Community 60 - "_deactivateAction"
Cohesion: 0.25
Nodes (10): _deactivateAction(), _isActiveAction(), _removeInactiveAction(), _removeInactiveBinding(), _removeInactiveBindingsForAction(), _takeBackAction(), _takeBackBinding(), uncacheAction() (+2 more)

### Community 62 - "U"
Cohesion: 0.22
Nodes (3): Be, la(), U()

### Community 63 - "dc"
Cohesion: 0.22
Nodes (4): dc(), kl, _l, yc()

### Community 64 - "Panjat Sengsara"
Cohesion: 0.22
Nodes (8): Aturan main, Butuh, Cek, Install, Jalanin (.exe), Jalanin (manual), Masalah umum, Panjat Sengsara

### Community 67 - "getX"
Cohesion: 0.47
Nodes (5): getW(), getX(), getY(), getZ(), gi()

### Community 76 - ".setHSL"
Cohesion: 0.33
Nodes (3): ae(), oi(), se()

## Knowledge Gaps
- **10 isolated node(s):** `noop`, `els`, `src`, `Butuh`, `Install` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 507 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **53 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `pe` connect `pe` to `three.min.js`, `je`, `n`, `.constructor`, `.render`, `ui`, `gc`, `ie`, `Pi`, `updateMatrixWorld`, `.setAttribute`, `.subVectors`, `constructor`, `rh`, `un`, `.multiplyScalar`, `.constructor`, `ol`, `.dot`, `s`, `nl`, `fr`, `getX`, `.constructor`, `Cl`, `.normalize`, `.parse`, `Ul`, `gl`, `vc`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `copy()` connect `copy` to `three.min.js`, `applyMatrix4`, `xn`, `ve`, `je`, `Ga`, `.constructor`, `update`, `me`, `.render`, `ui`, `gc`, `li`, `ie`, `Pi`, `Hr`, `.constructor`, `updateMatrixWorld`, `.setAttribute`, `.subVectors`, `rr`, `rh`, `sa`, `un`, `.multiplyScalar`, `.constructor`, `Ho`, `yn`, `so`, `ol`, `.fromJSON`, `clone`, `dr`, `.dot`, `al`, `toJSON`, `s`, `nl`, `fr`, `fl`, `add`, `U`, `dc`, `ah`, `eo`, `no`, `.constructor`, `cc`, `ch`, `Cl`, `Ll`, `.setHSL`, `zl`, `Ul`, `dl`, `gl`, `Jo`, `vc`, `bh`, `clampPoint`, `ir`, `sh`, `Hl`, `Ki`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `ke` connect `ke` to `three.min.js`, `applyMatrix4`, `je`, `n`, `.constructor`, `me`, `Pi`, `Hr`, `.constructor`, `updateMatrixWorld`, `.setAttribute`, `.subVectors`, `constructor`, `copy`, `rh`, `un`, `.multiplyScalar`, `.constructor`, `.fromBufferAttribute`, `.dot`, `toJSON`, `s`, `nl`, `getX`, `.constructor`, `.normalize`, `.parse`, `.copy`, `clampPoint`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **What connects `noop`, `els`, `src` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `three.min.js` be split into smaller, more focused modules?**
  _Cohesion score 0.03682057276446522 - nodes in this community are weakly interconnected._
- **Should `applyMatrix4` be split into smaller, more focused modules?**
  _Cohesion score 0.05194805194805195 - nodes in this community are weakly interconnected._
- **Should `xn` be split into smaller, more focused modules?**
  _Cohesion score 0.04915824915824916 - nodes in this community are weakly interconnected._