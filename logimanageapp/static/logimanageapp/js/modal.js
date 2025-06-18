// logimanageapp/static/js/modal.js (ou o caminho correto para o seu modal.js)

const openModalButton = document.querySelector("#open-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

const cancelButtons = document.querySelectorAll(".cancel");

const toggleModal = () => {
  modal.classList.toggle("hide");
  fade.classList.toggle("hide");
};

[openModalButton, fade].forEach((el) => {
  if (el) {
    el.addEventListener("click", () => toggleModal());
  }
});

cancelButtons.forEach((button) => {
  button.addEventListener("click", () => toggleModal());
});

const primeiraPagina = document.querySelector("#primeira-pagina");
const segundaPagina = document.querySelector(".segunda-pagina");
const terceiraPagina = document.querySelector(".terceira-pagina");
// Modifique esta linha para selecionar a div da quarta página corretamente,
// assumindo que ela tem a classe "quarta-pagina"
const quartaPagina = document.querySelector(".quarta-pagina"); // Mantenha como classe se for a classe da div principal

const proximo1 = document.querySelector("#proximo-1");
const proximo2 = document.querySelector("#proximo-2");
const proximo3 = document.querySelector("#proximo-3"); // Certifique-se de que este ID existe no HTML
const voltar2 = document.querySelector("#voltar-2");
const voltar3 = document.querySelector("#voltar-3");
const voltar4 = document.querySelector("#voltar-4"); // Certifique-se de que este ID existe no HTML

if (proximo1) {
  proximo1.addEventListener("click", () => {
    primeiraPagina.classList.add("hide");
    segundaPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}

if (proximo2) {
  proximo2.addEventListener("click", () => {
    segundaPagina.classList.add("hide");
    terceiraPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}

// Lógica para avançar da terceira para a quarta página
if (proximo3) {
  proximo3.addEventListener("click", () => {
    terceiraPagina.classList.add("hide");
    quartaPagina.classList.remove("hide"); // <<< ESTA É A LINHA CRÍTICA
    modal.scrollTop = 0;
  });
}

if (voltar2) {
  voltar2.addEventListener("click", () => {
    segundaPagina.classList.add("hide");
    primeiraPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}

if (voltar3) {
  voltar3.addEventListener("click", () => {
    terceiraPagina.classList.add("hide");
    segundaPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}

// Lógica para voltar da quarta para a terceira página
if (voltar4) {
    voltar4.addEventListener("click", () => {
        quartaPagina.classList.add("hide"); // <<< ESCONDE A QUARTA PÁGINA
        terceiraPagina.classList.remove("hide");
        modal.scrollTop = 0;
    });
}

// ============== CÓDIGO PARA BUSCA AUTOMÁTICA DE EQUIPAMENTO ==============
document.addEventListener('DOMContentLoaded', function() {
    const codigoEquipamentoInput = document.getElementById('id_codigo');
    const nomeEquipamentoInput = document.getElementById('id_equipamento');
    const valorRequisicaoInput = document.getElementById('id_valor');

    if (codigoEquipamentoInput && nomeEquipamentoInput && valorRequisicaoInput) {
        codigoEquipamentoInput.addEventListener('change', function() {
            const codigo = this.value;

            if (codigo) {
                fetch(`/buscar_equipamento/?codigo=${codigo}`)
                    .then(response => {
                        if (!response.ok) {
                            // Se a resposta não for OK (ex: 404), lança um erro
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        if (data.error) {
                            alert(data.error);
                            nomeEquipamentoInput.value = '';
                            valorRequisicaoInput.value = '';
                        } else {
                            nomeEquipamentoInput.value = data.nome;
                            valorRequisicaoInput.value = parseFloat(data.valor).toFixed(2);
                        }
                    })
                    .catch(error => {
                        console.error('Erro na requisição AJAX:', error);
                        alert('Erro ao buscar informações do equipamento. Verifique o console para mais detalhes.');
                        nomeEquipamentoInput.value = '';
                        valorRequisicaoInput.value = '';
                    });
            } else {
                nomeEquipamentoInput.value = '';
                valorRequisicaoInput.value = '';
            }
        });
    }
});