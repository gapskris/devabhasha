/**
 * Devabhāṣā Modern — Core Application Controller
 * Complete Visual, Layout, and Feature Parity with Ashtavadhanam (Pics 1, 2, and 3)
 * Butter-smooth 60fps Hardware-Accelerated Animations
 */

class DevabhashaApp {
  constructor() {
    this.data = (typeof DEVABHASHA_DATA !== 'undefined') ? DEVABHASHA_DATA : (window.DEVABHASHA_DATA || {});
    this.activeChapterId = 1;
    this.displayView = 'devanagari'; // 'devanagari' | 'bilingual' | 'english'
    document.body.classList.add('mode-devanagari');
    this.openingSequenceTimers = [];
    this.landingTimer = null;
    this.chimesEnabled = true;

    // DOM Elements
    this.splashGateway = document.getElementById('splash-gateway');
    this.openingTitleStage = document.getElementById('opening-title-stage');
    this.openingVideoStage = document.getElementById('opening-stage') || document.getElementById('opening-video-stage');
    this.titleContainer = document.getElementById('opening-title-container');
    this.mosaicContainer = document.getElementById('opening-mosaic-container');
    this.mosaicVideoWindow = document.getElementById('mosaic-video-window');
    this.openingMontageVideo = document.getElementById('opening-montage-video');
    this.statusTitle = document.getElementById('opening-sequence-status-title');
    this.statusDesc = document.getElementById('opening-sequence-status-desc');
    this.progressFill = document.getElementById('opening-sequence-progress');

    this.mosaicFrame03 = document.getElementById('mosaic-frame-03');
    this.mosaicFrame02 = document.getElementById('mosaic-frame-02');
    this.mosaicFrame01 = document.getElementById('mosaic-frame-01');

    this.btnStartFullExperience = document.getElementById('btn-start-full-experience');
    this.btnEnterDirect = document.getElementById('btn-enter-gateway') || document.getElementById('btn-enter-direct');
    this.btnSkipToMontage = document.getElementById('btn-skip-to-montage');
    this.btnSkipMontage = document.getElementById('btn-skip-opening') || document.getElementById('btn-skip-montage');
    this.btnMontageSoundToggle = document.getElementById('btn-montage-sound-toggle');
    this.btnToggleTheaterMode = document.getElementById('btn-toggle-theater-mode');

    // App Shell
    this.appShell = document.getElementById('app-shell');
    this.navDrawer = document.getElementById('nav-drawer');
    this.navBackdrop = document.getElementById('nav-drawer-backdrop');
    this.btnToggleMenu = document.getElementById('btn-toggle-menu');
    this.btnCloseNav = document.getElementById('btn-close-nav');
    this.btnCollapseSidebar = document.getElementById('btn-collapse-sidebar');

    this.chapterPillsContainer = document.getElementById('chapter-pills');
    this.btnChapterPrev = document.getElementById('btn-chapter-prev');
    this.btnChapterNext = document.getElementById('btn-chapter-next');

    this.stageChapterTitle = document.getElementById('stage-chapter-title');
    this.stageChapterSubmeta = document.getElementById('stage-chapter-submeta');
    this.stageCanvasBg = document.getElementById('stage-canvas-bg');
    this.dialoguesWrapper = document.getElementById('dialogues-wrapper');
    this.btnPlayAllChapter = document.getElementById('btn-play-all-chapter');
    this.scrollHintPill = document.getElementById('scroll-hint-pill');

    // Sub-Page Slide Ribbon & Anatomical Diagram Lightbox
    this.stageSlideBar = document.getElementById('stage-slide-bar');
    this.btnSlidePrev = document.getElementById('btn-slide-prev');
    this.btnSlideNext = document.getElementById('btn-slide-next');
    this.slideIndicators = document.getElementById('slide-indicators');
    this.slideCounter = document.getElementById('slide-counter');
    this.btnViewDiagram = document.getElementById('btn-view-diagram');
    this.modalDiagram = document.getElementById('modal-diagram');
    this.btnCloseDiagramModal = document.getElementById('btn-close-diagram-modal');
    this.modalDiagramImg = document.getElementById('modal-diagram-img');
    this.modalDiagramTitle = document.getElementById('modal-diagram-title');
    this.modalDiagramDesc = document.getElementById('modal-diagram-desc');

    // Dual-Pane Diagram Mode & Slide Verse Filtering
    this.canvasStageWrapper = document.getElementById('canvas-stage-wrapper');
    this.stageDiagramContainer = document.getElementById('stage-diagram-container');
    this.stageDiagramImg = document.getElementById('stage-diagram-img');
    this.diagramBadge = document.getElementById('diagram-badge');
    this.btnZoomDiagram = document.getElementById('btn-zoom-diagram');
    this.btnToggleVerseView = document.getElementById('btn-toggle-verse-view');
    this.verseViewIcon = document.getElementById('verse-view-icon');
    this.verseViewText = document.getElementById('verse-view-text');
    this.verseFilterMode = 'slide'; // 'slide' | 'all'

    this.activeSlideIndex = 0;
    this.currentSlides = [];
    this.currentDiagram = null;

    window.DevabhashaInstance = this;
    window.App = this;
    window.app = this;

    this.init();
  }

  async init() {
    console.log('[Devabhasha] Initializing application with 60fps animation engine...');
    
    // Asynchronously pre-decode opening frames into GPU memory to eliminate jank
    this.preloadOpeningImages();

    // Initialize Search and TV Remote
    if (window.DevabhashaSearch) {
      this.search = new DevabhashaSearch(this);
      this.search.initUI();
    }
    if (window.DevabhashaTvRemote) {
      this.tvRemote = new DevabhashaTvRemote(this);
    }

    this.bindEvents();
    this.initSidebarAndCarousel();
    this.initPWAInstallPrompt();
    this.loadChapter(1);

    // Start autonomous landing calligraphy dissolve
    this.startLandingAnimation();
  }

  /* ================= 60FPS ASYNCHRONOUS ASSET PRE-DECODING ================= */
  async preloadOpeningImages() {
    const urls = [
      'assets/images/opening/S01.jpg',
      'assets/images/opening/S02.jpg',
      'assets/images/opening/S03.jpg',
      'assets/images/opening/S04.jpg',
      'assets/images/opening/S05.jpg',
      'assets/images/opening/S06.jpg',
      'assets/images/opening/01.jpg',
      'assets/images/opening/02.jpg',
      'assets/images/opening/03.jpg'
    ];
    await Promise.all(urls.map(url => {
      const img = new Image();
      img.src = url;
      return img.decode().catch(() => {});
    }));
  }

