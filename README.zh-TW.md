# Intent-first Cognitive Harness

[English](README.md)

## 只要說出你要處理的事，不必先學會一套框架

你可以直接說：

> 我有三種整理研究筆記的方法，一直改來改去。請幫我決定下個月先做什麼。

這個 Skill 的文件化流程會先整理你想完成的結果，再判斷是否需要追問。它設計上會補出適合的對象、交付形式、範圍、限制與證據需求；只有缺少的資訊可能改變方向時，才用白話問你一個小問題。接著選一條足夠用的分析路徑，讓結果更接近可以採取行動的形式。

你不需要先知道 Minerva HC 的名稱，也不需要填 route、風險等級或 JSON。這些是 Skill 內部用來整理思考的資料，不是使用者的入場券。

## 裝好之後會發生什麼

安裝的是一個 `SKILL.md`，不是新的模型、聊天 App 或背景服務。Host 讀到這個 Skill 後，使用流程會是：

1. 你照平常的方式提出問題。
2. 文件化流程先判斷這是可以直接處理的工作，還是需要理解目標的問題。
3. 翻譯、格式整理等明確而低風險的請求直接完成，不增加框架儀式。
4. 研究、比較、決策、診斷、規劃或溝通問題，依文件化流程先整理目標與預期結果。
5. 流程要求優先使用檔案、工具或公開來源；只有你才知道、而且會改變答案的資料才列為使用者問題。
6. 輸出契約要求把事實、假設、未知、推測與建議分開；必要時留下下一次複查的條件。

如果 Host 支援 ambient Skill，這個入口可以先檢查每一個請求，再選擇直接通過或進入分析。這不等於每一題都會啟動完整流程；刻意保留「簡單工作直接做」這條路，正是降低使用負擔的一部分。若 Host 不支援自動載入，你仍可直接指定這個 Skill，或依 Host 的方式載入它。

## 你會怎麼使用

安裝並重新開啟 Agent session 後，直接用自然語言描述事情即可：

```text
請比較這三個工具。我們是五人的小團隊，三個月內不能再搬遷，請把成本、學習時間與長期風險分開。

這個流程偶爾會跳過澄清。請找出可能的失效邊界，並給我一個可以重跑的測試方案。

我要把這個研究結果交給非技術讀者，請先判斷他們需要知道什麼，再幫我改寫。

請把這段文字翻成繁體中文，人名保持原樣。
```

依文件化政策，前幾個請求預期進入意圖整理；最後一個請求若資料明確，通常可直接翻譯。這是設計行為，不是跨 Host 的語義效果保證。你不需要說「請使用 HC」或指定任何內部能力。

## 它怎麼替你補足需求

文件化流程會形成一份簡短的工作簡報，確認幾個會影響結果的問題：

- 你想完成什麼，而不只是想知道什麼？
- 結果要給誰使用？
- 你需要答案、決策、計畫、研究紀錄，還是可以直接送出的文字？
- 有哪些期限、預算、權限、風險或格式限制？
- 哪些資料可以查到，哪些只有你知道？

剩下的小缺口若可撤回，就先做一個標明的假設；真正會改變範圍、受眾、安全性或建議的缺口，才會問你。一般情況預設不提問，必要時以一至三題為上限；Host 沒有原生選單時，會用簡短的 A／B／C 選項協助你回答。

## Minerva HC 在這裡是什麼

這裡的 HC 是 Minerva 公開教育脈絡中 Habits of Mind 與 Foundational Concepts 的簡稱。它們可以理解成一組反覆使用的思考習慣：先把問題說清楚、檢查證據、拆解因果、比較替代方案、看見受眾與限制，再決定下一步。重點不在於背誦一張清單，而在於針對眼前的問題選出少數真正有用的檢查角度。

本專案把這一層放在 Skill 內部。一般使用者只需說自己的問題，文件化流程再把適合的思考角度轉成研究問題、使用者問題、反例與可檢查的產出。它不要求你先選 HC，也不把所有 HC 一次套上去。

