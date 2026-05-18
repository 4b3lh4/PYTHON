
document.addEventListener('DOMContentLoaded', function() {
    
    // Seleciona o formulário de consulta
    const formulario = document.querySelector('form');
    const botaoSubmit = document.querySelector('button');

    // Se o formulário existir na página, adiciona o evento de escuta
    if (formulario) {
        formulario.addEventListener('submit', function() {
            // Modifica o texto do botão para dar um feedback visual ao usuário
            botaoSubmit.textContent = "Acessando rede municipal...";
            botaoSubmit.style.backgroundColor = "#475569";
            botaoSubmit.style.cursor = "wait";
        });
    }
});