  /* ================= EVENT BINDINGS ================= */
  bindEvents() {
    // 1. Landing Gateway Buttons
    if (this.btnStartFullExperience) {
      this.btnStartFullExperience.addEventListener('click', () => this.runMontagePhase());
    }
    if (this.btnEnterDirect) {
      this.btnEnterDirect.addEventListener('click', () => this.enterApp());
    }
    if (this.btnSkipMontage) {
      this.btnSkipMontage.addEventListener('click', () => this.enterApp());
    }
    if (this.btnSkipToMontage) {
      this.btnSkipToMontage.addEventListener('click', () => this.runMontagePhase());
    }

    // Landing Page Theme Switcher Toggle (Dark Charcoal vs. Warm Amber/Gold)
    const btnLandingTheme = document.getElementById('btn-landing-theme-toggle');
    const savedLandingTheme = localStorage.getItem('devabhasha_landing_theme') || 'dark';
    this.applyLandingTheme(savedLandingTheme);

    if (btnLandingTheme) {
      btnLandingTheme.addEventListener('click', (e) => {
        e.stopPropagation();
        const currentIsDark = this.openingTitleStage && this.openingTitleStage.classList.contains('theme-dark');
        const nextTheme = currentIsDark ? 'amber' : 'dark';
        this.applyLandingTheme(nextTheme);
        localStorage.setItem('devabhasha_landing_theme', nextTheme);
      });
    }

    // Toggle Sound for Montage Video
    if (this.btnMontageSoundToggle && this.openingMontageVideo) {
      this.btnMontageSoundToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        this.openingMontageVideo.muted = !this.openingMontageVideo.muted;
        this.btnMontageSoundToggle.textContent = this.openingMontageVideo.muted ? '🔇 Sound: OFF' : '🔊 Sound: ON';
      });
    }

    // Toggle Expanded Theater / 1997 Mosaic Mode
    if (this.btnToggleTheaterMode && this.mosaicContainer) {
      this.btnToggleTheaterMode.addEventListener('click', (e) => {
        e.stopPropagation();
        const isTheater = this.mosaicContainer.classList.toggle('theater-mode');
        this.btnToggleTheaterMode.textContent = isTheater ? '🖼️ 1997 Mosaic Frame' : '🔲 Expand Theater';
      });
    }

    // 2. Navigation Drawer Toggle & Scrim
    const toggleNav = () => {
      if (window.innerWidth >= 1024) {
        // Desktop: toggle between sidebar-docked and sidebar-collapsed
        const isDocked = document.body.classList.contains('sidebar-docked');
        if (isDocked) {
          document.body.classList.remove('sidebar-docked');
          document.body.classList.add('sidebar-collapsed');
          if (this.btnCollapseSidebar) {
            this.btnCollapseSidebar.textContent = '▶';
            this.btnCollapseSidebar.title = 'Expand Sidebar';
          }
        } else {
          document.body.classList.remove('sidebar-collapsed');
          document.body.classList.add('sidebar-docked');
          if (this.btnCollapseSidebar) {
            this.btnCollapseSidebar.textContent = '◀';
            this.btnCollapseSidebar.title = 'Collapse Sidebar';
          }
        }
      } else {
        // Mobile / Tablet: toggle overlay drawer
        const isOpen = this.navDrawer.classList.toggle('open');
        if (this.navBackdrop) {
          this.navBackdrop.classList.toggle('hidden', !isOpen);
        }
      }
    };
    if (this.btnToggleMenu) this.btnToggleMenu.addEventListener('click', toggleNav);
    if (this.btnCollapseSidebar) this.btnCollapseSidebar.addEventListener('click', toggleNav);

    // Mobile close & backdrop
    const closeMobileNav = () => {
      if (this.navDrawer) this.navDrawer.classList.remove('open');
      if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
    };
    if (this.btnCloseNav) this.btnCloseNav.addEventListener('click', closeMobileNav);
    if (this.navBackdrop) this.navBackdrop.addEventListener('click', closeMobileNav);

    // Helper to close mobile drawer on navigation
    this.closeMobileDrawer = () => {
      if (window.innerWidth < 1024) {
        if (this.navDrawer) this.navDrawer.classList.remove('open');
        if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
      }
    };

    // Curriculum & Treatises Direct Navigation
    const btnCurriculum = document.getElementById('btn-nav-curriculum');
    if (btnCurriculum) {
      btnCurriculum.addEventListener('click', () => {
        this.loadChapter(this.activeChapterId || 1);
        window.scrollTo({ top: 0, behavior: 'smooth' });
        this.closeMobileDrawer();
      });
    }

    const btnLinguistics = document.getElementById('btn-nav-linguistics');
    if (btnLinguistics) {
      btnLinguistics.addEventListener('click', () => {
        this.loadChapter(1);
        this.closeMobileDrawer();
      });
    }

    const btnChitrakavya = document.getElementById('btn-nav-chitrakavya');
    if (btnChitrakavya) {
      btnChitrakavya.addEventListener('click', () => {
        this.loadChapter(3);
        this.closeMobileDrawer();
      });
    }

    const btnSacred = document.getElementById('btn-nav-sacred');
    if (btnSacred) {
      btnSacred.addEventListener('click', () => {
        this.loadChapter(7);
        this.closeMobileDrawer();
      });
    }

    // Home buttons -> Return to Landing Gateway
    const goHome = () => this.returnToLandingGateway();
    const btnHome = document.getElementById('btn-home');
    if (btnHome) btnHome.addEventListener('click', goHome);
    const brandHome = document.getElementById('brand-home');
    if (brandHome) brandHome.addEventListener('click', goHome);

    // 3. 3-Way Segmented Display Switcher
    document.querySelectorAll('.view-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
        e.currentTarget.classList.add('active');
        this.displayView = e.currentTarget.dataset.view;
        document.body.classList.remove('mode-devanagari', 'mode-bilingual', 'mode-english');
        document.body.classList.add(`mode-${this.displayView}`);
        this.renderChapterCards();
        this.renderSlide(this.activeSlideIndex, false);
        this.updateHeaderMetaLabels();
        if (window.Player) {
          if (typeof window.Player.updateTrackDisplay === 'function') window.Player.updateTrackDisplay();
          if (typeof window.Player.updatePlayState === 'function') window.Player.updatePlayState();
        }
      });
    });

    // 4. Chapter Carousel Arrows
    if (this.btnChapterPrev) {
      this.btnChapterPrev.addEventListener('click', () => {
        if (this.activeChapterId > 1) this.loadChapter(this.activeChapterId - 1);
      });
    }
    if (this.btnChapterNext) {
      this.btnChapterNext.addEventListener('click', () => {
        if (this.activeChapterId < 10) this.loadChapter(this.activeChapterId + 1);
      });
    }

    // 5. Play All in Chapter
    if (this.btnPlayAllChapter) {
      this.btnPlayAllChapter.addEventListener('click', () => {
        if (window.Player) window.Player.togglePlay();
      });
    }

    // 5B. Sub-page Slide Navigation Ribbon
    if (this.btnSlidePrev) {
      this.btnSlidePrev.addEventListener('click', () => this.prevSlide());
    }
    if (this.btnSlideNext) {
      this.btnSlideNext.addEventListener('click', () => this.nextSlide());
    }

    // 5C. Diagram Lightbox & Zoom Triggers
    if (this.btnViewDiagram) {
      this.btnViewDiagram.addEventListener('click', () => this.openDiagramModal());
    }
    if (this.btnZoomDiagram) {
      this.btnZoomDiagram.addEventListener('click', () => this.openDiagramModal());
    }
    if (this.btnCloseDiagramModal) {
      this.btnCloseDiagramModal.addEventListener('click', () => {
        if (this.modalDiagram) this.modalDiagram.classList.add('hidden');
      });
    }

    // 5D. Slide Verses vs. All Chapter Tracks View Toggle
    if (this.btnToggleVerseView) {
      this.btnToggleVerseView.addEventListener('click', () => {
        this.verseFilterMode = (this.verseFilterMode === 'slide' ? 'all' : 'slide');
        if (this.verseViewIcon) {
          this.verseViewIcon.textContent = (this.verseFilterMode === 'slide' ? '📄' : '📜');
        }
        if (this.verseViewText) {
          this.verseViewText.textContent = (this.verseFilterMode === 'slide' ? 'Slide Verses' : 'All Tracks');
        }
        this.filterVersesBySlide(true);
      });
    }

    // 6. Header & Nav Action Modals
    const bindModal = (btnId, modalId) => {
      const btn = document.getElementById(btnId);
      if (btn) {
        btn.addEventListener('click', () => {
          this.closeMobileDrawer();
          this.openModal(modalId);
        });
      }
    };

    bindModal('btn-header-search', 'search-modal');
    bindModal('btn-nav-search', 'search-modal');
    bindModal('btn-header-shlokas', 'modal-shlokas');
    bindModal('btn-nav-shlokas', 'modal-shlokas');
    bindModal('btn-nav-credits', 'modal-credits');
    bindModal('btn-nav-institutions', 'modal-institu');
    bindModal('btn-nav-sas', 'modal-sas');
    bindModal('btn-nav-scholars', 'modal-scholars');
    bindModal('btn-nav-gallery', 'modal-gallery');
    bindModal('btn-header-help', 'modal-help');
    bindModal('btn-nav-help', 'modal-help');
    bindModal('btn-exit-gateway', 'modal-exit');

    // 7. TV Mode and Fullscreen Header Controls
    const btnTv = document.getElementById('btn-tv-mode');
    if (btnTv) {
      btnTv.addEventListener('click', () => {
        if (this.tvRemote) {
          this.tvRemote.toggleTvMode();
          btnTv.classList.toggle('active', this.tvRemote.isTvMode);
        }
      });
    }

    const btnFs = document.getElementById('btn-fullscreen');
    if (btnFs) {
      btnFs.addEventListener('click', () => {
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(err => console.warn(err));
        } else {
          document.exitFullscreen().catch(err => console.warn(err));
        }
      });
      document.addEventListener('fullscreenchange', () => {
        const isFs = !!document.fullscreenElement;
        btnFs.classList.toggle('active', isFs);
        btnFs.textContent = isFs ? '🗗' : '⛶';
        btnFs.title = isFs ? 'Exit Fullscreen' : 'Toggle Fullscreen';
      });
    }

    // Replay opening
    const btnReplay = document.getElementById('btn-replay-opening');
    if (btnReplay) {
      btnReplay.addEventListener('click', () => {
        if (this.navDrawer) this.navDrawer.classList.remove('open');
        if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
        if (this.appShell) this.appShell.classList.add('hidden');
        if (this.splashGateway) this.splashGateway.classList.remove('hidden');
        if (window.Player) window.Player.audio.pause();
        this.runMontagePhase();
      });
    }

    // Temple Bell Chimes Toggle
    const btnChimes = document.getElementById('btn-toggle-chimes');
    if (btnChimes) {
      btnChimes.addEventListener('click', () => {
        this.chimesEnabled = !this.chimesEnabled;
        const label = document.getElementById('chimes-primary-label');
        if (label) label.textContent = `Temple Bell Chimes: ${this.chimesEnabled ? 'ON' : 'OFF'}`;
      });
    }

    // Close Modals
    document.querySelectorAll('.btn-close-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const modal = e.target.closest('.modal-overlay');
        if (modal) modal.classList.add('hidden');
      });
    });

    document.querySelectorAll('.modal-overlay').forEach(overlay => {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.add('hidden');
      });
    });

    const btnConfirmExit = document.getElementById('btn-confirm-return-gateway');
    if (btnConfirmExit) {
      btnConfirmExit.addEventListener('click', () => {
        const modal = document.getElementById('modal-exit');
        if (modal) modal.classList.add('hidden');
        this.returnToLandingGateway();
      });
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-overlay').forEach(m => m.classList.add('hidden'));
        if (this.navDrawer) this.navDrawer.classList.remove('open');
        if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
      } else if (e.key === ' ' && !e.target.matches('input, textarea')) {
        e.preventDefault();
        if (window.Player) window.Player.togglePlay();
      } else if (e.key === 'ArrowLeft') {
        if (this.activeChapterId > 1) this.loadChapter(this.activeChapterId - 1);
      } else if (e.key === 'ArrowRight') {
        if (this.activeChapterId < 10) this.loadChapter(this.activeChapterId + 1);
      } else if ((e.ctrlKey && e.key === 'k') || e.key === '/') {
        if (!e.target.matches('input, textarea')) {
          e.preventDefault();
          this.openModal('modal-search');
        }
      }
    });
  }

  /* ================= LANDING THEME CONTROLLER ================= */
  applyLandingTheme(theme) {
    const isDark = (theme === 'dark');
    if (this.openingTitleStage) {
      this.openingTitleStage.classList.toggle('theme-dark', isDark);
    }
    const themeIcon = document.getElementById('theme-toggle-icon');
    const themeLabel = document.getElementById('theme-toggle-label');
    if (themeIcon) {
      themeIcon.textContent = isDark ? '☀️' : '🌙';
    }
    if (themeLabel) {
      themeLabel.textContent = isDark ? 'Golden Amber' : 'Dark Theme';
    }
  }

  /* ================= AUTONOMOUS LANDING DISSOLVE (PIC 1) ================= */
  startLandingAnimation() {
    this.stopLandingAnimation();
    const landingFrames = [
      document.getElementById('landing-frame-1'),
      document.getElementById('landing-frame-2'),
      document.getElementById('landing-frame-3'),
      document.getElementById('landing-frame-4'),
      document.getElementById('landing-frame-5'),
      document.getElementById('landing-frame-6')
    ].filter(Boolean);

    if (landingFrames.length < 6) return;

    landingFrames.forEach((f, i) => {
      if (i === 0) f.classList.add('active');
      else f.classList.remove('active');
    });

    let step = 0;
    this.landingTimer = setInterval(() => {
      step++;
      if (step < 6) {
        landingFrames[step].classList.add('active');
      } else {
        // Hold on final frame S06
        clearInterval(this.landingTimer);
        this.landingTimer = null;
      }
    }, 750);
  }

  stopLandingAnimation() {
    if (this.landingTimer) {
      clearInterval(this.landingTimer);
      this.landingTimer = null;
    }
  }

  /* ================= AUTHENTIC OPENING CHOREOGRAPHY (PICS 1 & 2) ================= */
  runOpeningSequence() {
    this.stopLandingAnimation();
    this.openingSequenceTimers.forEach(t => clearTimeout(t));
    this.openingSequenceTimers = [];

    if (this.openingTitleStage) this.openingTitleStage.classList.add('hidden');
    if (this.openingVideoStage) this.openingVideoStage.classList.remove('hidden');
    if (this.mosaicContainer) this.mosaicContainer.classList.add('hidden');
    if (this.titleContainer) this.titleContainer.classList.remove('hidden');

    if (this.statusTitle) this.statusTitle.textContent = "Devabhāṣā — The Language of the Gods";
    if (this.statusDesc) this.statusDesc.textContent = "Phase 1: Illuminated Title Calligraphy";
    if (this.progressFill) this.progressFill.style.width = "5%";

    // Pre-buffer video during synchronous user click
    if (this.openingMontageVideo) {
      this.openingMontageVideo.muted = false;
      this.openingMontageVideo.load();
    }

    const titleFrames = [
      document.getElementById('opening-calligraphy-layer') || document.getElementById('opening-title-img'),
      document.getElementById('title-frame-2'),
      document.getElementById('title-frame-3'),
      document.getElementById('title-frame-4'),
      document.getElementById('title-frame-5'),
      document.getElementById('title-frame-6')
    ].filter(Boolean);

    titleFrames.forEach((f, i) => {
      if (i === 0) f.classList.add('active');
      else f.classList.remove('active');
    });

    const delays = [0, 800, 1600, 2400, 3200, 4000];
    delays.forEach((delay, idx) => {
      if (idx === 0) return;
      const t = setTimeout(() => {
        if (titleFrames[idx]) titleFrames[idx].classList.add('active');
        const pct = Math.round(5 + ((idx + 1) / 6) * 30);
        if (this.progressFill) this.progressFill.style.width = `${pct}%`;
        if (this.statusDesc) {
          this.statusDesc.textContent = `Illuminating Title Calligraphy — Stage ${idx + 1} of 6`;
        }

        if (idx === 5) {
          const finishTimer = setTimeout(() => {
            this.runMontagePhase();
          }, 2000);
          this.openingSequenceTimers.push(finishTimer);
        }
      }, delay);
      this.openingSequenceTimers.push(t);
    });
  }

  /* ================= PHASE 2: CULTURAL MOSAIC & MONTAGE (PIC 2) ================= */
  runMontagePhase() {
    this.stopLandingAnimation();
    this.openingSequenceTimers.forEach(t => clearTimeout(t));
    this.openingSequenceTimers = [];

    // Pre-buffer video during synchronous user click
    if (this.openingMontageVideo) {
      this.openingMontageVideo.muted = false;
      this.openingMontageVideo.load();
    }

    if (this.openingTitleStage) this.openingTitleStage.classList.add('hidden');
    if (this.openingVideoStage) this.openingVideoStage.classList.remove('hidden');
    if (this.titleContainer) this.titleContainer.classList.add('hidden');
    if (this.mosaicContainer) this.mosaicContainer.classList.remove('hidden');

    if (this.btnSkipToMontage) this.btnSkipToMontage.style.display = 'none';

    // Step 2A: Display 03.jpg (Color Cultural Mosaic)
    if (this.mosaicFrame03) this.mosaicFrame03.classList.add('active');
    if (this.mosaicFrame02) this.mosaicFrame02.classList.remove('active');
    if (this.mosaicFrame01) this.mosaicFrame01.classList.remove('active');
    if (this.mosaicVideoWindow) this.mosaicVideoWindow.classList.remove('visible');

    if (this.statusTitle) this.statusTitle.textContent = "Authentic 1997 Cultural Mosaic";
    if (this.statusDesc) this.statusDesc.textContent = "Phase 2: Cultural Heritage Mosaic";
    if (this.progressFill) this.progressFill.style.width = "35%";

    // Step 2B: Crossfade to 02.jpg (Sepia Transition Mosaic) at 1.2s
    const t2 = setTimeout(() => {
      if (this.mosaicFrame02) this.mosaicFrame02.classList.add('active');
      if (this.mosaicFrame03) this.mosaicFrame03.classList.remove('active');
      if (this.statusDesc) this.statusDesc.textContent = "Phase 2: Transition Mosaic";
      if (this.progressFill) this.progressFill.style.width = "40%";
    }, 1200);
    this.openingSequenceTimers.push(t2);

    // Step 2C: Crossfade to 01.jpg (Cutout) and launch pre-buffered video at 2.4s
    const t3 = setTimeout(() => {
      if (this.mosaicFrame01) this.mosaicFrame01.classList.add('active');
      if (this.mosaicFrame02) this.mosaicFrame02.classList.remove('active');
      if (this.mosaicVideoWindow) this.mosaicVideoWindow.classList.add('visible');

      if (this.statusTitle) this.statusTitle.textContent = "Authentic 1997 Archival Montage";
      if (this.statusDesc) this.statusDesc.textContent = "Phase 2: Archival Montage Video & Sanskrit Invocations";
      if (this.progressFill) this.progressFill.style.width = "45%";

      if (this.openingMontageVideo) {
        this.openingMontageVideo.currentTime = 0;
        this.openingMontageVideo.muted = false;
        this.openingMontageVideo.play().catch(e => {
          console.warn('Video playback requires mute fallback:', e);
          this.openingMontageVideo.muted = true;
          this.openingMontageVideo.play();
          if (this.btnMontageSoundToggle) {
            this.btnMontageSoundToggle.textContent = '🔇 Click to Unmute';
          }
        });
      }
    }, 2400);
    this.openingSequenceTimers.push(t3);

    // Video progress & onended handler
    if (this.openingMontageVideo) {
      this.openingMontageVideo.ontimeupdate = () => {
        if (this.openingMontageVideo.duration) {
          const vpct = this.openingMontageVideo.currentTime / this.openingMontageVideo.duration;
          const overallPct = Math.round(45 + vpct * 50);
          if (this.progressFill) this.progressFill.style.width = `${overallPct}%`;
        }
      };

      this.openingMontageVideo.onended = () => {
        this.enterApp();
      };
    }
  }

  /* ================= ENTER MAIN APPLICATION ================= */
  enterApp() {
    this.stopLandingAnimation();
    this.openingSequenceTimers.forEach(t => clearTimeout(t));
    this.openingSequenceTimers = [];

    if (this.openingMontageVideo) this.openingMontageVideo.pause();

    if (this.splashGateway) this.splashGateway.classList.add('hidden');
    if (this.appShell) this.appShell.classList.remove('hidden');

    window.scrollTo(0, 0);
    this.loadChapter(1);
  }

  returnToLandingGateway() {
    if (this.openingMontageVideo) this.openingMontageVideo.pause();
    if (window.Player) window.Player.audio.pause();

    if (this.appShell) this.appShell.classList.add('hidden');
    if (this.splashGateway) this.splashGateway.classList.remove('hidden');
    if (this.openingVideoStage) this.openingVideoStage.classList.add('hidden');
    if (this.openingTitleStage) this.openingTitleStage.classList.remove('hidden');

    this.startLandingAnimation();
  }

  /* ================= SIDEBAR & CAROUSEL INITIALIZATION ================= */
  initSidebarAndCarousel() {
    const chapters = this.data.chapters || [];
    
    // Top Carousel Pills
    if (this.chapterPillsContainer) {
      this.chapterPillsContainer.innerHTML = '';
      chapters.forEach(ch => {
        const titleSa = ch.titleSanskrit || ch.title_sa || '';
        const titleEn = ch.titleEnglish || ch.title_en || '';
        const pill = document.createElement('button');
        pill.className = `chapter-pill ${ch.id === this.activeChapterId ? 'active' : ''}`;
        pill.dataset.chapterId = ch.id;
        pill.textContent = (this.displayView === 'devanagari') ? `अध्यायः ${ch.id}` : `Ch. ${ch.id}`;
        pill.title = `Chapter ${ch.id}: ${titleSa} — ${titleEn}`;
        pill.addEventListener('click', () => this.loadChapter(ch.id));
        this.chapterPillsContainer.appendChild(pill);
      });
    }

    // Left Navigation Drawer
    const drawerList = document.getElementById('chapter-nav-list') || document.getElementById('drawer-chapter-list');
    if (drawerList) {
      drawerList.innerHTML = '';
      chapters.forEach(ch => {
        const titleSa = ch.titleSanskrit || ch.title_sa || '';
        const titleEn = ch.titleEnglish || ch.title_en || '';
        const li = document.createElement('li');
        li.innerHTML = `
          <button class="nav-link ${ch.id === this.activeChapterId ? 'active' : ''}" data-chapter-id="${ch.id}">
            <span class="nav-icon">📖</span>
            <span class="nav-text">
              <span class="text-primary-label">Ch. ${ch.id}: ${titleEn}</span>
              <span class="text-secondary-label">${titleSa}</span>
            </span>
          </button>
        `;
        li.querySelector('button').addEventListener('click', () => {
          this.loadChapter(ch.id);
          if (window.innerWidth < 1024) {
            if (this.navDrawer) this.navDrawer.classList.remove('open');
            if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
          }
        });
        drawerList.appendChild(li);
      });
    }
  }

  /* ================= LOAD CHAPTER & RENDER PARCHMENT STAGE ================= */
  loadChapter(chapterId) {
    this.activeChapterId = chapterId;
    const chapters = this.data.chapters || [];
    const chapter = chapters.find(c => c.id === chapterId) || chapters[0];
    if (!chapter) return;

    // Update Top Carousel Active State & Auto-Center Pill
    document.querySelectorAll('.chapter-pill').forEach(pill => {
      const id = parseInt(pill.dataset.chapterId, 10);
      const isActive = (id === chapterId);
      pill.classList.toggle('active', isActive);
      if (isActive && this.chapterPillsContainer) {
        const targetLeft = pill.offsetLeft - (this.chapterPillsContainer.clientWidth / 2) + (pill.clientWidth / 2);
        this.chapterPillsContainer.scrollTo({ left: Math.max(0, targetLeft), behavior: 'smooth' });
      }
    });

    // Update Carousel Arrow Disabled States
    if (this.btnChapterPrev) {
      this.btnChapterPrev.disabled = (chapterId <= 1);
      this.btnChapterPrev.classList.toggle('disabled', chapterId <= 1);
    }
    if (this.btnChapterNext) {
      this.btnChapterNext.disabled = (chapterId >= 10);
      this.btnChapterNext.classList.toggle('disabled', chapterId >= 10);
    }

    // Update Drawer Active State
    document.querySelectorAll('#chapter-nav-list .nav-link, #drawer-chapter-list .nav-link').forEach(link => {
      const id = parseInt(link.dataset.chapterId, 10);
      link.classList.toggle('active', id === chapterId);
    });
    const elLing = document.getElementById('btn-nav-linguistics');
    if (elLing) elLing.classList.toggle('active', chapterId === 1);
    const elChitra = document.getElementById('btn-nav-chitrakavya');
    if (elChitra) elChitra.classList.toggle('active', chapterId === 3);
    const elSacred = document.getElementById('btn-nav-sacred');
    if (elSacred) elSacred.classList.toggle('active', chapterId === 7);

    // Update Stage Header Info
    this.updateHeaderMetaLabels(chapter);

    // Configure safe zone illustration layout
    if (this.dialoguesWrapper) {
      this.dialoguesWrapper.classList.remove('art-left', 'art-right', 'art-center');
      if ([1, 5, 7].includes(chapter.id)) {
        this.dialoguesWrapper.classList.add('art-left');
      } else if ([2, 8, 9, 10].includes(chapter.id)) {
        this.dialoguesWrapper.classList.add('art-right');
      } else {
        this.dialoguesWrapper.classList.add('art-center');
      }
    }

    // Setup Multi-Slide Sub-Paging
    this.currentSlides = chapter.slides && chapter.slides.length > 0
      ? chapter.slides
      : [{ id: 1, slideNumber: 1, title: titleEn, canvas: chapter.canvas }];
    this.activeSlideIndex = 0;
    this.initSlideRibbon();

    this.renderChapterCards();
    this.renderSlide(0, false);
  }

  /* ================= SCRIPT-AWARE STAGE HEADER META LABELS ================= */
  updateHeaderMetaLabels(chapter) {
    if (!chapter) {
      const chapters = this.data.chapters || [];
      chapter = chapters.find(c => c.id === this.activeChapterId) || chapters[0];
    }
    if (!chapter) return;

    const audioTracks = chapter.audioTracks || chapter.recitations || [];
    const titleSa = chapter.titleSanskrit || chapter.title_sa || '';
    const titleEn = chapter.titleEnglish || chapter.title_en || '';

    if (this.stageChapterTitle) {
      this.stageChapterTitle.textContent = this.displayView === 'devanagari'
        ? `दशसु ${this.getSanskritOrdinal(chapter.id)}ऽध्यायः • अध्यायः ${chapter.id}`
        : `Chapter ${chapter.id} of 10`;
    }

    if (this.stageChapterSubmeta) {
      if (this.displayView === 'devanagari') {
        const countText = audioTracks.length === 1 ? 'एकं ध्वन्यङ्कनम्' : `${audioTracks.length} ध्वन्यङ्कनानि`;
        this.stageChapterSubmeta.textContent = audioTracks.length > 0 
          ? `${titleSa} • ${countText}`
          : titleSa;
      } else if (this.displayView === 'bilingual') {
        const trackWord = audioTracks.length === 1 ? 'Audio Recitation' : 'Audio Recitations';
        this.stageChapterSubmeta.textContent = audioTracks.length > 0 
          ? `${audioTracks.length} ${trackWord} • ${titleSa} — ${titleEn}`
          : `${titleSa} — ${titleEn}`;
      } else {
        const trackWord = audioTracks.length === 1 ? 'Audio Recitation' : 'Audio Recitations';
        this.stageChapterSubmeta.textContent = audioTracks.length > 0 
          ? `${audioTracks.length} ${trackWord} • ${titleEn}`
          : titleEn;
      }
    }

    const playAllText = document.getElementById('play-all-text');
    if (playAllText) {
      playAllText.textContent = this.displayView === 'devanagari' ? 'सर्वेषां गानम्' : 'Play All in Chapter';
    }

    const verseViewText = document.getElementById('verse-view-text');
    if (verseViewText) {
      verseViewText.textContent = this.displayView === 'devanagari'
        ? (this.verseFilterMode === 'slide' ? 'पृष्ठ-श्लोकाः' : 'सर्वे श्लोकाः')
        : (this.verseFilterMode === 'slide' ? 'Slide Verses' : 'All Tracks');
    }

    // Keep top chapter carousel pills synchronized with view mode
    if (this.chapterPillsContainer) {
      const pills = this.chapterPillsContainer.querySelectorAll('.chapter-pill');
      pills.forEach(pill => {
        const chId = pill.dataset.chapterId;
        pill.textContent = (this.displayView === 'devanagari') ? `अध्यायः ${chId}` : `Ch. ${chId}`;
      });
    }
  }

  getSanskritOrdinal(num) {
    const ordinals = ['', 'प्रथमो', 'द्वितीयो', 'तृतीयो', 'चतुर्थो', 'पञ्चमो', 'षष्ठो', 'सप्तमो', 'अष्टमो', 'नवमो', 'दशमो'];
    return ordinals[num] || `${num}`;
  }

  formatSanskritDisplay(text) {
    if (!text) return '';
    // Ensure non-breaking space before dandas
    const glued = text.replace(/[ \t]+([।॥])/g, '\u00A0$1');
    const lines = glued.split('\n');
    if (lines.length > 1) {
      return lines.map(line => `<div class="verse-line">${line.trim()}</div>`).join('');
    }
    return glued;
  }

  formatIastDisplay(text) {
    if (!text) return '';
    const lines = text.split('\n');
    if (lines.length > 1) {
      return lines.map(line => `<div class="iast-line">${line.trim()}</div>`).join('');
    }
    return text;
  }

  /* ================= RENDER STACKED MANUSCRIPT CARDS ================= */
  renderChapterCards() {
    if (!this.dialoguesWrapper) return;
    this.dialoguesWrapper.innerHTML = '';

    const chapters = this.data.chapters || [];
    const chapter = chapters.find(c => c.id === this.activeChapterId) || chapters[0];
    if (!chapter) return;

    const audioTracks = chapter.audioTracks || chapter.recitations || [];
    const contentSections = chapter.contentSections || chapter.sections || [];
    const playlist = [];

    const titleEn = chapter.titleEnglish || chapter.title_en || '';

    // If audio tracks exist for this chapter
    if (audioTracks.length > 0) {
      audioTracks.forEach((track, idx) => {
        const trackTitle = track.title || `Chapter ${chapter.id} Verse ${idx + 1}`;
        const trackSpeaker = track.speaker || 'वक्ता • Speaker';
        const trackSanskrit = track.sanskrit || track.text_sa || '';
        const trackIast = track.iast || track.text_iast || '';
        const trackTranslation = track.translation || track.text_en || '';
        const trackSa = track.titleSanskrit || track.title_sa || '';

        playlist.push({
          id: track.id || `chap${chapter.id}_${idx + 1}`,
          slideIndex: track.slideIndex !== undefined ? track.slideIndex : 0,
          m4a: track.m4a,
          mp3: track.mp3,
          title: trackTitle,
          titleSanskrit: trackSa || trackSanskrit || trackTitle,
          speaker: trackSpeaker,
          chapterTitle: `Devabhāṣā Chapter ${chapter.id}: ${titleEn}`,
          sanskrit: trackSanskrit,
          iast: trackIast,
          translation: trackTranslation
        });

        const card = document.createElement('div');
        card.className = 'dialogue-card';
        card.dataset.index = idx;

        const speakerClass = (idx % 2 === 0) ? 'speaker-avadhani' : 'speaker-shloka';

        const formattedSa = this.formatSanskritDisplay(trackSanskrit);
        const formattedIast = this.formatIastDisplay(trackIast);
        const formattedEn = trackTranslation ? trackTranslation.replace(/\n/g, '<br>') : '';

        let bodyHtml = '';
        if (this.displayView === 'devanagari') {
          bodyHtml = formattedSa 
            ? `<div class="text-sanskrit">${formattedSa}</div>` 
            : `<div class="text-sanskrit" style="font-size:1.15rem; color: #78350f;">${trackTitle}</div>`;
        } else if (this.displayView === 'english') {
          bodyHtml = `
            ${formattedIast ? `<div class="text-iast">${formattedIast}</div>` : ''}
            ${formattedEn ? `<div class="text-english">${formattedEn}</div>` : ''}
          `;
          if (!bodyHtml.trim()) {
            bodyHtml = `<div class="text-english" style="font-size:1rem; color: #78350f;">${trackTitle}</div>`;
          }
        } else {
          // Bilingual
          bodyHtml = `
            ${formattedSa ? `<div class="text-sanskrit">${formattedSa}</div>` : ''}
            ${formattedIast ? `<div class="text-iast">${formattedIast}</div>` : ''}
            ${formattedEn ? `<div class="text-english">${formattedEn}</div>` : ''}
          `;
        }

        // If bodyHtml is empty (e.g. Varṇamālā sound clips without Sanskrit text)
        if (!bodyHtml.trim()) {
          bodyHtml = `<div class="text-sanskrit" style="font-size:1.15rem; color: #78350f;">${trackTitle}</div>`;
        }

        // Compute script-specific semantic seal title
        let sealTitle = '';

        if (this.displayView === 'devanagari') {
          if (trackSa) {
            sealTitle = trackSa;
          } else if (chapter.id === 1) {
            sealTitle = 'रघुवंश-मङ्गलाचरणम् • महाकवि-कालिदासः';
          } else {
            sealTitle = `श्लोकः ${idx + 1}`;
          }
        } else if (this.displayView === 'english') {
          sealTitle = trackTitle;
        } else {
          // Bilingual
          if (trackSa) {
            let shortEn = trackTitle;
            if (shortEn.includes('—')) {
              shortEn = shortEn.split('—')[0].trim();
            } else if (shortEn.includes(' - ')) {
              shortEn = shortEn.split(' - ')[0].trim();
            }
            sealTitle = (shortEn && shortEn !== trackSa) ? `${trackSa} • ${shortEn}` : trackSa;
          } else {
            sealTitle = `श्लोकः ${idx + 1} • ${trackTitle}`;
          }
        }

        card.innerHTML = `
          <div class="dialogue-header">
            <span class="speaker-seal ${speakerClass}">〔 ${sealTitle} 〕</span>
            <button class="dialogue-audio-btn" data-index="${idx}" title="Play recitation">▶</button>
          </div>
          <div class="dialogue-body">
            ${bodyHtml}
          </div>
        `;

        card.addEventListener('click', () => {
          if (window.Player) window.Player.playClip(idx);
        });

        const btn = card.querySelector('.dialogue-audio-btn');
        if (btn) {
          btn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (window.Player) window.Player.playClip(idx);
          });
        }

        this.dialoguesWrapper.appendChild(card);
      });
    }

    // Render prose sections if available
    if (contentSections.length > 0) {
      contentSections.forEach((sec, idx) => {
        const card = document.createElement('div');
        card.className = 'dialogue-card prose-card';
        card.dataset.sectionIndex = idx;
        const headingSa = sec.heading_sa || sec.headingSanskrit || '';
        const headingEn = sec.heading || `Section ${sec.page || idx + 1}`;
        const bodySa = sec.body_sa || sec.content_sa || '';
        const bodyEn = sec.body || sec.content_en || '';

        let displayHeading = '';
        let bodyHtml = '';

        if (this.displayView === 'devanagari') {
          displayHeading = headingSa || 'अध्याय-विषयः';
          bodyHtml = `<div class="text-prose" style="font-size:1.02rem; line-height: 1.75; border: none; padding: 0; color: #3e1f08; font-family:'Noto Serif Devanagari', serif;">${(bodySa || 'संस्कृत-साहित्य-समीक्षा').replace(/\n\n/g, '<br><br>')}</div>`;
        } else if (this.displayView === 'english') {
          displayHeading = headingEn;
          bodyHtml = `<div class="text-prose" style="font-size:0.96rem; line-height: 1.6; border: none; padding: 0; color: #45220a;">${(bodyEn || bodySa).replace(/\n\n/g, '<br><br>')}</div>`;
        } else {
          // bilingual
          displayHeading = headingSa ? `${headingSa} • ${headingEn}` : headingEn;
          if (bodySa && bodyEn) {
            bodyHtml = `<div class="text-sanskrit" style="font-size:1.06rem; line-height:1.75; margin-bottom:1rem; font-family:'Noto Serif Devanagari', serif; color:#2c1505;">${bodySa.replace(/\n\n/g, '<br><br>')}</div><div class="text-english" style="font-size:0.95rem; line-height:1.65; color:#4a2b13; border-top:1px dashed rgba(180,83,9,0.25); padding-top:0.75rem;">${bodyEn.replace(/\n\n/g, '<br><br>')}</div>`;
          } else {
            bodyHtml = `<div class="text-prose" style="font-size:0.96rem; line-height: 1.6; border: none; padding: 0; color: #45220a;">${(bodySa || bodyEn).replace(/\n\n/g, '<br><br>')}</div>`;
          }
        }

        card.innerHTML = `
          <div class="dialogue-header">
            <span class="speaker-seal speaker-scholar">〔 ${displayHeading} 〕</span>
          </div>
          <div class="dialogue-body">
            ${bodyHtml}
          </div>
        `;
        this.dialoguesWrapper.appendChild(card);
      });
    }

    if (window.Player) {
      window.Player.setPlaylist(playlist);
    }

    // Initial slide verse filter
    this.filterVersesBySlide(false);

    // Scroll Hint Pill Management
    if (this.scrollHintPill) {
      setTimeout(() => {
        if (this.dialoguesWrapper.scrollHeight > this.dialoguesWrapper.clientHeight + 25) {
          this.scrollHintPill.classList.remove('hidden');
          this.scrollHintPill.style.opacity = '1';
        } else {
          this.scrollHintPill.classList.add('hidden');
        }
      }, 100);

      this.dialoguesWrapper.onscroll = () => {
        if (this.dialoguesWrapper.scrollTop > 20) {
          this.scrollHintPill.style.opacity = '0';
          setTimeout(() => {
            if (this.dialoguesWrapper.scrollTop > 20) this.scrollHintPill.classList.add('hidden');
          }, 350);
        } else if (this.dialoguesWrapper.scrollHeight > this.dialoguesWrapper.clientHeight + 25) {
          this.scrollHintPill.classList.remove('hidden');
          this.scrollHintPill.style.opacity = '1';
        }
      };
    }
  }

  /* ================= SUB-PAGE SLIDE RIBBON & AUDIO SYNC (OPTION 1) ================= */
  initSlideRibbon() {
    if (!this.stageSlideBar) return;
    const slides = this.currentSlides || [];

    if (slides.length <= 1) {
      this.stageSlideBar.classList.add('hidden');
      return;
    }

    this.stageSlideBar.classList.remove('hidden');

    if (this.slideIndicators) {
      this.slideIndicators.innerHTML = '';
      slides.forEach((slide, idx) => {
        const dot = document.createElement('div');
        dot.className = `slide-dot ${idx === 0 ? 'active' : ''}`;
        dot.title = `Slide ${idx + 1}: ${slide.title || ''}`;
        dot.dataset.slideIndex = idx;
        dot.addEventListener('click', () => this.renderSlide(idx, true));
        this.slideIndicators.appendChild(dot);
      });
    }

    this.updateSlideNavControls();
  }

  prevSlide() {
    if (this.activeSlideIndex > 0) {
      this.renderSlide(this.activeSlideIndex - 1, true);
    }
  }

  nextSlide() {
    if (this.currentSlides && this.activeSlideIndex < this.currentSlides.length - 1) {
      this.renderSlide(this.activeSlideIndex + 1, true);
    }
  }

  renderSlide(slideIndex, shouldScroll = true) {
    if (!this.currentSlides || this.currentSlides.length === 0) return;
    const slides = this.currentSlides;
    slideIndex = Math.max(0, Math.min(slideIndex, slides.length - 1));
    this.activeSlideIndex = slideIndex;
    const slide = slides[slideIndex];

    // Smooth GPU Canvas Backdrop crossfade with cache-busting
    if (this.stageCanvasBg && slide.canvas) {
      const targetSrc = slide.canvas.includes('?v=') ? slide.canvas : `${slide.canvas}?v=1.4.2`;
      const currentSrc = this.stageCanvasBg.getAttribute('src');
      if (currentSrc !== targetSrc && currentSrc !== slide.canvas) {
        this.stageCanvasBg.style.opacity = '0.3';
        this.stageCanvasBg.onload = () => {
          this.stageCanvasBg.style.opacity = '1';
        };
        this.stageCanvasBg.src = targetSrc;
      }
    }

    // Update Slide Ribbon UI
    this.updateSlideNavControls();

    // Universal Dual-Pane Presentation (Left: Visual Diagram OR Illuminated Folio Narrative)
    const visualSrc = slide.diagram;
    const visualTitle = slide.diagramTitle || slide.title || 'Manuscript Artwork';
    const sanskritText = slide.proseTextSanskrit || '';
    const englishText = slide.proseText || slide.description || '';
    let prose = '';
    if (this.displayView === 'devanagari') {
      prose = sanskritText || '';
    } else if (this.displayView === 'english') {
      prose = englishText || '';
    } else {
      prose = (sanskritText && englishText) ? `${sanskritText}\n\n${englishText}` : (sanskritText || englishText);
    }

    let allowedIndices = [];
    if (slide && slide.trackIndices && Array.isArray(slide.trackIndices)) {
      allowedIndices = slide.trackIndices;
    } else if (slide && slide.trackIndex !== null && slide.trackIndex !== undefined) {
      allowedIndices = [slide.trackIndex];
    }
    const hasAudioCards = (allowedIndices.length > 0);

    const diagramImgWrap = document.getElementById('stage-diagram-img-wrap');
    const folioNarrativeBox = document.getElementById('folio-narrative-box');
    const folioNarrativeTitle = document.getElementById('folio-narrative-title');
    const folioNarrativeText = document.getElementById('folio-narrative-text');

    if (visualSrc) {
      // Mode A: Diagram visual present
      this.currentDiagram = { src: visualSrc, title: visualTitle };
      if (this.canvasStageWrapper) this.canvasStageWrapper.classList.add('diagram-mode');
      if (this.stageDiagramContainer) this.stageDiagramContainer.classList.remove('hidden');
      if (diagramImgWrap) diagramImgWrap.classList.remove('hidden');
      if (this.stageDiagramImg) {
        this.stageDiagramImg.src = visualSrc;
        this.stageDiagramImg.alt = visualTitle;
      }
      if (this.btnZoomDiagram) this.btnZoomDiagram.classList.remove('hidden');
      if (this.diagramBadge) {
        let badgeText = '';
        if (this.displayView === 'devanagari') {
          if (this.activeChapterId === 2) badgeText = 'वर्णमाला-चित्रम्';
          else if (this.activeChapterId === 3) badgeText = 'चित्रकाव्य-चित्रम्';
          else if (this.activeChapterId === 4) badgeText = 'विज्ञान-चित्रम्';
          else badgeText = slide.titleSanskrit || 'पाण्डुलिपि-चित्रम्';
        } else {
          badgeText = slide.diagramTitle || (this.activeChapterId === 2 ? 'Alphabet Articulation Chart' : 'Visual Artwork & Diagram');
        }
        this.diagramBadge.textContent = badgeText;
      }
      if (this.btnViewDiagram) {
        this.btnViewDiagram.classList.remove('hidden');
        this.btnViewDiagram.title = `Zoom Lightbox: ${visualTitle}`;
        const viewLabel = this.displayView === 'devanagari' ? 'चित्र-दर्शनम्' : 'Diagram View';
        this.btnViewDiagram.innerHTML = `<span>👁️</span> ${viewLabel}`;
      }
      const btnZoom = document.getElementById('btn-zoom-diagram');
      if (btnZoom) {
        btnZoom.textContent = this.displayView === 'devanagari' ? '🔍 चित्र-विस्तारः' : '🔍 Expand Visual';
      }
      if (folioNarrativeBox) {
        folioNarrativeBox.classList.add('hidden');
      }
    } else {
      // Archetype 2: Image + Text Safe-Zone Mode (or Archetype 1 Image-Only)
      this.currentDiagram = null;
      if (this.canvasStageWrapper) this.canvasStageWrapper.classList.remove('diagram-mode');
      if (this.stageDiagramContainer) this.stageDiagramContainer.classList.add('hidden');
      if (this.btnViewDiagram) this.btnViewDiagram.classList.add('hidden');
      if (folioNarrativeBox) folioNarrativeBox.classList.add('hidden');
    }

    // Filter cards to match active slide
    this.filterVersesBySlide(shouldScroll);
  }

  filterVersesBySlide(shouldScroll = true) {
    if (!this.dialoguesWrapper) return;
    const slide = this.currentSlides ? this.currentSlides[this.activeSlideIndex] : null;
    const allCards = this.dialoguesWrapper.querySelectorAll('.dialogue-card');
    if (!allCards || allCards.length === 0) return;

    if (this.verseFilterMode === 'all' || !slide) {
      // Show all cards
      allCards.forEach(c => {
        c.style.display = '';
      });
      // Highlight matching track if any
      const targetIdx = slide ? (slide.trackIndex !== null && slide.trackIndex !== undefined ? slide.trackIndex : (slide.trackIndices && slide.trackIndices.length > 0 ? slide.trackIndices[0] : null)) : null;
      if (targetIdx !== null && shouldScroll) {
        const card = this.dialoguesWrapper.querySelector(`.dialogue-card[data-index="${targetIdx}"]`);
        if (card) {
          allCards.forEach(c => c.classList.remove('active'));
          card.classList.add('active');
          card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
      return;
    }

    // Mode: 'slide' - filter to matching tracks/sections
    const hasExplicitTracks = (slide && slide.trackIndices !== undefined);
    let allowedIndices = [];
    if (slide && slide.trackIndices && Array.isArray(slide.trackIndices)) {
      allowedIndices = slide.trackIndices;
    } else if (slide && slide.trackIndex !== null && slide.trackIndex !== undefined) {
      allowedIndices = [slide.trackIndex];
    }

    let firstVisibleCard = null;
    let visibleCount = 0;

    allCards.forEach(card => {
      // If prose section card
      if (card.classList.contains('prose-card')) {
        if (card.classList.contains('slide-intro-card')) return;
        const secIdx = parseInt(card.dataset.sectionIndex, 10);
        if (slide.sectionIndex !== undefined && slide.sectionIndex !== null) {
          const isMatch = (secIdx === slide.sectionIndex);
          card.style.display = isMatch ? '' : 'none';
          if (isMatch) visibleCount++;
        } else {
          card.style.display = 'none';
        }
        return;
      }

      // Verse card
      const trackIdx = parseInt(card.dataset.index, 10);
      if (hasExplicitTracks) {
        const isMatch = allowedIndices.includes(trackIdx);
        card.style.display = isMatch ? '' : 'none';
        if (isMatch) {
          visibleCount++;
          if (!firstVisibleCard) firstVisibleCard = card;
        }
      } else if (allowedIndices.length > 0) {
        const isMatch = allowedIndices.includes(trackIdx);
        card.style.display = isMatch ? '' : 'none';
        if (isMatch) {
          visibleCount++;
          if (!firstVisibleCard) firstVisibleCard = card;
        }
      } else {
        card.style.display = 'none';
      }
    });

    // Handle pure narrative slides with no matching audio tracks
    let slideCard = this.dialoguesWrapper.querySelector('.slide-intro-card');
    if (slide && slide.layout === 'image-only') {
      if (slideCard) slideCard.style.display = 'none';
      allCards.forEach(c => { c.style.display = 'none'; });
      this.dialoguesWrapper.style.display = 'none';
      return;
    } else {
      this.dialoguesWrapper.style.display = '';
    }

    if (visibleCount === 0 && slide && (slide.description || slide.proseText || slide.proseTextSanskrit)) {
      if (!slideCard) {
        slideCard = document.createElement('div');
        slideCard.className = 'dialogue-card prose-card slide-intro-card';
        this.dialoguesWrapper.appendChild(slideCard);
      }
      slideCard.style.display = '';
      const sealPageLabel = this.displayView === 'devanagari'
        ? `〔 अध्यायः ${this.activeChapterId} — पृष्ठम् ${slide.slideNumber} 〕`
        : `〔 Chapter ${this.activeChapterId} — Page ${slide.slideNumber} 〕`;
      const slideTitleDisplay = (this.displayView === 'devanagari')
        ? (slide.titleSanskrit || 'अध्याय-विषयः')
        : (slide.title || 'Overview');

      let textToDisplay = '';
      const sanskritText = slide.proseTextSanskrit || '';
      const englishText = slide.proseText || slide.description || '';
      if (this.displayView === 'devanagari') {
        textToDisplay = sanskritText || 'संस्कृत-वाङ्मय-परिचयः';
      } else if (this.displayView === 'english') {
        textToDisplay = englishText || sanskritText;
      } else {
        // bilingual
        textToDisplay = (sanskritText && englishText)
          ? `<div class="text-sanskrit" style="font-size:1.08rem; line-height:1.75; margin-bottom:1rem; font-family:'Noto Serif Devanagari', serif; color:#2c1505;">${sanskritText}</div><div class="text-english" style="font-size:0.96rem; line-height:1.65; color:#4a2b13; border-top:1px dashed rgba(180,83,9,0.25); padding-top:0.75rem;">${englishText}</div>`
          : (sanskritText || englishText);
      }

      slideCard.innerHTML = `
        <div class="dialogue-header">
          <span class="speaker-seal speaker-scholar">${sealPageLabel}</span>
        </div>
        <div class="dialogue-body">
          <h3 style="color:#d97706; font-size:1.15rem; margin-bottom:0.75rem; font-family:'Noto Serif Devanagari', serif;">${slideTitleDisplay}</h3>
          <div class="text-prose" style="font-size:1.02rem; line-height:1.75; color:#3e1f08;">${textToDisplay}</div>
        </div>
      `;
      visibleCount++;
      firstVisibleCard = slideCard;
    } else if (slideCard) {
      slideCard.style.display = 'none';
    }

    if (firstVisibleCard && shouldScroll) {
      allCards.forEach(c => c.classList.remove('active'));
      firstVisibleCard.classList.add('active');
      this.dialoguesWrapper.scrollTop = 0;
    }
  }

  updateSlideNavControls() {
    const slides = this.currentSlides || [];
    const count = slides.length;

    if (this.slideCounter) {
      this.slideCounter.textContent = this.displayView === 'devanagari' 
        ? `${this.activeSlideIndex + 1} / ${count} पृष्ठम्` 
        : `Slide ${this.activeSlideIndex + 1} of ${count}`;
    }

    if (this.btnSlidePrev) {
      this.btnSlidePrev.disabled = (this.activeSlideIndex <= 0);
    }
    if (this.btnSlideNext) {
      this.btnSlideNext.disabled = (this.activeSlideIndex >= count - 1);
    }

    // Update active dot in ribbon
    if (this.slideIndicators) {
      const dots = this.slideIndicators.querySelectorAll('.slide-dot');
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === this.activeSlideIndex);
      });
      // Scroll active dot into view if overflowing
      const activeDot = dots[this.activeSlideIndex];
      if (activeDot && this.slideIndicators) {
        const targetLeft = activeDot.offsetLeft - (this.slideIndicators.clientWidth / 2) + (activeDot.clientWidth / 2);
        this.slideIndicators.scrollTo({ left: Math.max(0, targetLeft), behavior: 'smooth' });
      }
    }
  }

  /* Called by Player when an audio track begins playback */
  onTrackChanged(track) {
    if (!track) return;
    if (track.slideIndex !== undefined && track.slideIndex !== null) {
      if (track.slideIndex !== this.activeSlideIndex) {
        this.renderSlide(track.slideIndex, true);
      }
    }
  }

  openDiagramModal(customSrc = null, customTitle = null, customDesc = null) {
    if (!this.modalDiagram) return;
    const img = document.getElementById('modal-diagram-img');
    const desc = document.getElementById('modal-diagram-desc');
    const title = document.getElementById('modal-diagram-title');

    const src = customSrc || (this.currentDiagram && this.currentDiagram.src);
    const t = customTitle || (this.currentDiagram && this.currentDiagram.title) || 'Visual Artwork & Diagram';
    const d = customDesc || (this.currentDiagram && this.currentDiagram.title) || 'Authentic 1997 Visual Artwork & Diagram';

    if (!src) return;
    if (img) img.src = src;
    if (title) title.textContent = t;
    if (desc) desc.textContent = d;

    this.modalDiagram.classList.remove('hidden');
  }

  /* ================= PWA INSTALLATION PROTOCOL ================= */
  initPWAInstallPrompt() {
    const btnInstallDrawer = document.getElementById('btn-install-pwa-drawer');
    const modalInstallGuide = document.getElementById('modal-install-guide');
    const btnCloseInstallModal = document.getElementById('btn-close-install-modal');
    const btnDismissInstallModal = document.getElementById('btn-dismiss-install-modal');
    const modalInstallBackdrop = document.getElementById('modal-install-backdrop');
    const btnTriggerPwa = document.getElementById('btn-trigger-pwa-prompt');

    const openInstallModal = () => {
      if (this.navDrawer) this.navDrawer.classList.remove('open');
      if (this.navBackdrop) this.navBackdrop.classList.add('hidden');
      if (modalInstallGuide) modalInstallGuide.classList.remove('hidden');
      if (btnTriggerPwa) {
        btnTriggerPwa.style.display = window.deferredPWAInstallPrompt ? 'inline-flex' : 'none';
      }
    };

    const closeInstallModal = () => {
      if (modalInstallGuide) modalInstallGuide.classList.add('hidden');
    };

    if (btnInstallDrawer) {
      btnInstallDrawer.addEventListener('click', (e) => {
        e.preventDefault();
        if (window.deferredPWAInstallPrompt) {
          window.deferredPWAInstallPrompt.prompt();
          window.deferredPWAInstallPrompt.userChoice.then(choice => {
            if (choice && choice.outcome === 'accepted') {
              console.log('[PWA] User accepted installation prompt');
            }
            window.deferredPWAInstallPrompt = null;
          }).catch(() => {});
        } else {
          openInstallModal();
        }
      });
    }

    if (btnTriggerPwa) {
      btnTriggerPwa.addEventListener('click', () => {
        if (window.deferredPWAInstallPrompt) {
          window.deferredPWAInstallPrompt.prompt();
          window.deferredPWAInstallPrompt.userChoice.then(choice => {
            if (choice && choice.outcome === 'accepted') {
              console.log('[PWA] User accepted installation prompt');
            }
            window.deferredPWAInstallPrompt = null;
            closeInstallModal();
          }).catch(() => {});
        }
      });
    }

    if (btnCloseInstallModal) btnCloseInstallModal.addEventListener('click', closeInstallModal);
    if (btnDismissInstallModal) btnDismissInstallModal.addEventListener('click', closeInstallModal);
    if (modalInstallBackdrop) modalInstallBackdrop.addEventListener('click', closeInstallModal);

    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      window.deferredPWAInstallPrompt = e;
      if (btnTriggerPwa) btnTriggerPwa.style.display = 'inline-flex';
    });

    window.addEventListener('appinstalled', () => {
      console.log('[PWA] App successfully installed on device.');
      window.deferredPWAInstallPrompt = null;
      closeInstallModal();
    });
  }

  /* ================= SYSTEM MODALS ================= */
  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.remove('hidden');

    if (modalId === 'modal-credits') this.populateCredits();
    if (modalId === 'modal-institu') this.populateInstitutions();
    if (modalId === 'modal-shlokas') this.populateShlokasConcordance();
    if (modalId === 'modal-scholars') this.populateScholars();
    if (modalId === 'modal-gallery') this.populateGallery();
  }

  populateCredits() {
    const roster = document.getElementById('credits-roster');
    if (!roster) return;
    const archival = this.data.archival || {};
    const acks = archival.acknowledgments || {};
    const team = acks.creative_team || [];

    roster.innerHTML = team.map(member => `
      <div style="background:var(--bg-card); padding:10px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle);">
        <div style="color:var(--accent-gold); font-weight:600; font-size:0.9rem;">${member.name}</div>
        <div style="color:var(--text-muted); font-size:0.75rem;">${member.role}</div>
      </div>
    `).join('');
  }

  populateInstitutions() {
    const list = document.getElementById('institutions-list');
    if (!list) return;
    const archival = this.data.archival || {};
    const dir = (archival.institutionsDirectory && archival.institutionsDirectory.directory) || archival.institutions || [];

    list.innerHTML = dir.map(item => {
      if (typeof item === 'string') {
        const match = item.match(/^(\d+)\.\s*(.+),\s*([^,]+)$/);
        let num = '';
        let name = item;
        let loc = '';
        if (match) {
          num = match[1];
          name = match[2];
          loc = match[3];
        } else {
          const numMatch = item.match(/^(\d+)\.\s*(.+)$/);
          if (numMatch) {
            num = numMatch[1];
            name = numMatch[2];
          }
        }
        return `
          <div class="institution-item-card" style="background:var(--bg-card); padding:10px 14px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle); display:flex; align-items:flex-start; gap:12px; transition:var(--transition);">
            <span style="display:inline-flex; align-items:center; justify-content:center; width:26px; height:26px; min-width:26px; border-radius:50%; background:rgba(229,169,60,0.15); border:1px solid var(--accent-gold); color:var(--accent-gold-light); font-size:0.75rem; font-weight:700;">${num}</span>
            <div style="flex:1;">
              <div style="color:var(--accent-gold-light); font-weight:600; font-size:0.9rem; line-height:1.35;">${name}</div>
              ${loc ? `<div style="color:var(--text-muted); font-size:0.78rem; margin-top:3px;">📍 ${loc}</div>` : ''}
            </div>
          </div>
        `;
      } else {
        return `
          <div class="institution-item-card" style="background:var(--bg-card); padding:10px 14px; border-radius:var(--radius-sm); border:1px solid var(--border-subtle); display:flex; align-items:flex-start; gap:12px; transition:var(--transition);">
            <div style="flex:1;">
              <div style="color:var(--accent-gold-light); font-weight:600; font-size:0.9rem;">${item.name_en || item.name}</div>
              ${item.name_sa ? `<div style="color:var(--text-secondary); font-family:var(--font-sanskrit); font-size:0.85rem;">${item.name_sa}</div>` : ''}
              ${item.location ? `<div style="color:var(--text-muted); font-size:0.78rem; margin-top:3px;">📍 ${item.location}</div>` : ''}
            </div>
          </div>
        `;
      }
    }).join('');
  }

  populateShlokasConcordance() {
    const container = document.getElementById('shlokas-concordance-list');
    if (!container) return;
    const chapters = this.data.chapters || [];
    const allRecitations = [];

    chapters.forEach(ch => {
      const tracks = ch.audioTracks || ch.recitations || [];
      const titleSa = ch.titleSanskrit || ch.title_sa || '';
      const titleEn = ch.titleEnglish || ch.title_en || '';
      tracks.forEach((r, idx) => {
        allRecitations.push({
          ...r,
          idx: idx,
          chapterId: ch.id,
          chapterTitle: `Devabhāṣā Chapter ${ch.id}: ${titleEn}`,
          title: r.title || `Chapter ${ch.id} Track ${idx + 1}`,
          sanskrit: r.sanskrit || r.text_sa || '',
          translation: r.translation || r.text_en || ''
        });
      });
    });

    container.innerHTML = allRecitations.map((rec, i) => `
      <div class="search-result-item" data-rec-index="${i}">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="search-result-title">Ch. ${rec.chapterId} — ${rec.title}</span>
          <button class="action-btn" style="padding:4px 10px; font-size:0.78rem; min-height:28px; background:var(--accent-gold); color:#120c08;">▶ Play</button>
        </div>
        <div class="search-result-text" style="font-family:var(--font-sanskrit);">${rec.sanskrit || rec.translation || ''}</div>
      </div>
    `).join('');

    container.querySelectorAll('.search-result-item').forEach((item, idx) => {
      item.addEventListener('click', () => {
        const rec = allRecitations[idx];
        const modal = document.getElementById('modal-shlokas');
        if (modal) modal.classList.add('hidden');
        this.loadChapter(rec.chapterId);
        if (window.Player) window.Player.playClip(rec.idx);
      });
    });
  }

  populateScholars() {
    const roster = document.getElementById('scholars-roster-list');
    if (!roster) return;
    const ch1 = (this.data.chapters || []).find(c => c.id === 1) || {};
    const scholars = [
      ...(ch1.scholars || []),
      {
        name: "Sir C.V. Raman",
        role: "Nobel Laureate in Physics (1930)",
        image: "assets/images/chapter8/raman.jpg",
        quote: "Sanskrit has played a vital role in Indian culture. It is our duty to preserve and study the scientific and rational literature enshrined in this great language."
      },
      {
        name: "Sir William Jones",
        role: "Pioneering Philologist & Jurist (1786)",
        image: "assets/images/chapter9/william jones.jpg",
        quote: "The Sanscrit language, whatever be its antiquity, is of a wonderful structure; more perfect than the Greek, more copious than the Latin, and more exquisitely refined than either."
      },
      {
        name: "Rabindranath Tagore",
        role: "Nobel Laureate in Literature & Poet of 'Gitanjali'",
        image: "assets/images/chapter10/tagore.jpg",
        quote: "Sanskrit has moulded the minds of India's greatest thinkers and visionaries. It carries the heartbeat of our spiritual consciousness across millennia."
      }
    ];

    roster.innerHTML = scholars.map(s => `
      <div class="scholar-roster-card">
        <img class="scholar-avatar" src="${s.image}" alt="${s.name}" loading="lazy" onerror="this.src='assets/icons/icon-192.png'">
        <div class="scholar-info">
          <div class="scholar-name">${s.name}</div>
          <div class="scholar-role">${s.role}</div>
          <div class="scholar-quote">"${s.quote}"</div>
        </div>
      </div>
    `).join('');
  }

  populateGallery() {
    const grid = document.getElementById('master-gallery-grid');
    if (!grid || grid.dataset.populated) return;
    grid.dataset.populated = 'true';

    const items = (typeof DEVABHASHA_GALLERY !== 'undefined') ? DEVABHASHA_GALLERY : [];
    if (!items.length) return;

    const renderGrid = (filter) => {
      const filtered = (filter === 'all') ? items : items.filter(it => it.category === filter);
      grid.innerHTML = filtered.map(item => `
        <div class="gallery-thumb-card" data-src="${item.src}" data-title="${item.title}">
          <img class="gallery-thumb-img" src="${item.src}" alt="${item.title}" loading="lazy" onerror="this.style.opacity='0.2'">
          <div class="gallery-thumb-caption" title="${item.title}">${item.title}</div>
        </div>
      `).join('');

      grid.querySelectorAll('.gallery-thumb-card').forEach(card => {
        card.addEventListener('click', () => {
          this.openDiagramModal(card.dataset.src, card.dataset.title, card.dataset.title);
        });
      });
    };

    renderGrid('all');

    const chipsContainer = document.getElementById('gallery-filter-chips');
    if (chipsContainer) {
      chipsContainer.querySelectorAll('.gallery-filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
          chipsContainer.querySelectorAll('.gallery-filter-btn').forEach(b => b.classList.remove('active'));
          e.currentTarget.classList.add('active');
          renderGrid(e.currentTarget.dataset.filter);
        });
      });
    }
  }
}

// Bootstrap on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  window.app = new DevabhashaApp();
  window.DevabhashaApp = window.app;
  window.DevabhashaInstance = window.app;
});
