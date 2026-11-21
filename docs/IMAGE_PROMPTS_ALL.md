# 이미지 프롬프트 모음 — 모든 데이터는 숫자가 된다 (목차 + 1~5장)

모든 그림은 **16비트 RPG 픽셀아트**, 흰 배경의 낮 연구실, 그림 안 글자·숫자·로고 없음. 말풍선은 HTML이 얹으므로 만화 컷에는 그리지 않습니다.

## 그림 전체 목록

| 구분 | 수 | 할 일 |
|---|---|---|
| 새로 그림: 표지 | 6 | cover_index, cover_ch1~ch5 (16:9, 1600×900) |
| 새로 그림: 4컷 만화 | 20 | cm1_1 ~ cm5_4 (3:2, 1200×800) |
| 표지에서 자름 | 6 | og_index, og_ch1~ch5 (1200×630, 표지 가운데를 기준으로) |
| 캐릭터 팩 재사용 | — | 말풍선·등장인물·대결·인턴·X1~X3 표정 그림 (fruitfly-lab-expressions) |

## 만드는 순서 (요청 = 대화 하나)

1. **R1_style_check** — cover_index (16:9) · 먼저 이 한 장으로 그림체를 확인합니다. 마음에 들면 이 그림을 이후 모든 요청에 참고 그림으로 함께 올립니다.
2. **R2_covers_1to3** — cover_ch1, cover_ch2, cover_ch3 (16:9)
3. **R3_covers_4to5** — cover_ch4, cover_ch5 (16:9)
4. **R4_comic_ch1** — cm1_1, cm1_2, cm1_3, cm1_4 (3:2)
5. **R5_comic_ch2** — cm2_1, cm2_2, cm2_3, cm2_4 (3:2)
6. **R6_comic_ch3** — cm3_1, cm3_2, cm3_3, cm3_4 (3:2)
7. **R7_comic_ch4** — cm4_1, cm4_2, cm4_3, cm4_4 (3:2)
8. **R8_comic_ch5** — cm5_1, cm5_2, cm5_3, cm5_4 (3:2)

참고 그림: 요청마다 `refs/`의 캐릭터 기본 그림 4장을 함께 올립니다. R2부터는 R1에서 받은 cover_index도 함께 올립니다.

## R1_style_check (16:9)

### cover_index · 1600×900 · 저장 이름 `cover_index.png`
한국어 지시: `docs/COVER_00_index.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading. A bright sunlit white laboratory corridor with six doors in a row from left to right, each with a small picture sign (a folded map, a framed apple, three apples of different colors, a lightning-bolt static symbol, a shrinking box, a game joystick). A path of small colored pixel blocks runs along the floor connecting the doors. In front, the scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) points to the first door like a guide; the young researcher (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) holds an open map; the beige boxy CRT robot with abacus-bead antenna and crawler treads looks excitedly toward the joystick door; the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) holds a magnifying glass in front of the lightning door. Height ratio 1.00 / 0.90 / 0.72 / 0.41. Empty space at the top for a title. No text, no numbers, no letters, no logos, no night, no neon.
```

## R2_covers_1to3 (16:9)

### cover_ch1 · 1600×900 · 저장 이름 `cover_ch1.png`
한국어 지시: `docs/COVER_01_why_numbers.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading. A bright daytime laboratory with white walls and large sunlit windows. On the right half, a large transparent funnel machine. Four things are being drawn into its wide top opening: a framed photo of a red apple, a blue sound-wave ribbon, a strip of film frames, and a speech-bubble shaped text scrap. Inside the funnel they break apart into rows of tiny colored square pixel blocks flowing downward, and from the narrow bottom outlet only one single glowing green orb comes out. On the left half, four characters stand in a row: a chibi scientist with thin teal square glasses, black hair with one white streak and a short ponytail, white lab coat over black vest and tie, smiling and gesturing at the funnel with an open palm; a young researcher with long pink hair in two round buns with navy streaks, lavender hoodie under a white lab coat, jeans, holding a clipboard and counting the falling blocks; a beige boxy CRT robot with a dark green screen face and mint pixel eyes, an antenna tipped with abacus beads, crawler treads, holding a wooden abacus and looking up excitedly at the funnel opening; a small anthropomorphic fruit fly researcher with black body, red compound eyes, blue helmet with gold stripe, white coat over black vest, black gloves, transparent wings, peering skeptically at the green orb through a magnifying glass. Height ratio scientist 1.00, researcher 0.90, robot 0.72, fruit fly 0.41. Leave empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night scene, no neon.

## 받은 뒤

1. `build_character_pack.py --ingest ./받은그림 --plates cover_ch1=L --out received_ch1`
2. 나온 base64 문자열을 `work/cover_ch1.b64`로 두고 다시 빌드하면 대체 표지가 그림으로 바뀝니다 (또는 `Object.assign(SPRITE,{cover_ch1:…})` 조각을 첫 스크립트 블록 끝에 붙입니다).
3. 공유 미리보기 `img/og_ch1.jpg`는 같은 그림을 1200×630으로 잘라 둡니다.
```

