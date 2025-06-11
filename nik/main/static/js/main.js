document.addEventListener('DOMContentLoaded', function() {
    const SLIDE_INTERVAL_MS = 5000;
    const SIDEBAR_TRANSITION_DELAY_MS = 50;
    const SIDEBAR_HIDE_DELAY_MS = 500;
    const storageAvailable = (() => {
        try {
            const testKey = '__test__';
            localStorage.setItem(testKey, testKey);
            localStorage.removeItem(testKey);
            return true;
        } catch {
            return false;
        }
    })();

    function initCalendar() {
        const calendarEl = document.getElementById('calendar');
        if (!calendarEl) return;

        try {
            const tripData = JSON.parse(calendarEl.getAttribute('data-trips') || '[]');
            const calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                height: 400,
                events: tripData.flatMap(trip => {
                    if (!trip.start || !trip.end) return [];

                    const events = [];
                    const start = new Date(trip.start);
                    const end = new Date(trip.end);

                    events.push({
                        title: 'Начало',
                        start: trip.start,
                        color: 'green'
                    });

                    let current = new Date(start);
                    if (start.toDateString() !== end.toDateString()) {
                        current.setDate(current.getDate() + 1);
                    }
                    

                    while (current <= end) {
                        events.push({
                            title: 'Командировка',
                            start: new Date(current).toISOString().split('T')[0],
                            color: 'yellow'
                        });
                        current.setDate(current.getDate() + 1);
                    }

                    return events;
                })
            });
            calendar.render();
        } catch (error) {
            console.error('Ошибка инициализации календаря:', error);
        }
    }

    function initSidebar() {
        const toggleSidebar = document.getElementById('toggleSidebar');
        const sidebar = document.getElementById('sidebar');

        if (!toggleSidebar || !sidebar) return;

        const sidebarState = storageAvailable ? localStorage.getItem('sidebarState') : null;

        sidebar.style.transition = 'none';

        if (sidebarState !== 'visible') {
            sidebar.style.transform = 'translateX(-100%)';
            sidebar.style.opacity = '0';
            sidebar.style.visibility = 'hidden';
        } else {
            sidebar.classList.add('visible');
            sidebar.style.visibility = 'visible';
        }

        setTimeout(() => {
            sidebar.style.transition = 'transform 0.5s ease-in-out, opacity 0.3s ease-in-out';
        }, SIDEBAR_TRANSITION_DELAY_MS);

        toggleSidebar.addEventListener('click', function() {
            const isVisible = sidebar.classList.toggle('visible');

            if (storageAvailable) {
                localStorage.setItem('sidebarState', isVisible ? 'visible' : 'hidden');
            }

            if (!isVisible) {
                setTimeout(() => {
                    sidebar.style.visibility = 'hidden';
                }, SIDEBAR_HIDE_DELAY_MS);
            } else {
                sidebar.style.visibility = 'visible';
            }
        });
    }

    function initSlider() {
        const slider = document.querySelector('.slider');
        const slides = document.querySelectorAll('.slide');
        const prevBtn = document.querySelector('.slider-prev');
        const nextBtn = document.querySelector('.slider-next');
        const dotsContainer = document.querySelector('.slider-dots');

        if (!slider || slides.length === 0 || !prevBtn || !nextBtn || !dotsContainer) {
            console.warn('Элементы слайдера не найдены. Пропуск инициализации слайдера.');
            return;
        }

        let currentIndex = 0;
        const slideCount = slides.length;
        let slideInterval;

        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('slider-dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.slider-dot');

        function goToSlide(index) {
            currentIndex = index;
            updateSlider();
        }

        function updateSlider() {
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;

            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }

        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + slideCount) % slideCount;
            updateSlider();
        });

        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % slideCount;
            updateSlider();
        });

        const startAutoSlide = () => {
            stopAutoSlide();
            slideInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % slideCount;
                updateSlider();
            }, SLIDE_INTERVAL_MS);
        };

        const stopAutoSlide = () => {
            clearInterval(slideInterval);
        };

        startAutoSlide();

        slider.addEventListener('mouseenter', stopAutoSlide);
        slider.addEventListener('mouseleave', startAutoSlide);

        updateSlider();
    }

    try {
        initCalendar();
        initSidebar();
        initSlider();
    } catch (error) {
        console.error('Общая ошибка инициализации:', error);
    }
});