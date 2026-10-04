/**
 * Devabhāṣā Modern — Smart TV Remote Controller
 * Listens for D-pad navigation, Enter/OK, and Back keys.
 */

class DevabhashaTvRemote {
  constructor(app) {
    this.app = app;
    this.isTvMode = false;
    this.focusableElements = [];
    this.currentIndex = 0;
    
    this.init();
  }

  init() {
    window.addEventListener('keydown', (e) => this.handleKeyDown(e));
  }

  toggleTvMode() {
    this.isTvMode = !this.isTvMode;
    document.body.classList.toggle('tv-mode', this.isTvMode);
    console.log(`[TV Remote] TV Mode: ${this.isTvMode ? 'ENABLED' : 'DISABLED'}`);
    if (this.isTvMode) {
      this.updateFocusables();
      this.focusCurrent();
    }
  }

  updateFocusables() {
    this.focusableElements = Array.from(document.querySelectorAll(
      'button:not([disabled]), input:not([disabled]), .chapter-nav-item, .recitation-card, [tabindex="0"]'
    )).filter(el => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0 && window.getComputedStyle(el).visibility !== 'hidden';
    });
  }

  handleKeyDown(e) {
    // Press 'T' to toggle TV mode
    if (e.key === 't' || e.key === 'T') {
      if (!e.target.matches('input, textarea')) {
        this.toggleTvMode();
        return;
      }
    }

    if (!this.isTvMode) return;

    this.updateFocusables();
    if (this.focusableElements.length === 0) return;

    switch (e.key) {
      case 'ArrowDown':
      case 'ArrowRight':
        e.preventDefault();
        this.currentIndex = (this.currentIndex + 1) % this.focusableElements.length;
        this.focusCurrent();
        break;

      case 'ArrowUp':
      case 'ArrowLeft':
        e.preventDefault();
        this.currentIndex = (this.currentIndex - 1 + this.focusableElements.length) % this.focusableElements.length;
        this.focusCurrent();
        break;

      case 'Enter':
        e.preventDefault();
        if (this.focusableElements[this.currentIndex]) {
          this.focusableElements[this.currentIndex].click();
        }
        break;

      case 'Escape':
      case 'Back':
      case 'BrowserBack':
        e.preventDefault();
        if (this.app) {
          this.app.closeAllModals();
        }
        break;
    }
  }

  focusCurrent() {
    this.focusableElements.forEach(el => el.classList.remove('tv-focused'));
    const target = this.focusableElements[this.currentIndex];
    if (target) {
      target.classList.add('tv-focused');
      target.focus();
      target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }
}