### cover_ch2 · 1600×900 · 저장 이름 `cover_ch2.png`
한국어 지시: `docs/COVER_02_rules_to_numbers.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading. A bright sunlit white laboratory; on the back wall four small bank-teller style counters arranged 2×2. Counter one takes in a framed red apple photo and outputs three rows of red, green and blue blocks; counter two takes in a strip of film and outputs a neat stack of thin layered plates; counter three takes in a speech-bubble shaped text scrap and outputs a line of small capsule-shaped pieces; counter four takes in a blue sound-wave ribbon and outputs a grid of square blocks of varying brightness. In front: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) guiding with an open palm; the young researcher (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) noting block counts on a clipboard; the beige boxy CRT robot (dark green screen face, mint pixel eyes, abacus-bead antenna, crawler treads) proudly holding up a blank signboard; the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) inspecting a shadowed, darkened apple with a magnifying glass. Height ratio 1.00 / 0.90 / 0.72 / 0.41. Empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night, no neon.
```

### cover_ch3 · 1600×900 · 저장 이름 `cover_ch3.png`
한국어 지시: `docs/COVER_03_same_despite_looks.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory. Upper right: a floating dashed circle holding four apples of different colors (red, green, yellow, blue) clustered closely together, all with the same brown stem. Lower right: a low stage where three black silhouettes of different heights (medium, short, tall) all raise their right hand and wave in exactly the same pose; on the floor beneath them three thin stick-figure joint shadows overlap into one. Lower left: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) pointing an open palm at the apple cluster; the young researcher (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) measuring the distance between apples with a tape measure; the beige boxy CRT robot (dark green screen face, mint pixel eyes, abacus-bead antenna, crawler treads) proudly hugging a stack of identical red-apple photos; the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) holding a yellow apple and tilting its head. Height ratio 1.00 / 0.90 / 0.72 / 0.41. Empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night, no neon.
```

## R3_covers_4to5 (16:9)

### cover_ch4 · 1600×900 · 저장 이름 `cover_ch4.png`
한국어 지시: `docs/COVER_04_noise_and_attacks.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory. Upper right: a wall monitor filled with black-and-white static where a faint green horizontal bar is barely visible. Lower right: an easel holding a red apple painting overlaid with very faint, regularly spaced reddish dots (visible only on close inspection); the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) inspects the dots with a magnifying glass. Lower left: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) pointing at the monitor; the young researcher (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) holding a clipboard with a surprised face; the beige boxy CRT robot (dark green screen face, mint pixel eyes, abacus-bead antenna, crawler treads) tilting its head with a sweat drop on its screen. Height ratio 1.00 / 0.90 / 0.72 / 0.41. Empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night, no neon.
```

### cover_ch5 · 1600×900 · 저장 이름 `cover_ch5.png`
한국어 지시: `docs/COVER_05_lighter_models.md` 참고

```
16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory. On the right, a 3×3 stack of grey blocks is compressed along an arrow into one small green block that slides into a smartphone screen. Next to the compressor, the young researcher (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) weighs blocks on a scale, and the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) trims thin twigs off the block stack with tiny scissors. Lower left: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) gesturing at the phone with an open palm; the beige boxy CRT robot (dark green screen face, mint pixel eyes, abacus-bead antenna, crawler treads) hesitating with a saw halfway into a big block. Height ratio 1.00 / 0.90 / 0.72 / 0.41. Empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night, no neon.
```

## R4_comic_ch1 (3:2)