專案的起點也受到李佳達在公開訪談與課程內容中談到的問題定義、思考習慣與 AI 協作方式啟發。例如可參考 [李佳達的公開訪談](https://www.youtube.com/watch?v=0eFbBsE9Vlk)。這是獨立的開源實作，與李佳達、Minerva University 或 Minerva Project 沒有合作、隸屬、授權或背書關係；本專案不重製課程內容，也不宣稱官方相容。

研究目前只對特定歷史出版物做出窄化判定：2020 年 IDB／Minerva 出版物的 Appendix I 記錄為該出版物範圍內的 79 項快照。這不是現行官方 taxonomy，也不能推出「完整官方 78 項」。英文／西文版本的圖像與文字資產等值性仍未完成核對。可參考 [IDB 出版物](https://publications.iadb.org/publications/spanish/document/Como-preparan-los-innovadores-disruptivos-a-los-estudiantes-de-hoy-para-ser-la-fuerza-laboral-del-manana-El-modelo-cooperativo-de-Minerva-Un-camino-para-cerrar-la-brecha-de-habilidades.pdf)。

目前專案已逐項保存這份已驗證出版物快照的 79 個項目，並把它們放進具版本的 capability model。可執行覆蓋按不同的認知能力計算，不強迫每個歷史標籤各自變成一張 executable card。這是研究與工程上的邊界說明，不代表現行官方 Minerva taxonomy 已經完整。

## 這些思考工具不是黑箱

目前 stable capability set 的每個 project-derived card，都把「什麼時候使用、需要哪些資料、要做哪些步驟、產出什麼可檢查的結果、可能在哪裡失效、如何批評與評分」寫成可回查規格。21 / 21 張卡已達本專案定義的 project official-grade executable quality；這代表工程與教學契約完整，不代表 Minerva 官方 authored、current taxonomy、語義 runtime、真人驗證或 production-ready。

對一般使用者來說，這些欄位不需要自己填。你只要說明遇到的事情，入口會先判斷能不能直接處理，再把真正有用的思考角度轉成簡短問題、資料查找與可檢查的產出。Minerva HC 是內部參考脈絡；程序、artifact、critic 與 rubric 是本專案自行建立，來源與衍生部分分開標示。

## 安裝：目前最短的可用路徑

這個版本沒有 npm 套件，也沒有假裝存在的 `npm install` 指令。Agent Skill 的載入位置由 Host 決定；最穩妥的做法是從 GitHub 下載本 repository，將完整 Skill 目錄放進 Host 能讀取的 Skill registry。

在支援 `.agents/skills/` 的 workspace 中：

```bash
git clone https://github.com/atonnyshen/intent-first-cognitive-harness.git
mkdir -p .agents/skills/intent-first-cognitive-harness
cp intent-first-cognitive-harness/SKILL.md \
  .agents/skills/intent-first-cognitive-harness/SKILL.md
```

若你是從 GitHub 下載 ZIP，將 `intent-first-cognitive-harness` 換成解壓縮後的資料夾即可。若 Host 另有原生 Skill 目錄，請將同一個資料夾放到該位置：

| Host | 安裝判準 | 本版狀態 |
|---|---|---|
| Codex | 放入 Host 支援的 `.agents/skills/` 或使用者 Skill 目錄 | 已有公開契約；尚無跨版本語義保證 |
| Claude Code | 放入 Host 支援的 `.claude/skills/` | 已有公開契約；尚無跨版本語義保證 |
| Antigravity／AGY | 放入工作區支援的 Skill 目錄，通常優先檢查 `.agents/skills/` | 有限 AGY 執行證據；不等於自動觸發已驗收 |
| Gemini CLI／OpenCode | 依各自現行 Skill discovery 規則放置 | 本版本尚未完成原生 Host 驗收 |
| 其他 Agent Host | 只要能載入 `SKILL.md`，可使用文字 fallback | 需自行收集 Host receipt |

放好之後重新開啟 session，輸入：

```text
我有一個想解決的問題，但還不知道該怎麼拆。請先幫我說明你理解的目標；只有必要時再問我問題。
```

若 Host 找不到 Skill，通常是 discovery 位置或 session 快取問題，不是內容本身已經執行。請先檢查 Host 的 Skill 目錄與重新載入方式。

## 一般使用者會覺得簡單嗎

以「使用介面」來說，這一版已朝目標前進：公開契約讓使用者用自己的話開始，不必先學 HC；簡單請求有直接通過的路徑；澄清問題以結果與限制為主，而不是要求填內部欄位。這些是工程契約與設計目標，不是真人可用性結論。

以「安裝」來說，目前是「手動但短」：複製一個 `SKILL.md`、重新開啟 session，就能開始。它還不是一鍵安裝，也不是 `npm install` 後所有 Host 都會自動出現。要把這件事升級成真正的一鍵安裝，還需要穩定的 repository、Host 版本矩陣、安裝器與各 Host 的 native discovery 驗收。

以「自動觸發」來說，目前只能做範圍受限的承諾：在會把 Skill 當 ambient instruction 載入的 Host 上，它可以檢查每個請求；但 Markdown 本身不能替 Host 創造自動載入能力。現有測試已證明工程契約、路由與可觀察輸出，還沒有證明所有 Host 都能正確發現、選路、追問與恢復。

這是第一版公開預覽，所以我們選擇把已做到的事說清楚，也把尚未證明的部分留在原位。

## 目前狀態

| 層級 | 狀態 | 代表什麼 |
|---|---|---|
| Engineering contract | `PASS_FOR_SCOPE` | 契約、路由、驗證與可觀察輸出可重跑 |
| Semantic runtime | `FORMATIVE_ONLY / BLOCKED_EVIDENCE` | 有真實語言執行紀錄，但仍需更完整的語義評估 |
| Human preference | `NOT_RUN` | 沒有捏造真人評分或偏好票數 |
| Host-native | `BLOCKED` | 尚未完成主要 Host 的完整互動收據 |
| Production | `NO_SHIP` | 不宣稱 production-ready |

詳細範圍見 [公開範圍](docs/PUBLIC_SCOPE.md)、[來源與限制](docs/PROVENANCE_AND_LIMITATIONS.md) 與 [Host 相容性](docs/HOST_COMPATIBILITY.md)。這個 repository 刻意不放私人 prompt、未審核的網路問題語料、原始來源摘錄、真人資料或尚未解決的 HC cards。

## 授權與參與

公開樹中的專案自有檔案採 MIT License。MIT 不會重新授權第三方名稱、標誌、引文、課程內容、資料集或來源文件；詳見 [NOTICE.md](NOTICE.md)。

請先讀 [CONTRIBUTING.md](CONTRIBUTING.md)。如果你回報 Host 觸發問題，請提供 Host、版本、安裝位置、測試輸入、實際輸出與是否能恢復；不要貼入私人資料或機密 prompt。安全問題請依 [SECURITY.md](SECURITY.md) 處理，不要放在公開 issue。
