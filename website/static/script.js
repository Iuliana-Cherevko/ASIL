const currentDate = new Date();

function getWeekRange(date) {
    const day = date.getDay();
    const startDate = new Date(date);
    startDate.setDate(date.getDate() + (day === 6 ? 0 : 0));
    
    const endDate = new Date(startDate);
    endDate.setDate(startDate.getDate() + (6 - startDate.getDay())); // Set to next Saturday

    return [startDate, endDate];
}

function updateCalendar() {
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();

    document.getElementById('calendar-month').textContent = monthNames[month];
    document.getElementById('calendar-year').textContent = year;

    const firstDayOfMonth = new Date(year, month, 1);
    const lastDayOfMonth = new Date(year, month + 1, 0);
    const daysInMonth = lastDayOfMonth.getDate();

    const calendarDays = document.getElementById('calendar-days');
    calendarDays.innerHTML = ''; 

    for (let i = 0; i < firstDayOfMonth.getDay(); i++) {
        const emptyDay = document.createElement('div');
        emptyDay.className = 'calendar__day empty';
        calendarDays.appendChild(emptyDay);
    }

    for (let i = 1; i <= daysInMonth; i++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'calendar__day';
        dayElement.textContent = i;
        calendarDays.appendChild(dayElement);
    }
    highlightCurrentWeek();
}

function highlightCurrentWeek() {
    const [startDate, endDate] = getWeekRange(currentDate);
    const weekDays = document.querySelectorAll('.calendar__day');
    const today = currentDate.getDate();

    console.log("Start Date of Week:", startDate);
    console.log("End Date of Week:", endDate);

    weekDays.forEach(day => {
        const dayNumber = parseInt(day.textContent, 10);

        if (!isNaN(dayNumber)) {
            const dayDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), dayNumber);

            if (dayDate.toDateString() === currentDate.toDateString()) {
                day.style.backgroundColor = '#f19b0e';
                day.style.color = 'white';
            } else if (dayDate >= startDate && dayDate <= endDate && dayDate > currentDate) {
                day.style.backgroundColor = '#c07a0a';
                day.style.color = 'white';
            }
            console.log("Processing Day:", dayNumber, "Date:", dayDate);
        }
    });
}

function updateWeekView(startDate) {
    const weekDays = document.querySelectorAll('.day');
    const weekRange = getWeekRange(startDate);

    weekDays.forEach((dayElement, index) => {
        const currentDate = new Date(weekRange[0]);
        currentDate.setDate(currentDate.getDate() + index);
        dayElement.textContent = currentDate.toLocaleString('en-us', { weekday: 'long' });
    });
}

window.onload = updateCalendar;