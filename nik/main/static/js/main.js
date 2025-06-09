document.addEventListener('DOMContentLoaded', function() {
    function initCalendar() {
        const calendarEl = document.getElementById('calendar');
        if (!calendarEl) return;

        const tripData = JSON.parse(calendarEl.getAttribute('data-trips') || '[]');

        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            height: 400,
            events: tripData.flatMap(trip => {
                const events = [];
                const start = new Date(trip.start);
                const end = new Date(trip.end);

                events.push({
                    title: 'Начало',
                    start: trip.start,
                    color: 'green'
                });

                let current = new Date(start);
                current.setDate(current.getDate() + 1);

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
    }

    function initSidebar() {
        const toggleSidebar = document.getElementById('toggleSidebar');
        const sidebar = document.getElementById('sidebar');

        if (toggleSidebar && sidebar) {
            toggleSidebar.addEventListener('click', function() {
                sidebar.classList.toggle('hidden');
            });
        }
    }

    function initCarousel() {
        const carousel = document.querySelector('.carousel-3d');
        if (!carousel) return;

        const items = document.querySelectorAll('.carousel-item');
        const dots = document.querySelectorAll('.carousel-dot');
        const totalItems = items.length;
        let currentIndex = 0;
        let angle = 0;

        function positionItems() {
            const deg = 360 / totalItems;
            items.forEach((item, i) => {
                const rotateY = i * deg;
                item.style.transform = `rotateY(${rotateY}deg) translateZ(500px)`;
            });
            carousel.style.transform = `translateZ(-500px) rotateY(${-angle}deg)`;
        }

        function nextSlide() {
            currentIndex = (currentIndex + 1) % totalItems;
            angle += 360 / totalItems;
            carousel.style.transform = `translateZ(-500px) rotateY(${-angle}deg)`;
            updateDots();
        }

        function updateDots() {
            dots.forEach(dot => dot.classList.remove('active'));
            dots[currentIndex].classList.add('active');
        }

        dots.forEach(dot => {
            dot.addEventListener('click', function() {
                const newIndex = parseInt(this.getAttribute('data-pos'));
                angle += (newIndex - currentIndex) * (360 / totalItems);
                currentIndex = newIndex;
                carousel.style.transform = `translateZ(-500px) rotateY(${-angle}deg)`;
                updateDots();
            });
        });

        let interval = setInterval(nextSlide, 3000);
        const container = document.querySelector('.carousel-3d-container');
        container.addEventListener('mouseenter', () => clearInterval(interval));
        container.addEventListener('mouseleave', () => {
            interval = setInterval(nextSlide, 3000);
        });

        positionItems();
        updateDots();
    }

    // Запуск всех функций
    initCalendar();
    initSidebar();
    initCarousel();  // ← ЭТОГО НЕ ХВАТАЛО
});
