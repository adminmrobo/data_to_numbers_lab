# 이미지 제작 명세서 — 6장 체험 (06_hands_on.html)
> 생성 도구에 그대로 붙여 넣을 완성 프롬프트(표지·만화 컷 전부)와 만드는 순서는 `IMAGE_PROMPTS_ALL.md`, 첨부용 참고 그림·요청문은 `d2n_image_request_pack.zip`에 있습니다.

그림체(공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_06_hands_on.md`와 같습니다.

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_ch6 | L | 1600×900 | 새로 그림 | 6장 `#cover` |
| og_ch6 | — | 1200×630 | cover_ch6에서 자름 | og:image |
| cm6_1 ~ cm6_4 | E | 1200×800 | 새로 그림 (지금은 캐릭터 팩 + SVG 배경) | 4컷 만화 ⑥ |
| 캐릭터 표정 | — | 96·192px | 캐릭터 팩 재사용 — 시아(안내), 모아(차·응원), X1(기본·놀람) | 마무리 상자·장면 D·아웃트로 |

조작판 그래프·그리기판·성적표는 페이지가 직접 그리므로 그림이 필요 없습니다.

## 4컷 만화 ⑥ 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, empty space in the upper third.*

- **cm6_1** — 박사가 왼쪽에서 화이트보드를 가리킨다. 보드에는 작업대 네 개의 작은 그림(글자 없음).
- **cm6_2** — 주판봇이 오른쪽에서 두꺼운 답안 노트를 자랑스럽게 펼쳐 든다.
- **cm6_3** — 가운데 작은 초파리 연구원이 조작판 손잡이를 가리킨다.
- **cm6_4** — 왼쪽 조수가 클립보드를 들고 반짝이는 눈으로 보고하고, 오른쪽 작은 주판봇이 노트를 내려놓고 땀을 흘린다.

## 반영

`build_character_pack.py --ingest ./받은그림 --plates cover_ch6=L,cm6_1=E,cm6_2=E,cm6_3=E,cm6_4=E --out received_ch6`
