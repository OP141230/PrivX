import gzip
import brotli

with open('searxng/sxng-base.min.css', 'r', encoding='utf-8') as f:
    base_css = f.read()

terminal_css = '''
/* ==========================================================================
   PrivX Terminal / Hacker CRT Theme
   ========================================================================== */

:root {
  --term-bg: #0a0d0a;
  --term-bright: #8fe89a;
  --term-dim: #4f8a58;
  --term-muted: #76b380;
  --term-dark-green: #1f3a24;
  --term-border: #2e5735;
  --term-mono: "SF Mono", Consolas, "Courier New", "Cascadia Code", "Fira Code", monospace;

  --color-base-font: #8fe89a;
  --color-base-font-rgb: 143, 232, 154;
  --color-base-background: #0a0d0a;
  --color-base-background-mobile: #0a0d0a;
  --color-url-font: #4f8a58;
  --color-url-visited-font: #4f8a58;
  --color-header-background: #0a0d0a;
  --color-header-border: #2e5735;
  --color-footer-background: #0a0d0a;
  --color-footer-border: #2e5735;
  --color-sidebar-border: #2e5735;
  --color-sidebar-font: #8fe89a;
  --color-sidebar-background: #0a0d0a;
  --color-backtotop-font: #8fe89a;
  --color-backtotop-border: #2e5735;
  --color-backtotop-background: #0a0d0a;
  --color-btn-background: #4f8a58;
  --color-btn-font: #0a0d0a;
  --color-show-btn-background: #1f3a24;
  --color-show-btn-font: #8fe89a;
  --color-search-border: #4f8a58;
  --color-search-shadow: none;
  --color-search-background: #0a0d0a;
  --color-search-font: #8fe89a;
  --color-search-background-hover: #4f8a58;
  --color-error: #ff5555;
  --color-error-background: #1a0808;
  --color-warning: #ffb86c;
  --color-warning-background: #1a1508;
  --color-success: #8fe89a;
  --color-success-background: #0a1f0a;
  --color-categories-item-selected-font: #0a0d0a;
  --color-categories-item-border-selected: #4f8a58;
  --color-autocomplete-font: #8fe89a;
  --color-autocomplete-border: #4f8a58;
  --color-autocomplete-shadow: 0 8px 24px rgba(0, 0, 0, 0.85);
  --color-autocomplete-background: #0a0d0a;
  --color-autocomplete-background-hover: rgba(79, 138, 88, 0.25);
  --color-answer-font: #8fe89a;
  --color-answer-background: #0a0d0a;
  --color-result-background: transparent;
  --color-result-border: #1a2e1d;
  --color-result-url-font: #4f8a58;
  --color-result-vim-selected: rgba(79, 138, 88, 0.15);
  --color-result-vim-arrow: #8fe89a;
  --color-result-description-highlight-font: #8fe89a;
  --color-result-link-font: #8fe89a;
  --color-result-link-font-highlight: #a8ffb2;
  --color-result-link-visited-font: #8fe89a;
  --color-result-publishdate-font: #4f8a58;
  --color-settings-tr-hover: rgba(79, 138, 88, 0.15);
}

/* ==========================================================================
   Universal Reset & Overflow Protection
   ========================================================================== */

*, *::before, *::after {
  font-family: var(--term-mono) !important;
  box-sizing: border-box !important;
}

html, body {
  background-color: #0a0d0a !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  min-height: 100vh !important;
  margin: 0 !important;
  padding: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
}

/* Dense CRT Scanlines + Radial Vignette + Subtle Flicker */
body::before {
  content: "" !important;
  display: block !important;
  position: fixed !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background:
    repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.38) 0px,
      rgba(0, 0, 0, 0.38) 1px,
      transparent 1px,
      transparent 2px
    ),
    radial-gradient(
      ellipse at center,
      rgba(10, 13, 10, 0) 50%,
      rgba(5, 7, 5, 0.72) 100%
    ) !important;
  pointer-events: none !important;
  z-index: 99999 !important;
  animation: crt-flicker 0.15s infinite !important;
}

@keyframes crt-flicker {
  0% { opacity: 0.96; }
  50% { opacity: 1.0; }
  100% { opacity: 0.97; }
}

@keyframes blink-cursor {
  0%, 49% { opacity: 1; visibility: visible; }
  50%, 100% { opacity: 0; visibility: hidden; }
}

/* ==========================================================================
   Header & Top Navigation Badges
   ========================================================================== */

#links_on_top {
  display: flex !important;
  justify-content: flex-end !important;
  align-items: center !important;
  gap: 12px !important;
  padding: 16px 24px !important;
  position: relative !important;
  background: transparent !important;
  border-bottom: none !important;
  width: 100% !important;
  max-width: 100% !important;
}

#main_index, #main_results, #main_preferences, #main_stats, #main_about {
  position: relative !important;
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
}

#main_index::before, #main_results::before, #main_preferences::before, #main_stats::before, #main_about::before {
  content: "root@privx:~$" !important;
  position: absolute !important;
  top: 16px !important;
  left: 24px !important;
  display: inline-block !important;
  border: 1px solid #4f8a58 !important;
  padding: 4px 12px !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.85rem !important;
  background: rgba(10, 15, 10, 0.85) !important;
  border-radius: 0 !important;
  z-index: 100 !important;
}

#links_on_top a {
  display: inline-flex !important;
  align-items: center !important;
  border: 1px solid #4f8a58 !important;
  padding: 4px 12px !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.85rem !important;
  text-decoration: none !important;
  background: rgba(10, 15, 10, 0.85) !important;
  border-radius: 0 !important;
  transition: all 0.2s ease !important;
}

#links_on_top a:hover {
  border-color: #8fe89a !important;
  color: #8fe89a !important;
  background: rgba(79, 138, 88, 0.15) !important;
}

#links_on_top a svg {
  display: none !important;
}

#links_on_top .link_on_top_about span {
  font-size: 0 !important;
}
#links_on_top .link_on_top_about span::before {
  content: "man privx" !important;
  font-size: 0.85rem !important;
}

#links_on_top .link_on_top_preferences span {
  font-size: 0 !important;
}
#links_on_top .link_on_top_preferences span::before {
  content: "settings" !important;
  font-size: 0.85rem !important;
}

/* ==========================================================================
   Home / Index Page Logo: > PrivX_
   ========================================================================== */

.index .title, .title {
  background: none !important;
  background-image: none !important;
  min-height: auto !important;
  height: auto !important;
  margin: 3.5rem auto 1.5rem auto !important;
  text-align: center !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  visibility: visible !important;
  opacity: 1 !important;
  width: 100% !important;
}

.index .title h1, .title h1 {
  font-size: 0 !important;
  color: transparent !important;
  margin: 0 !important;
  padding: 0 !important;
  display: inline-flex !important;
  align-items: baseline !important;
  justify-content: center !important;
  line-height: 1 !important;
  height: auto !important;
  visibility: visible !important;
}

.index .title h1::before, .title h1::before {
  content: "> PrivX" !important;
  font-size: 4.2rem !important;
  font-weight: 800 !important;
  font-family: var(--term-mono) !important;
  color: #8fe89a !important;
  letter-spacing: -1px !important;
  text-shadow: 0 0 14px rgba(143, 232, 154, 0.55), 0 0 28px rgba(143, 232, 154, 0.25) !important;
  line-height: 1 !important;
  display: inline-block !important;
  visibility: visible !important;
}

.index .title h1::after, .title h1::after {
  content: "_" !important;
  font-size: 4.2rem !important;
  font-weight: 800 !important;
  font-family: var(--term-mono) !important;
  color: #8fe89a !important;
  letter-spacing: -1px !important;
  animation: blink-cursor 1.1s step-end infinite !important;
  text-shadow: 0 0 14px rgba(143, 232, 154, 0.55) !important;
  line-height: 1 !important;
  margin-left: 2px !important;
  display: inline-block !important;
  visibility: visible !important;
}

.index .title::after, .title::after {
  content: "// no logs. no tracking. no noise." !important;
  font-size: 0.95rem !important;
  font-weight: 500 !important;
  font-family: var(--term-mono) !important;
  color: #4f8a58 !important;
  letter-spacing: 0.5px !important;
  margin-top: 0.75rem !important;
  display: block !important;
  text-align: center !important;
  visibility: visible !important;
}

/* ==========================================================================
   Results Page Logo: > PrivX_
   ========================================================================== */

#search_logo {
  display: flex !important;
  align-items: baseline !important;
  justify-content: center !important;
  text-decoration: none !important;
  border: none !important;
  background: transparent !important;
  padding: 0 !important;
  margin: 1.5rem auto 0.75rem auto !important;
  height: auto !important;
  width: auto !important;
}

#search_logo svg, #search_logo img, #search_logo span {
  display: none !important;
}

#search_logo::before {
  content: "> PrivX" !important;
  font-size: 2.8rem !important;
  font-weight: 800 !important;
  font-family: var(--term-mono) !important;
  color: #8fe89a !important;
  letter-spacing: -1px !important;
  text-shadow: 0 0 12px rgba(143, 232, 154, 0.55) !important;
  line-height: 1 !important;
  display: inline-block !important;
}

#search_logo::after {
  content: "_" !important;
  font-size: 2.8rem !important;
  font-weight: 800 !important;
  font-family: var(--term-mono) !important;
  color: #8fe89a !important;
  animation: blink-cursor 1.1s step-end infinite !important;
  text-shadow: 0 0 12px rgba(143, 232, 154, 0.55) !important;
  line-height: 1 !important;
  margin-left: 2px !important;
  display: inline-block !important;
}

/* ==========================================================================
   Search Header & Search Box (Cleaned of Overlays and Lines)
   ========================================================================== */

#search_header, body.results_endpoint #search_header, .index #search_header {
  background: transparent !important;
  border: none !important;
  border-bottom: none !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  grid-template-columns: none !important;
  grid-template-areas: none !important;
  padding: 0 1rem !important;
  margin: 0 auto !important;
  width: 100% !important;
  max-width: 800px !important;
  box-sizing: border-box !important;
}

#search_view, #search_view:focus-within, body.results_endpoint #search_view {
  position: static !important;
  top: auto !important;
  left: auto !important;
  right: auto !important;
  bottom: auto !important;
  width: 100% !important;
  max-width: 660px !important;
  height: auto !important;
  background: transparent !important;
  z-index: 10 !important;
  padding: 0 !important;
  margin: 0 auto !important;
}

.search_box,
#search_view .search_box,
#search_view:focus-within .search_box,
#search_view:focus-within .search_box * {
  border-bottom: none !important;
  text-decoration: none !important;
}

.search_box, #search_view .search_box, #search_view:focus-within .search_box {
  display: flex !important;
  align-items: center !important;
  background: #0a0d0a !important;
  border: 1px solid #4f8a58 !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  padding: 0 14px !important;
  position: relative !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
  width: 100% !important;
  max-width: 660px !important;
  height: 48px !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
}

.search_box:focus-within,
#search_view:focus-within .search_box {
  border: 1px solid #8fe89a !important;
  box-shadow: 0 0 12px rgba(143, 232, 154, 0.25) !important;
}

.search_box::before {
  content: "query>" !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
  margin-right: 10px !important;
  white-space: nowrap !important;
  user-select: none !important;
  line-height: 1 !important;
}

#q, input[type="text"]#q, #search_view #q, #search_view:focus-within #q {
  background: transparent !important;
  border: none !important;
  border-bottom: none !important;
  box-shadow: none !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  font-size: 1.05rem !important;
  font-weight: 500 !important;
  caret-color: #8fe89a !important;
  padding: 10px 6px !important;
  outline: none !important;
  width: 100% !important;
  height: 100% !important;
  text-decoration: none !important;
}

#q::placeholder {
  color: #2b5030 !important;
  font-family: var(--term-mono) !important;
}

#send_search, #clear_search {
  background: transparent !important;
  border: none !important;
  color: #4f8a58 !important;
  cursor: pointer !important;
  padding: 4px 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: color 0.2s ease !important;
}

#send_search:hover, #clear_search:hover {
  color: #8fe89a !important;
}

#send_search svg, #clear_search svg {
  stroke: currentColor !important;
  fill: currentColor !important;
  width: 18px !important;
  height: 18px !important;
}

.autocomplete {
  background: #0a0d0a !important;
  border: 1px solid #4f8a58 !important;
  border-radius: 0 !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.9) !important;
}

.autocomplete li {
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  padding: 8px 14px !important;
}

.autocomplete li.selected, .autocomplete li:hover {
  background: rgba(79, 138, 88, 0.25) !important;
  color: #a8ffb2 !important;
}

/* Search Filters (languages, time, safesearch) */
.search_filters {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  gap: 12px !important;
  margin: 1rem auto 0 auto !important;
  width: 100% !important;
  max-width: 660px !important;
  padding: 0 !important;
  overflow-x: auto !important;
}

.search_filters select, .search_filters label {
  background: #0a0d0a !important;
  border: 1px solid #2e5735 !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.85rem !important;
  padding: 4px 10px !important;
  border-radius: 0 !important;
}

/* ==========================================================================
   Category Tabs
   ========================================================================== */

#categories, .search_categories {
  display: flex !important;
  justify-content: center !important;
  margin-top: 1.25rem !important;
  margin-bottom: 1.5rem !important;
  width: 100% !important;
  max-width: 800px !important;
}

#categories_container {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-wrap: wrap !important;
  gap: 0 !important;
  background: transparent !important;
  border: none !important;
}

.category {
  display: inline-flex !important;
  align-items: center !important;
  margin: 0 !important;
  padding: 0 !important;
  background: transparent !important;
  border: none !important;
  position: relative !important;
}

.category + .category {
  border-left: 1px solid #233e27 !important;
}

.category label, .category button, .category.category_button {
  background: transparent !important;
  border: none !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.9rem !important;
  padding: 6px 14px !important;
  cursor: pointer !important;
  text-decoration: none !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  transition: all 0.15s ease !important;
  border-radius: 0 !important;
}

.category svg {
  display: none !important;
}

.category:hover label, .category:hover button, .category:hover .category_name {
  color: #8fe89a !important;
}

.category input[type="checkbox"]:checked + label,
.category.selected,
.category_button.selected,
.category.selected .category_name {
  background: #4f8a58 !important;
  color: #0a0d0a !important;
  font-weight: 700 !important;
  border-radius: 0 !important;
}

.category input[type="checkbox"]:checked + label .category_name,
.category.selected .category_name {
  color: #0a0d0a !important;
}

/* ==========================================================================
   Search Results & Sidebar (Centered, No Overflow)
   ========================================================================== */

#results {
  display: flex !important;
  justify-content: center !important;
  gap: 2rem !important;
  max-width: 1100px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 1.5rem 1rem !important;
  box-sizing: border-box !important;
}

#urls {
  flex: 1 !important;
  max-width: 680px !important;
  min-width: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;
}

article.result {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  margin-bottom: 2.2rem !important;
  padding: 0 !important;
  display: flex !important;
  flex-direction: column !important;
}

article.result .favicon {
  display: none !important;
}

article.result h3 {
  order: 1 !important;
  margin: 0 0 4px 0 !important;
  font-size: 1.15rem !important;
  line-height: 1.4 !important;
  font-weight: 600 !important;
  font-family: var(--term-mono) !important;
}

article.result h3 a {
  color: #8fe89a !important;
  text-decoration: none !important;
  font-family: var(--term-mono) !important;
  transition: color 0.15s ease, text-shadow 0.15s ease !important;
}

article.result h3 a:hover {
  color: #b4ffbe !important;
  text-shadow: 0 0 8px rgba(143, 232, 154, 0.4) !important;
  text-decoration: underline !important;
}

article.result .url_header,
article.result .url_wrapper {
  order: 2 !important;
  color: #4f8a58 !important;
  font-size: 0.85rem !important;
  font-family: var(--term-mono) !important;
  text-decoration: none !important;
  margin-bottom: 6px !important;
  display: block !important;
  word-break: break-all !important;
}

article.result .url_wrapper span {
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
}

article.result .content {
  order: 3 !important;
  color: #76b380 !important;
  font-size: 0.95rem !important;
  line-height: 1.55 !important;
  font-family: var(--term-mono) !important;
  margin: 0 !important;
}

article.result .engines,
article.result .engines span,
article.result .cache_link {
  order: 4 !important;
  color: #38633e !important;
  font-size: 0.75rem !important;
  font-family: var(--term-mono) !important;
  margin-top: 5px !important;
}

article.result .cache_link {
  color: #4f8a58 !important;
  text-decoration: none !important;
  margin-left: 8px !important;
}
article.result .cache_link:hover {
  color: #8fe89a !important;
}

/* Sidebar & Infoboxes */
#sidebar {
  width: 320px !important;
  min-width: 280px !important;
  max-width: 340px !important;
  border-left: 1px solid #1a2e1d !important;
  padding-left: 1.5rem !important;
  box-sizing: border-box !important;
}

.infobox, .sidebar-collapsible {
  background: rgba(10, 18, 10, 0.6) !important;
  border: 1px solid #2e5735 !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  border-radius: 0 !important;
  padding: 1rem !important;
  box-sizing: border-box !important;
}

@media screen and (max-width: 850px) {
  #results {
    flex-direction: column !important;
    align-items: center !important;
  }
  #sidebar {
    width: 100% !important;
    max-width: 680px !important;
    border-left: none !important;
    border-top: 1px solid #1a2e1d !important;
    padding-left: 0 !important;
    padding-top: 1.5rem !important;
  }
}

/* ==========================================================================
   Pagination
   ========================================================================== */

#pagination, .numbered_pagination {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  flex-wrap: wrap !important;
  gap: 8px !important;
  margin: 2.5rem auto !important;
  width: 100% !important;
  max-width: 800px !important;
  font-family: var(--term-mono) !important;
}

#pagination button,
#pagination input[type="submit"],
#pagination input[type="button"],
.page_number input,
.previous_page button,
.next_page button {
  background: rgba(10, 18, 10, 0.8) !important;
  border: 1px solid #4f8a58 !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.85rem !important;
  padding: 6px 14px !important;
  cursor: pointer !important;
  border-radius: 0 !important;
  transition: all 0.15s ease !important;
}

#pagination button:hover,
#pagination input[type="submit"]:hover,
.page_number input:hover,
.previous_page button:hover,
.next_page button:hover {
  border-color: #8fe89a !important;
  color: #8fe89a !important;
  background: rgba(79, 138, 88, 0.15) !important;
}

.page_number_current,
#pagination input.page_number_current {
  background: #4f8a58 !important;
  color: #0a0d0a !important;
  border-color: #4f8a58 !important;
  font-weight: 700 !important;
}

/* ==========================================================================
   Preferences Page
   ========================================================================== */

.preferences_wrapper, #preferences, #main_preferences {
  max-width: 800px !important;
  width: 100% !important;
  margin: 2rem auto !important;
  padding: 0 1rem !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  box-sizing: border-box !important;
}

.preferences_section, fieldset {
  border: 1px solid #2e5735 !important;
  background: rgba(10, 18, 10, 0.6) !important;
  padding: 1.5rem !important;
  margin-bottom: 1.5rem !important;
  border-radius: 0 !important;
  box-sizing: border-box !important;
}

legend {
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  font-weight: 700 !important;
  padding: 0 8px !important;
}

.tabs .tab, .tabs label {
  background: transparent !important;
  border: 1px solid #2e5735 !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  border-radius: 0 !important;
  padding: 8px 16px !important;
}

.tabs .tab:hover, .tabs label:hover {
  color: #8fe89a !important;
  border-color: #4f8a58 !important;
}

.tabs input:checked + label, .tabs .tab.active {
  background: #4f8a58 !important;
  color: #0a0d0a !important;
  border-color: #4f8a58 !important;
  font-weight: 700 !important;
}

table, tr, td, th {
  border-color: #2e5735 !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
}

select, textarea, input {
  background: #0a0d0a !important;
  border: 1px solid #4f8a58 !important;
  color: #8fe89a !important;
  font-family: var(--term-mono) !important;
  border-radius: 0 !important;
  padding: 6px 10px !important;
}

select:focus, textarea:focus, input:focus {
  border-color: #8fe89a !important;
  outline: none !important;
  box-shadow: 0 0 8px rgba(143, 232, 154, 0.3) !important;
}

.btn, button.btn, input[type="submit"].btn {
  background: #4f8a58 !important;
  color: #0a0d0a !important;
  border: 1px solid #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-weight: 700 !important;
  padding: 8px 16px !important;
  cursor: pointer !important;
  border-radius: 0 !important;
}

.btn:hover, button.btn:hover {
  background: #8fe89a !important;
  color: #0a0d0a !important;
}

/* Error Dialog */
.dialog-error {
  background: #1a0a0a !important;
  border: 1px solid #ff5555 !important;
  color: #ff8888 !important;
  font-family: var(--term-mono) !important;
  padding: 1rem !important;
  border-radius: 0 !important;
  margin: 1rem auto !important;
  max-width: 680px !important;
  box-sizing: border-box !important;
}

/* ==========================================================================
   Footer
   ========================================================================== */

footer {
  border-top: 1px solid #1a2e1d !important;
  background: transparent !important;
  color: #4f8a58 !important;
  font-family: var(--term-mono) !important;
  font-size: 0.8rem !important;
  text-align: center !important;
  padding: 2rem 1rem !important;
  margin-top: 4rem !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}

footer a {
  color: #4f8a58 !important;
  text-decoration: none !important;
  font-family: var(--term-mono) !important;
}

footer a:hover {
  color: #8fe89a !important;
  text-decoration: underline !important;
}
'''

full_css = base_css + '\n' + terminal_css

with open('searxng/custom.css', 'w', encoding='utf-8') as f:
    f.write(full_css)

with open('searxng/custom.css.gz', 'wb') as f:
    f.write(gzip.compress(full_css.encode('utf-8'), compresslevel=9))

with open('searxng/custom.css.br', 'wb') as f:
    f.write(brotli.compress(full_css.encode('utf-8'), quality=11))

print('custom.css, custom.css.gz, and custom.css.br successfully generated! Total size:', len(full_css))
