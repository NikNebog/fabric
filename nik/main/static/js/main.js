document.addEventListener('DOMContentLoaded', function() {
    // Константы для лучшей читабельности
    const SLIDE_INTERVAL_MS = 5000; // 5 секунд для автопрокрутки слайдов
    const SIDEBAR_TRANSITION_DELAY_MS = 50; // Задержка перед включением перехода боковой панели
    const SIDEBAR_HIDE_DELAY_MS = 500; // Задержка перед скрытием боковой панели после завершения перехода

    // Проверка поддержки localStorage
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

    // --- Инициализация календаря ---
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

                    // Добавляем начальное событие
                    events.push({
                        title: 'Начало',
                        start: trip.start,
                        color: 'green'
                    });

                    // Добавляем события для каждого дня командировки
                    let current = new Date(start);
                    // Учитываем, если поездка на один день, чтобы не добавлять "Командировку" после "Начало"
                    if (start.toDateString() !== end.toDateString()) {
                        current.setDate(current.getDate() + 1);
                    }
                    

                    while (current <= end) {
                        events.push({
                            title: 'Командировка',
                            start: new Date(current).toISOString().split('T')[0], // Убеждаемся в формате YYYY-MM-DD
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

    // --- Инициализация боковой панели ---
    function initSidebar() {
        const toggleSidebar = document.getElementById('toggleSidebar');
        const sidebar = document.getElementById('sidebar');

        if (!toggleSidebar || !sidebar) return;

        // Инициализация состояния боковой панели
        const sidebarState = storageAvailable ? localStorage.getItem('sidebarState') : null;

        // Устанавливаем начальное состояние без перехода
        sidebar.style.transition = 'none';

        if (sidebarState !== 'visible') {
            sidebar.style.transform = 'translateX(-100%)';
            sidebar.style.opacity = '0';
            sidebar.style.visibility = 'hidden';
        } else {
            sidebar.classList.add('visible');
            sidebar.style.visibility = 'visible';
        }

        // Включаем анимацию после небольшой задержки
        setTimeout(() => {
            sidebar.style.transition = 'transform 0.5s ease-in-out, opacity 0.3s ease-in-out';
        }, SIDEBAR_TRANSITION_DELAY_MS);

        // Обработчик клика
        toggleSidebar.addEventListener('click', function() {
            const isVisible = sidebar.classList.toggle('visible');

            // Сохраняем состояние
            if (storageAvailable) {
                localStorage.setItem('sidebarState', isVisible ? 'visible' : 'hidden');
            }

            if (!isVisible) {
                // Задерживаем скрытие видимости до завершения перехода
                setTimeout(() => {
                    sidebar.style.visibility = 'hidden';
                }, SIDEBAR_HIDE_DELAY_MS);
            } else {
                sidebar.style.visibility = 'visible';
            }
        });
    }

    // --- Инициализация слайдера ---
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
        let slideInterval; // Объявляем slideInterval здесь, чтобы он был доступен

        // Создаем точки-индикаторы
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('slider-dot');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });

        const dots = document.querySelectorAll('.slider-dot');

        // Функция перехода к слайду
        function goToSlide(index) {
            currentIndex = index;
            updateSlider();
        }

        // Обновление слайдера
        function updateSlider() {
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;

            // Обновляем активные точки
            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === currentIndex);
            });
        }

        // Кнопка "Назад"
        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + slideCount) % slideCount;
            updateSlider();
        });

        // Кнопка "Вперед"
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % slideCount;
            updateSlider();
        });

        // Автопрокрутка
        const startAutoSlide = () => {
            stopAutoSlide(); // Очищаем существующий интервал перед запуском нового
            slideInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % slideCount;
                updateSlider();
            }, SLIDE_INTERVAL_MS);
        };

        const stopAutoSlide = () => {
            clearInterval(slideInterval);
        };

        // Запускаем автопрокрутку при инициализации
        startAutoSlide();

        // Остановка автопрокрутки при наведении, перезапуск при уходе мыши
        slider.addEventListener('mouseenter', stopAutoSlide);
        slider.addEventListener('mouseleave', startAutoSlide);

        // Инициализируем позицию слайдера для первого слайда
        updateSlider();
    }


    // --- Инициализируем все компоненты ---
    try {
        initCalendar();
        initSidebar();
        initSlider(); // Вызываем функцию инициализации слайдера
    } catch (error) {
        console.error('Общая ошибка инициализации:', error);
    }
});