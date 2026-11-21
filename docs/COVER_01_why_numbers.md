# 표지 지시문 — 1장 도입: 사진도, 목소리도, 결국 숫자다

- 판: L (글 표지) · 1600×900 · 16:9 · 파일 이름 `cover_ch1.webp` (페이지 `#cover`의 `data-img="cover_ch1"` 자리)
- 그림체: **16비트 RPG 픽셀아트**, 굵은 어두운 외곽선(#1d1a22 계열), 명암 2~3단계, 낮의 연구실(흰 벽·큰 창의 자연광)
- 그림 안에 글자·숫자·로고 넣지 않음 (숫자 줄은 "숫자처럼 보이는 픽셀 블록"으로만 표현, 제목은 페이지가 HTML로 얹음)
- 참고 그림으로 함께 올릴 것: 캐릭터 저장소 `fruitfly-lab-expressions`의 박사·조수·초파리 3면도(k02~k04), 주판봇 v2 기본 표정(E13), 네 식구 단체 사진

## Genspark 등에 붙여 넣는 한국어 지시

16:9 가로 표지, 16비트 RPG 픽셀아트. 햇빛이 드는 하얀 연구실. 화면 오른쪽 절반에 커다란 투명 깔때기 장치가 있다. 깔때기 위쪽 입구로 네 가지가 빨려 들어간다: 빨간 사과 사진 액자, 파란 소리 파형 띠, 필름 조각(영상), 말풍선 모양 글 조각. 깔때기 안에서 이것들이 작은 색 사각형 블록(픽셀 블록) 줄로 잘게 바뀌어 흘러내리고, 깔때기 아래 출구에서는 반짝이는 초록 구슬 하나만 나온다. 화면 왼쪽 절반에 연구실 식구 넷이 나란히 서 있다: 박사(얇은 청록 테 사각 안경, 검은 머리에 흰 브릿지 한 줄, 짧은 꽁지머리, 흰 가운 안 검은 조끼와 넥타이)가 깔때기를 손바닥으로 가리키며 웃고, 조수(긴 분홍 머리에 둥근 번 두 개, 남색 브릿지, 연보라 후드티 위 흰 가운, 청바지)가 클립보드를 들고 흘러내리는 블록을 세고, 주판봇(베이지 상자형 CRT 몸체, 짙은 초록 화면에 민트 픽셀 눈, 주판알 달린 안테나, 무한궤도)이 주판을 들고 신나서 깔때기 입구를 올려다보고, 초파리 연구원(검은 몸, 빨간 겹눈, 금줄 파란 헬멧, 흰 가운 안 검은 조끼, 검은 장갑, 투명한 날개)이 돋보기로 출구의 초록 구슬을 의심스럽게 들여다본다. 키 비율은 박사 1.00, 조수 0.90, 주판봇 0.72, 초파리 0.41. 왼쪽 위에는 제목을 얹을 빈 벽 공간을 남긴다. 글자, 숫자, 로고, 어두운 밤 분위기, 네온은 넣지 않는다.

## English prompt

16:9 wide cover, 16-bit RPG pixel art, bold dark outlines, 2–3 tone shading. A bright daytime laboratory with white walls and large sunlit windows. On the right half, a large transparent funnel machine. Four things are being drawn into its wide top opening: a framed photo of a red apple, a blue sound-wave ribbon, a strip of film frames, and a speech-bubble shaped text scrap. Inside the funnel they break apart into rows of tiny colored square pixel blocks flowing downward, and from the narrow bottom outlet only one single glowing green orb comes out. On the left half, four characters stand in a row: a chibi scientist with thin teal square glasses, black hair with one white streak and a short ponytail, white lab coat over black vest and tie, smiling and gesturing at the funnel with an open palm; a young researcher with long pink hair in two round buns with navy streaks, lavender hoodie under a white lab coat, jeans, holding a clipboard and counting the falling blocks; a beige boxy CRT robot with a dark green screen face and mint pixel eyes, an antenna tipped with abacus beads, crawler treads, holding a wooden abacus and looking up excitedly at the funnel opening; a small anthropomorphic fruit fly researcher with black body, red compound eyes, blue helmet with gold stripe, white coat over black vest, black gloves, transparent wings, peering skeptically at the green orb through a magnifying glass. Height ratio scientist 1.00, researcher 0.90, robot 0.72, fruit fly 0.41. Leave empty wall space at upper left for a title. No text, no numbers, no letters, no logos, no night scene, no neon.

## 받은 뒤

1. `build_character_pack.py --ingest ./받은그림 --plates cover_ch1=L --out received_ch1`
2. 나온 base64 문자열을 `work/cover_ch1.b64`로 두고 다시 빌드하면 대체 표지가 그림으로 바뀝니다 (또는 `Object.assign(SPRITE,{cover_ch1:…})` 조각을 첫 스크립트 블록 끝에 붙입니다).
3. 공유 미리보기 `img/og_ch1.jpg`는 같은 그림을 1200×630으로 잘라 둡니다.
