document.addEventListener('DOMContentLoaded', () => {
    const dates = document.querySelectorAll('.calendar-date');
    dates.forEach(date => {
        date.addEventListener('click', () => {
            alert(`Вы выбрали дату: ${date.dataset.date}`);
        });
    });
});