### cm1_1 · 1200×800 · 저장 이름 `cm1_1.png`
- 등장: 주판봇(오른쪽) · 이 컷의 말풍선(HTML): "AI야, 이 빨간 사과 보여? 맛있어 보이지?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: an open laboratory floor with tidy shelves. Characters: the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) on the right, grinning proudly with sparkling eyes. The robot holds out a shiny red apple toward the viewer. The left half of the panel is empty. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm1_2 · 1200×800 · 저장 이름 `cm1_2.png`
- 등장: 조수(하루)(왼쪽), 주판봇(오른쪽 작게) · 이 컷의 말풍선(HTML): "AI한테는 "255, 31, 28…" 숫자 15만 개로 보여요."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a large wall monitor. Characters: the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) on the left, holding a clipboard and reporting earnestly; the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) small on the right, eyes wide open in amazement. Haru points at a monitor filled with neat rows of green pixel blocks that look like data (no readable digits). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm1_3 · 1200×800 · 저장 이름 `cm1_3.png`
- 등장: 초파리 연구원(가운데 작게) · 이 컷의 말풍선(HTML): "그럼 빨간 공도 거의 같은 숫자겠네?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) small in the center, peering through a magnifying glass. A red apple and a red ball sit side by side on the desk; the fruit fly compares them. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm1_4 · 1200×800 · 저장 이름 `cm1_4.png`
- 등장: 박사(왼쪽) · 이 컷의 말풍선(HTML): "그래서 숫자를 "뜻 있는 숫자"로 다듬는 법을 배울 거예요."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a whiteboard. Characters: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) on the left, pointing at a whiteboard like a kind teacher. The whiteboard shows a red dot cluster and a green dot cluster being rearranged by arrows (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

## R5_comic_ch2 (3:2)

### cm2_1 · 1200×800 · 저장 이름 `cm2_1.png`
- 등장: 주판봇(오른쪽) · 이 컷의 말풍선(HTML): "규칙 하나면 끝! "빨간 건 사과다.""

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) on the right, grinning proudly with sparkling eyes. The robot proudly holds up a single red apple as if it were a rule card (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm2_2 · 1200×800 · 저장 이름 `cm2_2.png`
- 등장: 조수(하루)(왼쪽), 주판봇(오른쪽 작게) · 이 컷의 말풍선(HTML): "이 초록 사과는요? 그리고 빨간 공은요?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) on the left, shocked, mouth open, hands raised; the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) small on the right, with a big sweat drop, sheepish and deflated. Haru holds up a green apple in one hand and a red ball in the other. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm2_3 · 1200×800 · 저장 이름 `cm2_3.png`
- 등장: 초파리 연구원(가운데 작게) · 이 컷의 말풍선(HTML): "불 끄면 빨간색도 까매지는데?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: an open laboratory floor with tidy shelves. Characters: the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) small in the center, peering through a magnifying glass. The room lights are dimmed on one side; the fruit fly examines a red apple that looks almost black in the shadow. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm2_4 · 1200×800 · 저장 이름 `cm2_4.png`
- 등장: 박사(왼쪽) · 이 컷의 말풍선(HTML): "그래서 규칙이 어디까지 되는지부터 재 봐요."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a whiteboard. Characters: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) on the left, pointing at a whiteboard like a kind teacher. The whiteboard shows a simple bar gauge rising and stopping at a dashed line (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

## R6_comic_ch3 (3:2)

### cm3_1 · 1200×800 · 저장 이름 `cm3_1.png`
- 등장: 주판봇(오른쪽) · 이 컷의 말풍선(HTML): "빨간 사과 사진을 백 장 복사했어! 이제 사과는 완벽하게 알아보겠지?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a large wall monitor. Characters: the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) on the right, grinning proudly with sparkling eyes. The robot stands beside a tall stack of identical red-apple photos coming out of a copier. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm3_2 · 1200×800 · 저장 이름 `cm3_2.png`
- 등장: 조수(하루)(왼쪽), 주판봇(오른쪽 작게) · 이 컷의 말풍선(HTML): "이 초록 사과는요?"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) on the left, holding a clipboard and reporting earnestly; the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) small on the right, with a big sweat drop, sheepish and deflated. Haru holds out a green apple; the small robot looks at it with a sweat drop. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm3_3 · 1200×800 · 저장 이름 `cm3_3.png`
- 등장: 초파리 연구원(가운데 작게) · 이 컷의 말풍선(HTML): "같은 걸 백 번 봐도 배우는 건 한 가지야. 색을 바꿔서 보여 줘."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: an open laboratory floor with tidy shelves. Characters: the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) small in the center, pointing firmly with one gloved hand, confident. The fruit fly fans out four cards showing the same apple painted red, green, yellow and blue. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm3_4 · 1200×800 · 저장 이름 `cm3_4.png`
- 등장: 박사(왼쪽) · 이 컷의 말풍선(HTML): "무엇이 달라도 되는지를 보여 주는 것, 그게 오늘 주제예요."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a whiteboard. Characters: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) on the left, pointing at a whiteboard like a kind teacher. The whiteboard shows apple dots of different colors gathered inside one circle (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

## R7_comic_ch4 (3:2)

### cm4_1 · 1200×800 · 저장 이름 `cm4_1.png`
- 등장: 주판봇(오른쪽) · 이 컷의 말풍선(HTML): "시험 정확도 98%! 이 판정기 바로 현장에 보내자!"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a large wall monitor. Characters: the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) on the right, grinning proudly with sparkling eyes. The robot holds up a glowing trophy-shaped monitor, very proud. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm4_2 · 1200×800 · 저장 이름 `cm4_2.png`
- 등장: 조수(하루)(왼쪽), 주판봇(오른쪽 작게) · 이 컷의 말풍선(HTML): "사진에 점 몇 개만 찍었는데… "가로줄"이 "세로줄"이 됐어요."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) on the left, shocked, mouth open, hands raised; the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) small on the right, with a big sweat drop, sheepish and deflated. Haru holds up a picture with a few small dots on it, shocked; the small robot sweats. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm4_3 · 1200×800 · 저장 이름 `cm4_3.png`
- 등장: 초파리 연구원(가운데 작게) · 이 컷의 말풍선(HTML): "점을 아무렇게나 찍은 게 아니야. 판정기가 제일 약한 방향으로 찍었지."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: an open laboratory floor with tidy shelves. Characters: the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) small in the center, pointing firmly with one gloved hand, confident. The fruit fly points with a magnifying glass at small dots on a picture that line up in one direction. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm4_4 · 1200×800 · 저장 이름 `cm4_4.png`
- 등장: 박사(왼쪽) · 이 컷의 말풍선(HTML): "우연한 잡음과 노린 잡음. 오늘은 둘을 나눠 봅시다."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a whiteboard. Characters: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) on the left, pointing at a whiteboard like a kind teacher. The whiteboard shows scattered random dots on the left and one bold arrow on the right (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

## R8_comic_ch5 (3:2)

### cm5_1 · 1200×800 · 저장 이름 `cm5_1.png`
- 등장: 주판봇(오른쪽) · 이 컷의 말풍선(HTML): "모델을 휴대폰에 넣으래. 큰 짐은 그냥 반으로 잘라서 넣으면 되지!"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a large wall monitor. Characters: the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) on the right, grinning proudly with sparkling eyes. The robot is about to saw a big cardboard moving box in half. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm5_2 · 1200×800 · 저장 이름 `cm5_2.png`
- 등장: 조수(하루)(왼쪽), 주판봇(오른쪽 작게) · 이 컷의 말풍선(HTML): "반으로 자른 쪽에 중요한 게 다 들어 있었는데요…"

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: at a wooden lab desk. Characters: the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans) on the left, shocked, mouth open, hands raised; the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads) small on the right, with a big sweat drop, sheepish and deflated. Haru stares at important items spilling out of a box sawn in half; the small robot sweats. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm5_3 · 1200×800 · 저장 이름 `cm5_3.png`
- 등장: 초파리 연구원(가운데 작게) · 이 컷의 말풍선(HTML): "이삿짐은 안 쓰는 것부터 버리고, 남은 건 차곡차곡 접어야지."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: an open laboratory floor with tidy shelves. Characters: the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings) small in the center, pointing firmly with one gloved hand, confident. The fruit fly tosses unused items aside and squeezes clothes into a vacuum storage bag. Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

