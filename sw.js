/**
 * Devabhāṣā Modern — Service Worker
 * Architecture: Conservative PWA Shell Precaching + Runtime Media Cache
 *
 * MANDATORY SAFETY CONSTRAINTS:
 * 1. VIDEO: Pure Network Passthrough (bypasses SW completely).
 * 2. RANGE REQUESTS: Any request with a 'range' header is NEVER intercepted or served
 *    with a standard 200 response, allowing the browser/server to handle byte ranges natively.
 * 3. CORE SHELL: Precached on install for instant offline availability.
 * 4. AUDIO: Cached at runtime only upon receiving a complete 200 OK response.
 */

const CORE_CACHE_NAME = 'devabhasha-core-v1.4.1';
const MEDIA_CACHE_NAME = 'devabhasha-media-v1.4.1';

// Core Application Shell assets (~2.5 MB total)
const PRECACHE_ASSETS = [
  './',
  'index.html',
  'manifest.json',
  'css/main.css',
  'css/player.css',
  'css/tv.css',
  'js/app.js',
  'js/search.js',
  'js/data.js',
  'js/player.js',
  'js/tv-remote.js',
  'content/data.json',
  'js/gallery_data.js',
  'favicon.ico',
  'assets/icons/icon-192.png',
  'assets/icons/icon-512.png',
  'assets/icons/maskable-512.png',
  'assets/icons/apple-touch-icon.png',
  'assets/images/opening/S01.jpg',
  'assets/images/opening/S02.jpg',
  'assets/images/opening/S03.jpg',
  'assets/images/opening/S04.jpg',
  'assets/images/opening/S05.jpg',
  'assets/images/opening/S06.jpg',
  'assets/images/opening/01.jpg',
  'assets/images/opening/02.jpg',
  'assets/images/opening/03.jpg',
  'assets/images/canvas_parchment.jpg'
];

// INSTALL: Precache core shell and activate immediately
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CORE_CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => {
      return self.skipWaiting();
    })
  );
});

// ACTIVATE: Purge stale core & media caches, and claim clients
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if ((key.startsWith('devabhasha-core-') && key !== CORE_CACHE_NAME) ||
              (key.startsWith('devabhasha-media-') && key !== MEDIA_CACHE_NAME)) {
            console.log('[SW] Purging outdated cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// MESSAGE: Allow clients to command service worker to skip waiting
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// FETCH: Conservative routing with range-request and video safety
self.addEventListener('fetch', (event) => {
  const request = event.request;

  // 1. Only handle GET requests
  if (request.method !== 'GET') {
    return;
  }

  // 2. CRITICAL RANGE SAFETY: Never intercept Range requests with a full 200 response
  // Allow browser and server to handle HTTP 206 Partial Content directly
  if (request.headers.has('range')) {
    return;
  }

  const url = new URL(request.url);

  // 3. VIDEO SAFETY: Pure network passthrough for all video files (.mp4 or /video/)
  if (url.pathname.endsWith('.mp4') || url.pathname.includes('/video/')) {
    return;
  }

  // 4. AUDIO ASSETS: Cache-first at runtime for standard 200 OK responses
  if (url.pathname.endsWith('.m4a') || url.pathname.endsWith('.mp3')) {
    event.respondWith(
      caches.open(MEDIA_CACHE_NAME).then((cache) => {
        return cache.match(request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          return fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              cache.put(request, networkResponse.clone());
            }
            return networkResponse;
          });
        });
      })
    );
    return;
  }

  // 5. STATIC IMAGES & CANVASES: Network-First with Cache Fallback
  // Guarantees updated icons, diagrams, and artwork are immediately visible online
  if (url.pathname.match(/\.(jpg|jpeg|png|webp|svg|gif|ico)$/i)) {
    event.respondWith(
      fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(MEDIA_CACHE_NAME).then((cache) => {
              cache.put(request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          return caches.match(request);
        })
    );
    return;
  }

  // 6. CORE SHELL (HTML, CSS, JS, JSON): Network-First with Cache Fallback
  event.respondWith(
    fetch(request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseClone = networkResponse.clone();
          caches.open(CORE_CACHE_NAME).then((cache) => {
            cache.put(request, responseClone);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        return caches.match(request);
      })
  );
});
