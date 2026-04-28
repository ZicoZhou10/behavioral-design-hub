/**
 * Behavioral Design Score — Embeddable Widget Loader
 *
 * Usage (minimal):
 *   <div id="bds-widget"></div>
 *   <script src="https://behavioral-design-hub.github.io/embed/embed.js"></script>
 *
 * Usage (with options):
 *   <div id="bds-widget" data-theme="light" data-ref="your-site-name"></div>
 *   <script src="https://behavioral-design-hub.github.io/embed/embed.js"></script>
 *
 * Usage (inline script tag):
 *   <script src="https://behavioral-design-hub.github.io/embed/embed.js"
 *           data-theme="dark" data-ref="your-site-name" data-target="my-container-id"></script>
 *
 * Events (postMessage from iframe to parent):
 *   bds:answer   — { type: 'bds:answer', question: 1-5, value: 15|40|70|95 }
 *   bds:complete — { type: 'bds:complete', score: 0-100, dimensions: [...] }
 *   bds:restart  — { type: 'bds:restart' }
 *   bds:resize   — { type: 'bds:resize', height: <px> }
 */
(function() {
  'use strict';

  var BASE_URL = 'https://behavioral-design-hub.github.io/embed/';
  var DEFAULT_HEIGHT = 640;
  var MIN_HEIGHT = 400;

  // Find configuration
  var scriptTag = document.currentScript || (function() {
    var scripts = document.getElementsByTagName('script');
    return scripts[scripts.length - 1];
  })();

  // Configuration sources: script data attributes > container data attributes > defaults
  var targetId = scriptTag.getAttribute('data-target') || 'bds-widget';
  var container = document.getElementById(targetId);

  if (!container) {
    // If no container found, create one before the script tag
    container = document.createElement('div');
    container.id = targetId;
    scriptTag.parentNode.insertBefore(container, scriptTag);
  }

  var theme = scriptTag.getAttribute('data-theme')
    || container.getAttribute('data-theme')
    || 'dark';
  var ref = scriptTag.getAttribute('data-ref')
    || container.getAttribute('data-ref')
    || (window.location.hostname || 'unknown');
  var width = scriptTag.getAttribute('data-width')
    || container.getAttribute('data-width')
    || '100%';
  var maxWidth = scriptTag.getAttribute('data-max-width')
    || container.getAttribute('data-max-width')
    || '720px';

  // Build iframe URL
  var iframeSrc = BASE_URL + '?theme=' + encodeURIComponent(theme)
    + '&ref=' + encodeURIComponent(ref);

  // Create iframe
  var iframe = document.createElement('iframe');
  iframe.src = iframeSrc;
  iframe.style.cssText = 'width:' + width + ';max-width:' + maxWidth
    + ';height:' + DEFAULT_HEIGHT + 'px;border:none;border-radius:12px;'
    + 'display:block;margin:0 auto;overflow:hidden;'
    + 'background:' + (theme === 'light' ? '#f8f9fa' : '#0a0a0f') + ';';
  iframe.setAttribute('title', 'Behavioral Design Score Assessment');
  iframe.setAttribute('loading', 'lazy');
  iframe.setAttribute('allow', 'clipboard-write');
  iframe.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-popups allow-popups-to-navigate-from-opener');

  // Listen for resize messages from the widget
  window.addEventListener('message', function(event) {
    if (!event.data || typeof event.data !== 'object') return;
    if (event.data.type === 'bds:resize' && event.data.height) {
      var newHeight = Math.max(MIN_HEIGHT, event.data.height + 20);
      iframe.style.height = newHeight + 'px';
    }
    // Re-emit events so the host page can listen via window.addEventListener
    if (event.data.type && event.data.type.startsWith('bds:')) {
      var customEvent = new CustomEvent(event.data.type, { detail: event.data });
      document.dispatchEvent(customEvent);
    }
  });

  // Insert
  container.innerHTML = '';
  container.appendChild(iframe);
})();
