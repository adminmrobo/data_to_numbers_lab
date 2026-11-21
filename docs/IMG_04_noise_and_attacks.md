# 이미지 제작 명세서 — 4장 고급 (04_noise_and_attacks.html)

그림체(공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_04_noise_and_attacks.md`와 같습니다.

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_ch4 | L | 1600×900 | 새로 그림 | 4장 `#cover` |
| og_ch4 | — | 1200×630 | cover_ch4에서 자름 | og:image |
| cm4_1 ~ cm4_4 | E | 1200×800 | 새로 그림 (지금은 캐릭터 팩 + SVG 배경) | 4컷 만화 ④ |
| 캐릭터 표정 | — | 96·192px | 캐릭터 팩 재사용 — 시아(안내·설명·뿌듯·신호), 모아(차·응원), X1(기본), X2(기본·당황), X3(기본·뿌듯·충격) | 확인 상자·쉬어 가기·⑨ 영상·관중석 |

## 4컷 만화 ④ 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, empty space in the upper third.*

- **cm4_1** — 주판봇이 오른쪽에서 반짝이는 트로피 모양 모니터를 들고 자랑한다.
- **cm4_2** — 조수가 왼쪽에서 점 몇 개가 찍힌 그림을 들고 놀라고, 오른쪽 작은 주판봇이 땀을 흘린다.
- **cm4_3** — 가운데 초파리 연구원이 그림 위 점들이 한 방향으로 줄지어 있는 것을 돋보기로 가리킨다.
- **cm4_4** — 박사가 왼쪽에서 화이트보드를 가리킨다. 보드 왼쪽에는 제멋대로 흩어진 점, 오른쪽에는 한 방향 화살표가 그려져 있다(글자 없음).

## 반영

`build_character_pack.py --ingest ./받은그림 --plates cover_ch4=L,cm4_1=E,cm4_2=E,cm4_3=E,cm4_4=E --out received_ch4`
