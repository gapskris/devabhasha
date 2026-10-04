/**
 * Devabhāṣā Modern — High-Fidelity Audio Player Engine
 * Synchronization: requestAnimationFrame + media.currentTime
 * Auto-fallback: High-Fidelity M4A (192kbps AAC-LC) -> Universal MP3
 * Tolerance: < 50ms drift
 */

class DevabhashaPlayer {
  constructor() {
    this.audio = new Audio();
    this.playlist = [];
    this.currentIndex = 0;
    this.currentTrack = null;
    this.isPlaying = false;
    this.syncCallbacks = [];
    this.animFrameId = null;
    
    // UI elements
    this.playBtn = document.getElementById('btn-player-play');
    this.prevBtn = document.getElementById('btn-player-prev');
    this.nextBtn = document.getElementById('btn-player-next');
    this.progressBar = document.getElementById('audio-scrubber') || document.getElementById('audio-progress');
    this.timeCurrent = document.getElementById('time-current');
    this.timeTotal = document.getElementById('time-total');
    this.titleDisplay = document.getElementById('player-track-title');
    this.subDisplay = document.getElementById('player-track-sub');
    this.volumeSlider = document.getElementById('volume-slider');
    
    this.initListeners();
  }

  initListeners() {
    if (this.playBtn) {
      this.playBtn.addEventListener('click', () => this.togglePlay());
    }
    
    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', () => {
        if (this.currentIndex > 0) {
          this.playClip(this.currentIndex - 1);
        }
      });
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', () => {
        if (this.currentIndex < this.playlist.length - 1) {
          this.playClip(this.currentIndex + 1);
        }
      });
    }

    if (this.progressBar) {
      this.progressBar.addEventListener('input', (e) => {
        if (this.audio.duration) {
          const seekTo = (e.target.value / 100) * this.audio.duration;
          this.audio.currentTime = seekTo;
        }
      });
    }

    if (this.volumeSlider) {
      this.volumeSlider.addEventListener('input', (e) => {
        this.audio.volume = parseFloat(e.target.value);
      });
    }

    // Audio Playback Events
    this.audio.addEventListener('play', () => {
      this.isPlaying = true;
      this.updatePlayState();
      this.startSyncLoop();
    });

    this.audio.addEventListener('pause', () => {
      this.isPlaying = false;
      this.updatePlayState();
      this.stopSyncLoop();
    });

    this.audio.addEventListener('ended', () => {
      this.isPlaying = false;
      this.updatePlayState();
      this.stopSyncLoop();
      // Auto-advance to next track in chapter playlist
      if (this.currentIndex < this.playlist.length - 1) {
        this.playClip(this.currentIndex + 1);
      }
    });

    this.audio.addEventListener('loadedmetadata', () => {
      if (this.timeTotal && !isNaN(this.audio.duration)) {
        this.timeTotal.textContent = this.formatTime(this.audio.duration);
      }
    });

    // Auto-fallback from M4A to MP3 if decoding or network failure occurs
    this.audio.addEventListener('error', () => {
      console.warn('[Player] Audio error on current source:', this.audio.error, this.audio.src);
      if (this.currentTrack && this.audio.src.includes('.m4a') && this.currentTrack.mp3) {
        const mp3Src = encodeURI(this.currentTrack.mp3);
        console.log('[Player] Initiating fallback to universal MP3:', mp3Src);
        this.audio.src = mp3Src;
        if (this.isPlaying) {
          this.audio.play().catch(e => console.warn('[Player] MP3 fallback play error:', e));
        }
      }
    });
  }

  setPlaylist(tracks) {
    this.playlist = tracks || [];
    if (this.playlist.length > 0 && !this.isPlaying) {
      this.loadInitialTrack(0);
    }
  }

  loadInitialTrack(index = 0) {
    if (!this.playlist || !this.playlist[index]) return;
    this.currentIndex = index;
    const track = this.playlist[index];
    this.currentTrack = track;

    const canPlayM4A = this.audio.canPlayType('audio/mp4; codecs="mp4a.40.2"');
    const source = (canPlayM4A && track.m4a) ? track.m4a : (track.mp3 || track.m4a);
    const targetSrc = encodeURI(source);

    if (!this.audio.src.endsWith(targetSrc)) {
      this.audio.src = targetSrc;
    }

    if (this.titleDisplay) this.titleDisplay.textContent = track.title || 'Sanskrit Recitation';
    if (this.subDisplay) this.subDisplay.textContent = track.speaker || track.chapterTitle || 'Devabhāṣā';
    if (this.timeCurrent) this.timeCurrent.textContent = '0:00';
    if (this.progressBar) this.progressBar.value = 0;

    this.updatePlayState();
  }

  playClip(index) {
    if (!this.playlist || !this.playlist[index]) return;

    // Toggle: If currently playing this exact clip, PAUSE IT
    if (this.currentIndex === index && this.isPlaying) {
      this.togglePlay();
      return;
    }

    // Toggle: If this exact clip is paused, RESUME IT
    if (this.currentIndex === index && !this.isPlaying && this.audio.src) {
      this.togglePlay();
      return;
    }

    this.currentIndex = index;
    const track = this.playlist[index];
    this.playTrack(track);
  }

  playTrack(track) {
    if (!track) return;
    this.currentTrack = track;
    
    // Test if m4a supported, otherwise mp3
    const canPlayM4A = this.audio.canPlayType('audio/mp4; codecs="mp4a.40.2"');
    const source = (canPlayM4A && track.m4a) ? track.m4a : (track.mp3 || track.m4a);
    const targetSrc = encodeURI(source);
    
    if (!this.audio.src.endsWith(targetSrc)) {
      this.audio.src = targetSrc;
    }
    
    if (this.titleDisplay) this.titleDisplay.textContent = track.title || 'Sanskrit Recitation';
    if (this.subDisplay) this.subDisplay.textContent = track.speaker || track.chapterTitle || 'Devabhāṣā';

    const playPromise = this.audio.play();
    if (playPromise !== undefined) {
      playPromise.then(() => {
        this.isPlaying = true;
        this.updatePlayState();
        // Synchronize stage canvas slide with currently playing track
        if (window.DevabhashaInstance && typeof window.DevabhashaInstance.onTrackChanged === 'function') {
          window.DevabhashaInstance.onTrackChanged(track);
        }
      }).catch(err => {
        console.warn('[Player] Autoplay prevented, requires user gesture:', err);
        this.isPlaying = false;
        this.updatePlayState();
      });
    }

    this.highlightActiveCard();
  }

  highlightActiveCard() {
    // Update active highlight across cards
    document.querySelectorAll('.dialogue-card').forEach(c => c.classList.remove('active'));
    document.querySelectorAll('.dialogue-audio-btn').forEach(b => {
      b.classList.remove('playing');
      b.textContent = '▶';
    });

    const activeCard = document.querySelector(`.dialogue-card[data-index="${this.currentIndex}"]`);
    if (activeCard) {
      activeCard.classList.add('active');
      const activeBtn = activeCard.querySelector('.dialogue-audio-btn');
      if (activeBtn) {
        activeBtn.classList.add('playing');
        activeBtn.textContent = '❚❚';
      }
    }
  }

  togglePlay() {
    if (this.playlist.length === 0) return;
    
    if (this.isPlaying) {
      this.audio.pause();
    } else {
      if (!this.audio.src || this.audio.src === '' || this.audio.src.endsWith('undefined')) {
        this.playClip(this.currentIndex || 0);
      } else {
        const p = this.audio.play();
        if (p !== undefined) {
          p.then(() => {
            this.isPlaying = true;
            this.updatePlayState();
            if (this.currentTrack && window.DevabhashaInstance && typeof window.DevabhashaInstance.onTrackChanged === 'function') {
              window.DevabhashaInstance.onTrackChanged(this.currentTrack);
            }
          }).catch(err => {
            console.warn('[Player] Play error, attempting reload:', err);
            this.playClip(this.currentIndex || 0);
          });
        }
      }
    }
  }

  updatePlayState() {
    // Bottom player bar play button
    if (this.playBtn) {
      this.playBtn.innerHTML = this.isPlaying ? '❚❚' : '▶';
    }

    // Stage header "Play All in Chapter" button
    const playAllIcon = document.getElementById('play-all-icon');
    const playAllText = document.getElementById('play-all-text');
    if (playAllIcon) playAllIcon.textContent = this.isPlaying ? '❚❚' : '▶';
    if (playAllText) playAllText.textContent = this.isPlaying ? 'Pause Chapter' : 'Play All in Chapter';

    // In-card play buttons
    document.querySelectorAll('.dialogue-audio-btn').forEach((btn) => {
      const idx = parseInt(btn.dataset.index, 10);
      if (idx === this.currentIndex && this.isPlaying) {
        btn.classList.add('playing');
        btn.textContent = '❚❚';
      } else {
        btn.classList.remove('playing');
        btn.textContent = '▶';
      }
    });
  }

  startSyncLoop() {
    this.stopSyncLoop();
    const loop = () => {
      if (this.isPlaying && this.audio.duration) {
        const cur = this.audio.currentTime;
        const dur = this.audio.duration;
        const pct = (cur / dur) * 100;
        
        if (this.progressBar) this.progressBar.value = pct;
        if (this.timeCurrent) this.timeCurrent.textContent = this.formatTime(cur);

        for (const cb of this.syncCallbacks) {
          cb(cur, dur);
        }
      }
      this.animFrameId = requestAnimationFrame(loop);
    };
    this.animFrameId = requestAnimationFrame(loop);
  }

  stopSyncLoop() {
    if (this.animFrameId) {
      cancelAnimationFrame(this.animFrameId);
      this.animFrameId = null;
    }
  }

  formatTime(sec) {
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }
}

// Global player instance
window.Player = new DevabhashaPlayer();
