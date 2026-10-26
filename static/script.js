const textarea = document.getElementById('caixa-texto');

const nomePagina = textarea.dataset.pagina; 
let timeoutId;

// Quando carrega, busca o texto
fetch(`/api/${nomePagina}`)
    .then(response => response.json())
    .then(data => {
        textarea.value = data.conteudo || "";
    });

// Fica escutando a digitação
textarea.addEventListener('input', () => {
    clearTimeout(timeoutId);
    
    timeoutId = setTimeout(() => {
        fetch(`/api/${nomePagina}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ conteudo: textarea.value })
        }).then(() => console.log("Salvo automaticamente!"));
    }, 1000);
});