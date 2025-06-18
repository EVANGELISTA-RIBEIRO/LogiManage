// logimanageapp/static/logimanageapp/js/formularios.js

document.addEventListener('DOMContentLoaded', function() {
    const openDocButton = document.getElementById('btn-abrir-requisicao'); // Botão "Abrir"
    const transportNumberModal = document.getElementById('transportNumberModal'); // O modal
    const confirmGenerateDocButton = document.getElementById('confirmGenerateDoc'); // Botão "Gerar Documento" no modal
    const cancelGenerateDocButton = document.getElementById('cancelGenerateDoc'); // Botão "Cancelar" no modal
    const requisicaoIdInput = document.getElementById('requisicaoIdInput'); // Input para o ID

    // Função para mostrar/esconder o modal
    const toggleModal = () => {
        transportNumberModal.classList.toggle('active');
    };

    // Event listener para o botão "Abrir Documento"
    if (openDocButton) {
        openDocButton.addEventListener('click', function(e) {
            e.preventDefault(); // Evita o comportamento padrão do link/botão
            toggleModal(); // Abre o modal
            requisicaoIdInput.focus(); // Coloca o foco no input
        });
    }

    // Event listener para o botão "Cancelar" no modal
    if (cancelGenerateDocButton) {
        cancelGenerateDocButton.addEventListener('click', function() {
            toggleModal(); // Fecha o modal
            requisicaoIdInput.value = ''; // Limpa o input
        });
    }

    // Event listener para o botão "Gerar Documento" no modal
    if (confirmGenerateDocButton) {
        confirmGenerateDocButton.addEventListener('click', function() {
            const requisicaoId = requisicaoIdInput.value.trim();

            if (requisicaoId) {
                // Redireciona para a URL que gera o documento, passando o ID como parâmetro GET
                window.location.href = `/gerar-requisicao-word/?numero_transporte=${requisicaoId}`; // Use a URL absoluta
                toggleModal(); // Fecha o modal
                requisicaoIdInput.value = ''; // Limpa o input
            } else {
                alert('Por favor, insira um Número da Requisição.');
            }
        });
    }
});