# 이미지 제작 명세서 — 3장 중급 (03_same_despite_looks.html)

그림체(공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_03_same_despite_looks.md`와 같습니다.

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_ch3 | L | 1600×900 | 새로 그림 | 3장 `#cover` |
| og_ch3 | — | 1200×630 | cover_ch3에서 자름 | og:image |
| cm3_1 ~ cm3_4 | E | 1200×800 | 새로 그림 (지금은 캐릭터 팩 + SVG 배경) | 4컷 만화 ③ |
| 캐릭터 표정 | — | 96·192px | 캐릭터 팩 재사용 — 시아(안내·설명·뿌듯·신호), 모아(차·응원), X1(기본·놀람), X2(기본·생각), X3(기본) | 확인 상자·쉬어 가기·⑦⑧ 무대·관중석 |

## 4컷 만화 ③ 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, empty space in the upper third.*

- **cm3_1** — 주판봇이 오른쪽에서 똑같은 빨간 사과 사진 더미를 복사기 옆에 쌓고 신나게 웃는다.
- **cm3_2** — 조수가 왼쪽에서 초록 사과를 내밀고, 오른쪽 작은 주판봇이 화면에 땀방울을 띄운다.
- **cm3_3** — 가운데 초파리 연구원이 같은 사과를 여러 색으로 칠한 그림 네 장을 펼쳐 보인다.
- **cm3_4** — 박사가 왼쪽에서 화이트보드를 가리킨다. 보드에는 색이 다른 사과 점들이 한 원 안에 모여 있다(글자 없음).

## 반영

`build_character_pack.py --ingest ./받은그림 --plates cover_ch3=L,cm3_1=E,cm3_2=E,cm3_3=E,cm3_4=E --out received_ch3`