### cm5_4 · 1200×800 · 저장 이름 `cm5_4.png`
- 등장: 박사(왼쪽) · 이 컷의 말풍선(HTML): "무엇을 버리고 어떻게 접을지, 오늘 하나씩 재 봅시다."

```
Comic panel, 3:2 landscape (1200×800), 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background. Setting: in front of a whiteboard. Characters: the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie) on the left, pointing at a whiteboard like a kind teacher. The whiteboard shows a big box turning into a small box through three arrows (no writing). Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.
```

## 표지에서 자르기 (생성하지 않음)

| 저장 이름 | 원본 | 크기 |
|---|---|---|
| og_index.jpg | cover_index.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |
| og_ch1.jpg | cover_ch1.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |
| og_ch2.jpg | cover_ch2.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |
| og_ch3.jpg | cover_ch3.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |
| og_ch4.jpg | cover_ch4.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |
| og_ch5.jpg | cover_ch5.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |

## 반영

받은 그림을 한 폴더에 모은 뒤:

```
python3 build_character_pack.py --ingest ./받은그림 \
  --plates cover_index=L,cover_ch1=L,cover_ch2=L,cover_ch3=L,cover_ch4=L,cover_ch5=L,cm1_1=E,cm1_2=E,cm1_3=E,cm1_4=E,cm2_1=E,cm2_2=E,cm2_3=E,cm2_4=E,cm3_1=E,cm3_2=E,cm3_3=E,cm3_4=E,cm4_1=E,cm4_2=E,cm4_3=E,cm4_4=E,cm5_1=E,cm5_2=E,cm5_3=E,cm5_4=E \
  --out received_all
```

표지는 1600×900 WebP, 만화 컷은 1200×800 WebP로 줄여 각 페이지에 넣습니다(한 편 600KB 이하).
