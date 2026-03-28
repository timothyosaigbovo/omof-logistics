// Tracking timeline — animate items on page load
document.addEventListener('DOMContentLoaded', function () {
    const items = document.querySelectorAll('.timeline-item');
    if (!items.length) return;

    items.forEach(function (item, index) {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        setTimeout(function () {
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
        }, index * 150);
    });
});
