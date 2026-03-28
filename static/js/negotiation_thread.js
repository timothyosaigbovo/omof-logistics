// Negotiation thread — auto-refresh every 10 seconds
document.addEventListener('DOMContentLoaded', function () {
    const thread = document.getElementById('negotiation-thread');
    if (!thread) return;

    // Scroll to bottom of thread on load
    thread.scrollTop = thread.scrollHeight;

    // Auto-refresh thread messages every 10 seconds
    setInterval(function () {
        const url = window.location.href;
        fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
            .then(function (response) { return response.text(); })
            .then(function (html) {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newThread = doc.getElementById('negotiation-thread');
                if (newThread && newThread.innerHTML !== thread.innerHTML) {
                    thread.innerHTML = newThread.innerHTML;
                    thread.scrollTop = thread.scrollHeight;
                }
            })
            .catch(function () {});
    }, 10000);
});
