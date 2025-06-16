const openModalButton = document.querySelector("#open-modal");
// Remova a linha que seleciona apenas o closeModalButton pelo ID, pois vamos usar a classe
// const closeModalButton = document.querySelector("#close-modal");
const modal = document.querySelector("#modal");
const fade = document.querySelector("#fade");

// Seleciona TODOS os botões com a classe 'cancel'
const cancelButtons = document.querySelectorAll(".cancel");

const toggleModal = () => {
  modal.classList.toggle("hide");
  fade.classList.toggle("hide");
};

// Adiciona o event listener ao botão que abre o modal e ao fade
// Não inclua mais closeModalButton aqui, pois ele será tratado abaixo com os outros cancelButtons
[openModalButton, fade].forEach((el) => {
  if (el) { // Verifica se o elemento existe antes de adicionar o listener
    el.addEventListener("click", () => toggleModal());
  }
});

// Adiciona o event listener a TODOS os botões 'cancel'
cancelButtons.forEach((button) => {
  button.addEventListener("click", () => toggleModal());
});


const primeiraPagina = document.querySelector("#primeira-pagina");
const segundaPagina = document.querySelector(".segunda-pagina");
const terceiraPagina = document.querySelector(".terceira-pagina");
const quartaPagina = document.querySelector(".quarta-pagina");

const proximo1 = document.querySelector("#proximo-1");
const proximo2 = document.querySelector("#proximo-2");
const proximo3 = document.querySelector("#proximo-3");
const voltar2 = document.querySelector("#voltar-2");
const voltar3 = document.querySelector("#voltar-3");
const voltar4 = document.querySelector("#voltar-4");

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

if (proximo3) {
  proximo3.addEventListener("click", () => {
    terceiraPagina.classList.add("hide");
    quartaPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}

if (voltar4) {
  voltar4.addEventListener("click", () => {
    quartaPagina.classList.add("hide");
    terceiraPagina.classList.remove("hide");
    modal.scrollTop = 0;
  });
}