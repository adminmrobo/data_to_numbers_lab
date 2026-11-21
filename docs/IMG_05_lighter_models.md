# 이미지 제작 명세서 — 5장 특별 (05_lighter_models.html)

그림체(공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_05_lighter_models.md`와 같습니다.

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_ch5 | L | 1600×900 | 새로 그림 | 5장 `#cover` |
| og_ch5 | — | 1200×630 | cover_ch5에서 자름 | og:image |
| cm5_1 ~ cm5_4 | E | 1200×800 | 새로 그림 (지금은 캐릭터 팩 + SVG 배경) | 4컷 만화 ⑤ |
| 캐릭터 표정 | — | 96·192px | 캐릭터 팩 재사용 — 시아(안내·설명·뿌듯·신호), 모아(차·응원), X1(기본·놀람), X2(기본), X3(기본·뿌듯) | 확인 상자·쉬어 가기·⑦ 기기·관중석 |

## 4컷 만화 ⑤ 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, empty space in the upper third.*

- **cm5_1** — 주판봇이 오른쪽에서 커다란 상자를 톱으로 반 자르려 한다.
- **cm5_2** — 조수가 왼쪽에서 반으로 잘린 상자에서 쏟아진 중요한 물건들을 보고 놀라고, 오른쪽 작은 주판봇이 땀을 흘린다.
- **cm5_3** — 가운데 초파리 연구원이 안 쓰는 물건을 버리고 옷을 압축 팩에 넣는다.
- **cm5_4** — 박사가 왼쪽에서 화이트보드를 가리킨다. 보드에는 큰 상자가 세 단계 화살표를 거쳐 작은 상자가 되는 그림(글자 없음).

## 반영

`build_character_pack.py --ingest ./받은그림 --plates cover_ch5=L,cm5_1=E,cm5_2=E,cm5_3=E,cm5_4=E --out received_ch5`
