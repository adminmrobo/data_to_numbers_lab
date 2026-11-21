# 이미지 제작 명세서 — 2장 초급 (02_rules_to_numbers.html)
> 생성 도구에 그대로 붙여 넣을 완성 프롬프트(표지·만화 컷 전부)와 만드는 순서는 `IMAGE_PROMPTS_ALL.md`, 첨부용 참고 그림·요청문은 `d2n_image_request_pack.zip`에 있습니다.

그림체(공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_02_rules_to_numbers.md`와 같습니다.

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_ch2 | L | 1600×900 | 새로 그림 | 2장 `#cover` |
| og_ch2 | — | 1200×630 | cover_ch2에서 자름 | og:image |
| cm2_1 ~ cm2_4 | E | 1200×800 | 새로 그림 (지금은 캐릭터 팩 + SVG 배경) | 4컷 만화 ② |
| 캐릭터 표정 | — | 96·192px | 캐릭터 팩 재사용 (@ 86d04ac) — 인턴 시아(안내·설명·뿌듯·신호), 모아(차·응원), 미공개 X1~X3(기본·생각) 포함 | 말풍선·확인 상자·쉬어 가기·관중석 |

## 4컷 만화 ② 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, empty space in the upper third.*

- **cm2_1** — 책상 위 빨간 사과를 주판봇이 오른쪽에서 가리키며 자신만만하게 웃는다.
- **cm2_2** — 조수가 왼쪽에서 초록 사과와 빨간 공을 양손에 들고 놀란 얼굴, 오른쪽 주판봇이 땀을 흘린다.
- **cm2_3** — 불이 반쯤 꺼진 책상 위에서 사과가 검붉게 보이고, 초파리 연구원이 가운데에서 돋보기로 본다.
- **cm2_4** — 박사가 왼쪽에서 화이트보드를 가리킨다. 보드에는 점 여러 개가 한 줄 선을 사이에 두고 뒤섞여 있다(글자 없음).

## 반영

`build_character_pack.py --ingest ./받은그림 --plates cover_ch2=L,cm2_1=E,cm2_2=E,cm2_3=E,cm2_4=E --out received_ch2`
