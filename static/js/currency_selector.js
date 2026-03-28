// Currency Selector — booking summary page
document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('currency-select');
    if (!select) return;

    const symbols = { GBP: '£', USD: '$', EUR: '€', NGN: '₦', CAD: 'CA$', GHS: 'GH₵' };
    const priceDisplay = document.getElementById('price-display');
    const currencyHidden = document.getElementById('currency-hidden');
    const currencyNote = document.getElementById('currency-note');
    const baseAmount = priceDisplay ? priceDisplay.dataset.amount : null;

    if (!select || !priceDisplay) return;

    select.addEventListener('change', function () {
        const selected = this.value;
        const symbol = symbols[selected] || selected;
        priceDisplay.textContent = symbol + ' ' + baseAmount + ' ' + selected;
        if (currencyHidden) currencyHidden.value = selected;
        if (currencyNote) {
            currencyNote.textContent = selected === priceDisplay.dataset.base
                ? 'No conversion needed — paying in the quoted currency.'
                : 'Stripe will convert to your selected currency at the current exchange rate.';
        }
    });
});
