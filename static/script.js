const textarea = document.getElementById('caixa-texto');
const nomePagina = textarea.dataset.pagina; 
let timeoutId;

// Quando carrega, busca o texto E as subpáginas
fetch(`/api/${nomePagina}`)
    .then(response => response.json())
    .then(data => {
        textarea.value = data.conteudo || "";
        
        // Se existirem subpáginas cadastradas
        if (data.subpaginas && data.subpaginas.length > 0) {
            const sidebar = document.getElementById('sidebar');
            const lista = document.getElementById('lista-subpaginas');
            
            data.subpaginas.forEach(sub => {
                // "sub" será "projetos/ideias".
                const nomeCurto = sub.replace(nomePagina + '/', '');
                
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = '/' + sub;
                a.textContent = '/ ' + nomeCurto;
                
                li.appendChild(a);
                lista.appendChild(li);
            });
            
            // Torna o menu visível
            sidebar.style.display = 'block'; 
        }
    });

// Fica escutando a digitação
textarea.addEventListener('input', () => {
    clearTimeout(timeoutId);
    
    timeoutId = setTimeout(() => {
        fetch(`/api/${nomePagina}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ conteudo: textarea.value })
        }).then(() => {
            // Exibe a notificação na tela
            const toast = document.getElementById('notificacao');
            toast.classList.add('mostrar');
            
            // Esconde a notificação após 2 segundos
            setTimeout(() => {
                toast.classList.remove('mostrar');
            }, 2000);
        });
    }, 1000);
});