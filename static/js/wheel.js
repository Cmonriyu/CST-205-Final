document.addEventListener('DOMContentLoaded', function() {
    const wheel = document.getElementById('wheel');
    const options = document.querySelectorAll('.option');
    const selectedArea = document.getElementById('selected-area');
    const spinButton = document.getElementById('spin');

    // Function to get the currently selected option
    function getSelectedOption() {
        const container = document.getElementById('wheel-container');
        const containerRect = container.getBoundingClientRect();
        const centerY = containerRect.top + containerRect.height / 2;

        let closestOption = null;
        let minDistance = Infinity;

        options.forEach(option => {
            const rect = option.getBoundingClientRect();
            const optionCenterY = rect.top + rect.height / 2;
            const distance = Math.abs(optionCenterY - centerY);

            if (distance < minDistance) {
                minDistance = distance;
                closestOption = option;
            }
        });

        return closestOption;
    }

    // Function to update selected highlight
    function updateSelectedHighlight() {
        options.forEach(option => option.classList.remove('selected'));
        const selected = getSelectedOption();
        if (selected) {
            selected.classList.add('selected');
        }
    }

    // Update selected area and highlight on scroll
    wheel.addEventListener('scroll', function() {
        const selected = getSelectedOption();
        if (selected) {
            selectedArea.value = selected.dataset.value;
        }
        updateSelectedHighlight();
    });

    // Handle click on option
    options.forEach(option => {
        option.addEventListener('click', function() {
            const value = this.dataset.value;
            selectedArea.value = value;
            // Scroll to center this option
            const container = document.getElementById('wheel-container');
            const containerHeight = container.offsetHeight;
            const optionHeight = this.offsetHeight;
            const scrollTop = this.offsetTop - (containerHeight / 2) + (optionHeight / 2);
            wheel.scrollTo({ top: scrollTop, behavior: 'smooth' });
            // Update highlight after scroll
            setTimeout(updateSelectedHighlight, 300);
        });
    });

    // Spin random
    spinButton.addEventListener('click', function() {
        const randomIndex = Math.floor(Math.random() * options.length);
        const randomOption = options[randomIndex];
        const container = document.getElementById('wheel-container');
        const containerHeight = container.offsetHeight;
        const optionHeight = randomOption.offsetHeight;
        const scrollTop = randomOption.offsetTop - (containerHeight / 2) + (optionHeight / 2);
        wheel.scrollTo({ top: scrollTop, behavior: 'smooth' });
        selectedArea.value = randomOption.dataset.value;
        // Update highlight after scroll
        setTimeout(updateSelectedHighlight, 300);
    });

    // Initialize selected area and highlight
    const initialSelected = getSelectedOption();
    if (initialSelected) {
        selectedArea.value = initialSelected.dataset.value;
    }
    updateSelectedHighlight();
});