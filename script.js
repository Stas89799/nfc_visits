document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registration-form');
    const cardForm = document.getElementById('card-form');
    const linkContainer = document.getElementById('link-container');

    if (registrationForm) {
        registrationForm.addEventListener('submit', (e) => {
            e.preventDefault();
            // Обработка регистрации пользователя
            window.location.href = 'card.html';
        });
    }

    if (cardForm) {
        cardForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(cardForm);
            const firstname = formData.get('firstname');
            const lastname = formData.get('lastname');
            const phone = formData.get('phone');
            const photo = formData.get('photo');

            // Генерация уникальной ссылки (можно заменить на более сложную логику)
            const uniqueId = `${firstname}-${lastname}-${Date.now()}`;
            const link = `${window.location.origin}/card.html?id=${uniqueId}`;
            
            // Отображение ссылки
            linkContainer.innerHTML = `<p>Ссылка для просмотра визитки: <a href="${link}" target="_blank">${link}</a></p>`;
        });
    }
});