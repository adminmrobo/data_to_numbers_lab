# 이미지 제작 명세서 — 1장 도입 (01_why_numbers.html)
> 생성 도구에 그대로 붙여 넣을 완성 프롬프트(표지·만화 컷 전부)와 만드는 순서는 `IMAGE_PROMPTS_ALL.md`, 첨부용 참고 그림·요청문은 `d2n_image_request_pack.zip`에 있습니다.

그림체(모든 그림 공통): **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선, 명암 2~3단계, 낮의 연구실 흰 배경, 그림 안 글자·숫자·로고 없음. 캐릭터 외형·키 비율은 `COVER_01_why_numbers.md`와 같습니다.

## 그림 전체 목록

| 키 | 판 | 크기 | 상태 | 자리 |
|---|---|---|---|---|
| cover_index | L | 1600×900 | 새로 그림 (먼저) | index.html 표지 |
| cover_ch1 | L | 1600×900 | 새로 그림 | 1장 `#cover` |
| og_ch1 | — | 1200×630 | cover_ch1에서 자름 | og:image |
| cm1_1 ~ cm1_4 | E | 1200×800 (가로) → 컷 안에 맞춤 | 새로 그림 (지금은 캐릭터 팩 표정 그림 + SVG 배경) | 4컷 만화 ① |
| 캐릭터 표정 34종 | — | 96·192px | 캐릭터 팩 재사용 (fruitfly-lab-expressions @ 86d04ac) | 말풍선·등장인물·대결 |

## 만드는 순서

1. cover_index → 그림체 확인 2. cover_ch1 (cover_index를 참고 그림으로) 3. cm1_1~4 (한 요청에 네 장, 같은 비율)

## 4컷 만화 ① 프롬프트 (글자 없음, 말풍선은 HTML이 얹음)

공통 문장: *16-bit RPG pixel art panel, bright daytime white laboratory, bold dark outlines, no text, no letters, no numbers, no speech bubbles, leave empty space in the upper third for a speech bubble.*

- **cm1_1** — 주판봇(beige boxy CRT robot, abacus-bead antenna)이 오른쪽에서 반짝이는 빨간 사과를 들고 화면 쪽으로 자랑스럽게 내민다. 왼쪽은 비어 있다.
- **cm1_2** — 조수(pink twin-bun hair, lavender hoodie, white lab coat)가 왼쪽에서 모니터를 가리키고, 모니터에는 초록 픽셀 블록 줄이 빼곡하다(숫자처럼 보이는 블록, 실제 글자 아님). 오른쪽에 작게 주판봇이 놀라 눈이 커진다.
- **cm1_3** — 책상 위에 빨간 사과와 빨간 공이 나란히 있고, 초파리 연구원(small fruit fly researcher, blue helmet)이 가운데에서 돋보기로 둘을 번갈아 본다.
- **cm1_4** — 박사(teal square glasses, white streak hair, lab coat)가 왼쪽에서 화이트보드를 가리킨다. 보드에는 빨간 점 무리와 초록 점 무리가 화살표로 다시 정리되는 그림(글자 없음).

## 반영

받은 그림은 `build_character_pack.py --ingest ./받은그림 --plates cm1_1=E,cm1_2=E,cm1_3=E,cm1_4=E --out received_cm1`로 처리해 `SPRITE`에 넣으면, 만화 컷의 SVG 배경과 캐릭터 그림이 받은 그림으로 바뀝니다(말풍선은 그대로).
