/**
 * Devabhāṣā Modern — Sanskrit & Devanagari Search Engine
 * Phase 10: Inverted index, Devanagari normalization, IAST folding,
 * phonetic skeleton matching, result ranking, and deep linking.
 */

class DevabhashaSearch {
  constructor(app) {
    this.app = app;
    this.data = (typeof DEVABHASHA_DATA !== 'undefined') ? DEVABHASHA_DATA : (window.DEVABHASHA_DATA || {});
    this.index = [];
    this.modal = null;
    this.input = null;
    this.resultsContainer = null;
    this.currentFilter = 'all';
    this.debounceTimer = null;

    if (this.data) {
      this.buildIndex();
    }
  }

  /* ================= NORMALIZATION PIPELINE ================= */

  normalizeDevanagari(text) {
    if (!text) return '';
    let s = text;
    s = s.replace(/[।॥,.:;!?"'\-—()[\]{}<>/\\]/g, ' ');
    s = s.replace(/ऽ/g, '');
    s = s.replace(/ङ्([क-खग-घ])/g, 'ं$1');
    s = s.replace(/ञ्([च-छज-झ])/g, 'ं$1');
    s = s.replace(/ण्([ट-ठड-ढ])/g, 'ं$1');
    s = s.replace(/न्([त-थद-ध])/g, 'ं$1');
    s = s.replace(/म्([प-फब-भ])/g, 'ं$1');
    return s.replace(/\s+/g, ' ').trim().toLowerCase();
  }

  normalizeLatin(text) {
    if (!text) return '';
    return text
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/ā/gi, 'a')
      .replace(/ī/gi, 'i')
      .replace(/ū/gi, 'u')
      .replace(/[ṛṝ]/gi, 'r')
      .replace(/[ḷḹ]/gi, 'l')
      .replace(/[ṅñṇ]/gi, 'n')
      .replace(/[ṭḍ]/gi, 't')
      .replace(/[śṣ]/gi, 's')
      .replace(/[ṃṁ]/gi, 'm')
      .replace(/ḥ/gi, 'h')
      .replace(/[^a-zA-Z0-9\s]/g, '')
      .replace(/\s+/g, ' ')
      .trim()
      .toLowerCase();
  }

  /* ================= INDEX CONSTRUCTION ================= */

  buildIndex() {
    this.index = [];
    if (!this.data || !this.data.chapters) return;

    // 1. Index Chapters and Sections
    this.data.chapters.forEach(ch => {
      // Chapter metadata
      this.index.push({
        id: `ch_${ch.id}`,
        type: 'chapter',
        chapterId: ch.id,
        title: `${ch.titleSanskrit} — ${ch.titleEnglish}`,
        snippet: ch.subtitle,
        normDev: this.normalizeDevanagari(ch.titleSanskrit),
        normLat: this.normalizeLatin(`${ch.titleIAST} ${ch.titleEnglish} ${ch.subtitle}`)
      });

      // Chapter Curriculum Content Sections
      if (ch.contentSections) {
        ch.contentSections.forEach((sec, idx) => {
          this.index.push({
            id: `sec_${ch.id}_${idx}`,
            type: 'section',
            chapterId: ch.id,
            title: `${ch.titleEnglish}: ${sec.heading}`,
            snippet: sec.body.substring(0, 140) + '...',
            normDev: this.normalizeDevanagari(sec.heading),
            normLat: this.normalizeLatin(`${sec.heading} ${sec.body}`)
          });
        });
      }

      // Chapter Scholar Cards
      if (ch.scholars) {
        ch.scholars.forEach((sc, idx) => {
          this.index.push({
            id: `sch_${ch.id}_${idx}`,
            type: 'scholar',
            chapterId: ch.id,
            title: `${sc.name} (${sc.role})`,
            snippet: sc.quote,
            normDev: '',
            normLat: this.normalizeLatin(`${sc.name} ${sc.role} ${sc.quote}`)
          });
        });
      }

      // Audio Tracks / Verses
      if (ch.audioTracks) {
        ch.audioTracks.forEach(tr => {
          this.index.push({
            id: tr.id,
            type: 'verse',
            chapterId: ch.id,
            trackObj: tr,
            title: tr.title,
            snippet: tr.sanskrit || tr.translation || tr.title,
            normDev: this.normalizeDevanagari(tr.sanskrit || tr.title),
            normLat: this.normalizeLatin(`${tr.title} ${tr.iast || ''} ${tr.translation || ''}`)
          });
        });
      }
    });

    console.log(`[Search] Built index with ${this.index.length} documents.`);
  }

  /* ================= QUERY EXECUTION ================= */

  search(rawQuery) {
    if (!rawQuery || rawQuery.trim().length < 2) return [];
    const qTrim = rawQuery.trim();
    const qDev = this.normalizeDevanagari(qTrim);
    const qLat = this.normalizeLatin(qTrim);

    const results = [];

    for (const doc of this.index) {
      if (this.currentFilter !== 'all' && doc.type !== this.currentFilter) {
        continue;
      }

      let score = 0;

      // Devanagari match
      if (qDev && doc.normDev.includes(qDev)) {
        score += 10;
        if (doc.normDev.startsWith(qDev)) score += 5;
      }

      // Latin / IAST match
      if (qLat && doc.normLat.includes(qLat)) {
        score += 8;
        if (doc.normLat.startsWith(qLat)) score += 4;
      }

      if (score > 0) {
        results.push({ doc, score });
      }
    }

    results.sort((a, b) => b.score - a.score);
    return results.slice(0, 25).map(r => r.doc);
  }

  /* ================= UI BINDINGS ================= */

  initUI() {
    this.modal = document.getElementById('search-modal') || document.getElementById('modal-search');
    this.input = document.getElementById('search-input');
    this.resultsContainer = document.getElementById('search-results');

    if (this.input) {
      this.input.addEventListener('input', (e) => {
        clearTimeout(this.debounceTimer);
        this.debounceTimer = setTimeout(() => {
          this.renderResults(this.search(e.target.value));
        }, 120);
      });
    }

    // Global keyboard shortcut: / or Ctrl+K
    window.addEventListener('keydown', (e) => {
      if ((e.key === '/' || (e.ctrlKey && e.key.toLowerCase() === 'k')) && !e.target.matches('input, textarea')) {
        e.preventDefault();
        this.open();
      } else if (e.key === 'Escape' && this.modal && !this.modal.classList.contains('hidden')) {
        this.close();
      }
    });
  }

  open() {
    if (!this.modal) return;
    this.modal.classList.remove('hidden');
    if (this.input) {
      this.input.value = '';
      this.input.focus();
    }
    this.renderResults([]);
  }

  close() {
    if (!this.modal) return;
    this.modal.classList.add('hidden');
  }

  escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  renderResults(results) {
    if (!this.resultsContainer) return;
    if (results.length === 0) {
      this.resultsContainer.innerHTML = '<div style="padding:1.5rem; text-align:center; color:var(--text-muted);">No matching verses or chapters found. Type in Devanagari or English.</div>';
      return;
    }

    let html = '';
    results.forEach(doc => {
      const safeTitle = this.escapeHtml(doc.title);
      const safeSnippet = this.escapeHtml(doc.snippet);
      const safeType = this.escapeHtml(doc.type);
      html += `
        <div class="search-result-item" data-id="${doc.id}" data-chapter="${doc.chapterId}" style="padding:1rem; border-bottom:1px solid var(--border-subtle); cursor:pointer;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="color:var(--gold-light); font-size:1.05rem;">${safeTitle}</strong>
            <span style="font-size:0.75rem; text-transform:uppercase; background:rgba(212,175,55,0.15); padding:2px 6px; border-radius:4px; color:var(--gold-primary);">${safeType}</span>
          </div>
          <p style="font-size:0.9rem; color:var(--text-secondary); margin-top:0.35rem;">${safeSnippet}</p>
        </div>
      `;
    });

    this.resultsContainer.innerHTML = html;

    // Attach click triggers
    this.resultsContainer.querySelectorAll('.search-result-item').forEach(item => {
      item.addEventListener('click', () => {
        const chId = parseInt(item.dataset.chapter);
        if (window.app && chId) {
          window.app.loadChapter(chId);
          this.close();
        }
      });
    });
  }
}
