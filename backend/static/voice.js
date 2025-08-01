// voice.js
window.addEventListener('DOMContentLoaded', function() {
    const micBtn = document.createElement('button');
    micBtn.innerHTML = '🎤 Comando de Voz';
    micBtn.type = 'button';
    micBtn.style = 'margin-left: 20px;';

    document.querySelector('.breadcrumbs')?.appendChild(micBtn);

    micBtn.onclick = function() {
        if (!('webkitSpeechRecognition' in window)) {
            alert('Seu navegador não suporta reconhecimento de voz.');
            return;
        }
        const recognition = new webkitSpeechRecognition();
        recognition.lang = 'pt-BR';
        recognition.start();

        recognition.onresult = function(event) {
            const texto = event.results[0][0].transcript;
            // Preenche o primeiro campo de texto do formulário
            const input = document.querySelector('input[type="text"]');
            if (input) input.value = texto;
        };
    };
}); 